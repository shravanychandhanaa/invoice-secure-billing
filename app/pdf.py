from reportlab.pdfgen import canvas

def create_pdf(invoice):
    file_name = f"invoice_{invoice.id}.pdf"
    c = canvas.Canvas(file_name)

    c.drawString(100, 750, f"Invoice ID: {invoice.id}")
    c.drawString(100, 730, f"Customer: {invoice.customer}")
    c.drawString(100, 710, f"Amount: {invoice.amount}")
    c.drawString(100, 690, f"Description: {invoice.description}")

    c.save()
    return file_name