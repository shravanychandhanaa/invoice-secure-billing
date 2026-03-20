from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from fastapi.security import OAuth2PasswordRequestForm

from . import models, database, schemas
from .auth import authenticate_user, create_token, get_current_user
from .pdf import create_pdf

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=database.engine)

# DB Dependency
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()


# 🔐 LOGIN API (OAuth2 compatible)
@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if not authenticate_user(form_data.username, form_data.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}  # nosec


# 🔒 CREATE INVOICE (Protected)
@app.post("/invoice/", response_model=schemas.InvoiceResponse)
def create_invoice(
    invoice: schemas.InvoiceCreate,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    new_invoice = models.Invoice(**invoice.dict())
    db.add(new_invoice)
    db.commit()
    db.refresh(new_invoice)
    return new_invoice


# 🔒 GET ALL INVOICES (Protected)
@app.get("/invoice/", response_model=list[schemas.InvoiceResponse])
def get_invoices(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return db.query(models.Invoice).all()


# 🔒 GENERATE PDF (Protected)
@app.get("/invoice/{id}/pdf")
def generate_pdf(
    id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    invoice = db.query(models.Invoice).filter(models.Invoice.id == id).first()

    if not invoice:
        raise HTTPException(status_code=404, detail="Invoice not found")

    file_path = create_pdf(invoice)
    return FileResponse(file_path, media_type='application/pdf', filename=file_path)

