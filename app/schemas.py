from pydantic import BaseModel

class InvoiceCreate(BaseModel):
    customer: str
    amount: float
    description: str

class InvoiceResponse(BaseModel):
    id: int
    customer: str
    amount: float
    description: str

    class Config:
        from_attributes = True   # for SQLAlchemy

class LoginRequest(BaseModel):
    username: str
    password: str