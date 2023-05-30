import spacy

def extract_keywords(text):
    # Load the language model
    nlp = spacy.load('en_core_web_sm')

    # Process the text
    doc = nlp(text)

    # Filter out stopwords and punctuation marks
    keywords = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]

    # Perform frequency analysis and select the most frequent keywords
    keyword_freq = {}
    for keyword in keywords:
        keyword_freq[keyword] = keyword_freq.get(keyword, 0) + 1

    # Sort the keywords by frequency in descending order
    sorted_keywords = sorted(keyword_freq, key=keyword_freq.get, reverse=True)

    # Return the top N keywords
    top_n = 5  # Adjust the value as per your requirements
    return sorted_keywords[:top_n]

def load_text_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Example usage
paragraph = load_text_from_file("spacy_test/par.txt")
print(paragraph)
keywords = extract_keywords(paragraph)
print(keywords)