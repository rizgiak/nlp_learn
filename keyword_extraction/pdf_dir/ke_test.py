import os
import PyPDF2
import string
from collections import Counter

# Define a function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        text = ''
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

# Define a function to preprocess and tokenize the text
def preprocess_and_tokenize(text):
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    # Split into individual words
    tokens = text.split()
    # Remove stop words
    stopwords = set(open('stopwords.txt').read().split())
    tokens = [token for token in tokens if token not in stopwords]
    return tokens

# Define a function to count the frequency of each token
def count_token_frequency(tokens):
    counter = Counter(tokens)
    return counter

# Define a function to select the top N keywords
def select_top_keywords(counter, N):
    keywords = [token for token, count in counter.most_common(N)]
    return keywords

# Define a function to filter out irrelevant words
def filter_keywords(keywords):
    # Add any additional filtering logic here
    return keywords

# Define the main function to process all the PDF files in a directory
def process_directory(directory_path, N):
    all_tokens = []
    for filename in os.listdir(directory_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(directory_path, filename)
            text = extract_text_from_pdf(file_path)
            tokens = preprocess_and_tokenize(text)
            all_tokens.extend(tokens)
    counter = count_token_frequency(all_tokens)
    keywords = select_top_keywords(counter, N)
    filtered_keywords = filter_keywords(keywords)
    return filtered_keywords

# Call the main function with the directory containing the PDF files and the desired number of keywords
keywords = process_directory('pdf_directory', 10)
print(keywords)