import PyPDF2

def insert_signature(pdf_file, signature_image, page_number, x, y):
    with open(pdf_file, 'rb') as pdf_file:
        reader = PyPDF2.PdfReader(pdf_file)
        writer = PyPDF2.PdfWriter()

        # Copy pages from the reader to the writer
        for page in reader.pages:
            writer.add_page(page)

        # Add the signature image to the specified page
        page = writer.pages[page_number - 1]
        page.add_image(signature_image, x, y)

        # Save the modified PDF file
        with open('output.pdf', 'wb') as output_file:
            writer.write(output_file)

# Example usage
pdf_file = 'input.pdf'
signature_image = 'signature.png'
page_number = 1
x = 100
y = 200

insert_signature(pdf_file, signature_image, page_number, x, y)