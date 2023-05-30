from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import BytesIO

def extract_text_from_pdf(file_path):
    resource_manager = PDFResourceManager()
    output_string = BytesIO()
    codec = 'utf-8'
    laparams = LAParams()

    with open(file_path, 'rb') as file:
        interpreter = PDFPageInterpreter(resource_manager, TextConverter(resource_manager, output_string, codec=codec, laparams=laparams))
        for page in PDFPage.get_pages(file, check_extractable=True):
            interpreter.process_page(page)

    text = output_string.getvalue().decode('utf-8')
    output_string.close()
    
    return text

# Provide the path to your PDF file
pdf_file_path = 'yuan2020.pdf'
extracted_text = extract_text_from_pdf(pdf_file_path)

# Print extracted text using the appropriate encoding
print(extracted_text.encode('cp932', errors='ignore').decode('cp932'))