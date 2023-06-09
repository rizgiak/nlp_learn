import gensim
from gensim import corpora
from pprint import pprint

# Sample documents
documents = [
    "Machine learning is the future of artificial intelligence",
    "Python is a popular programming language for data analysis",
    "Data science includes various techniques and algorithms",
    "Artificial intelligence helps in automating tasks",
    "Python libraries are widely used in machine learning"
]

# Tokenize the documents
tokenized_docs = [doc.lower().split() for doc in documents]

# Create a dictionary of unique words
dictionary = corpora.Dictionary(tokenized_docs)

# Convert tokenized documents to bag of words (BoW) format
bow_corpus = [dictionary.doc2bow(doc) for doc in tokenized_docs]

# Train the LDA model
lda_model = gensim.models.LdaModel(
    bow_corpus,
    num_topics=2,
    id2word=dictionary,
    passes=10,
    alpha='auto',
    random_state=42
)

# Print the topics and their top words
pprint(lda_model.print_topics())

# Perform inference on a new document
new_doc = "Machine learning and data science go hand in hand"
new_doc_bow = dictionary.doc2bow(new_doc.lower().split())
new_doc_topics = lda_model.get_document_topics(new_doc_bow)

# Print the inferred topic distribution for the new document
pprint(new_doc_topics)