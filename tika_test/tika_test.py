import os
import tika
from tika import parser

# Set proxy environment variables
os.environ['HTTP_PROXY'] = 'http://daicelproxy3:80'
os.environ['HTTPS_PROXY'] = 'http://daicelproxy3:80'

tika.initVM()

# Specify the path to the PDF file
pdf_path = 'robotics-11-00130-v2.pdf'

# Parse the PDF file
parsed_pdf = parser.from_file(pdf_path)

# Extract the text content from the parsed PDF
text_content = parsed_pdf['content']

# Print the extracted text
print(text_content)