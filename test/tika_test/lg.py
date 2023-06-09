import os
import tika
from tika import parser
from langdetect import detect

# Set proxy environment variables
# os.environ['HTTP_PROXY'] = 'http://daicelproxy3:80'
# os.environ['HTTPS_PROXY'] = 'http://daicelproxy3:80'

# Specify the path to the document file
document_path = 'langdet.pdf'

# Parse the document
parsed_doc = parser.from_file(document_path)

# Extract the text content from the parsed document
text_content = parsed_doc['content']

# Detect the language of the text content
detected_language = detect(text_content)

# Print the detected language
print("Detected Language:", detected_language)

