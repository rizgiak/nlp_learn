import io
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from pdfminer.utils import get_level

def extract_headings_and_content(pdf_path):
    headings = []
    content = []

    # Create a PDF resource manager and set parameters
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    laparams = LAParams()

    # Create a string buffer to store the extracted text
    output_string = io.StringIO()

    # Create a PDF interpreter object
    with open(pdf_path, 'rb') as file:
        interpreter = PDFPageInterpreter(rsrcmgr, TextConverter(rsrcmgr, output_string, codec=codec, laparams=laparams))
        for page in PDFPage.get_pages(file):
            interpreter.process_page(page)

            # Extract the content of the page
            page_content = output_string.getvalue()
            output_string.truncate(0)  # Clear the string buffer

            # Extract headings and content from the page
            headings.extend(extract_headings_from_page(page_content))
            content.extend(extract_content_from_page(page_content))

    return headings, content

def extract_headings_from_page(page_content):
    headings = []

    lines = page_content.split('\n')
    for line in lines:
        level = get_level(line)
        if level > 0:
            headings.append(line.strip())

    return headings

def extract_content_from_page(page_content):
    content = []

    lines = page_content.split('\n')
    is_heading = False
    current_block = ''
    for line in lines:
        level = get_level(line)
        if level > 0:
            if current_block:
                content.append(current_block.strip())
                current_block = ''
            is_heading = True
        elif line.strip():
            current_block += line + ' '
        elif is_heading and not line.strip():
            is_heading = False

    if current_block:
        content.append(current_block.strip())

    return content

# Usage example
pdf_path = '../tika_test/robotics-11-00130-v2.pdf'
headings, content = extract_headings_and_content(pdf_path)
for heading, text in zip(headings, content):
    print(heading)
    print(text)
    print('---')