from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO

def extract_text_from_pdf(file_path, page_number):
    resource_manager = PDFResourceManager()
    output_string = StringIO()
    codec = 'utf-8'
    laparams = LAParams()

    with open(file_path, 'rb') as file:
        interpreter = PDFPageInterpreter(resource_manager, TextConverter(resource_manager, output_string, codec=codec, laparams=laparams))
        page = list(PDFPage.get_pages(file))[page_number - 1]  # Subtract 1 to account for 0-based indexing
        interpreter.process_page(page)

    text = output_string.getvalue()
    output_string.close()

    return text

# Provide the path to your PDF file and the page number to extract
pdf_file_path = 'yuan2020.pdf'
page_number = 1
extracted_text = extract_text_from_pdf(pdf_file_path, page_number)

# Print extracted text using the appropriate encoding
print(extracted_text.encode('cp932', errors='ignore').decode('cp932'))