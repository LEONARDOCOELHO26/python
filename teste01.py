import PyPDF2

def generate_pdf(pdf_file_name):
    # Create a PDF object
    pdf = PyPDF2.PdfFileWriter()

    # Create a PDF page
    page = pdf.addBlankPage(300, 300)

    # Get the page's content stream
    content = page.getContentStream()

    # Write some text to the page
    content.writeText("Hello World!")

    # Save the PDF to a file
    with open(pdf_file_name, 'wb') as f:
        pdf.write(f)
