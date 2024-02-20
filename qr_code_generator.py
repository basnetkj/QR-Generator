import qrcode
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


def generate_qr_code(text, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)


def create_pdf_with_qr_code(text, pdf_filename, qr_filename):
    c = canvas.Canvas(pdf_filename, pagesize=letter)
    width, height = letter

    # Add text to the PDF
    c.drawString(1 * inch, 10 * inch, text)

    # Add QR code image to the PDF
    c.drawInlineImage(qr_filename, 1 * inch, 6 * inch, width=2*inch, height=2*inch)

    c.save()


if __name__ == "__main__":
    text_input = input("Enter the text for the QR code and PDF: ")
    qr_filename = "qr_code.png"
    pdf_filename = "document_with_qr.pdf"

    # Generate QR code
    generate_qr_code(text_input, qr_filename)

    # Create PDF with QR code
    create_pdf_with_qr_code(text_input, pdf_filename, qr_filename)

    print(f"PDF '{pdf_filename}' with QR code generated successfully.")
