"""
Utility
"""
# pylint: disable=C0103
import re
import json
import requests


# Import Keyword Extractor KeyBERT
from keybert import KeyBERT
import yake


def _cut_text_between_patterns(text, start_pattern, end_pattern):
    """
    cut_text_between_patterns
    """
    pattern = re.escape(start_pattern) + r"(.*?)" + re.escape(end_pattern)
    match = re.search(pattern, text, re.DOTALL)
    if match:
        return match.group(1)
    return ""


def abstract_extraction(text):
    """
    abstract_extraction
    """
    text = text.lower()
    start_pattern = "abstract"
    end_pattern = "introduction"
    result = _cut_text_between_patterns(text, start_pattern, end_pattern)
    return result


def metadata_extraction(text):
    """
    metadata_extraction
    """
    data = json.loads(text)
    return data


def keywords_extraction(text):
    """
    keywords_extraction
    """
    # Create candidates
    kw_extractor = yake.KeywordExtractor(top=100)
    candidates = kw_extractor.extract_keywords(text)
    candidates = [candidate[0] for candidate in candidates]

    i = 0
    for candidate in candidates:
        candidates[i] = candidate.lower()
        i += 1

    # Pass candidates to KeyBERT
    kw_model = KeyBERT()
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 10),
        candidates=candidates,
        stop_words="english",
        use_mmr=True,
        diversity=0.4,
    )
    return keywords


def crossref_search(title):
    """
    crossref_search
    """
    # Specify the API endpoint
    ENDPOINT = "https://api.crossref.org/works"

    # Set up the query parameters
    params = {
        "query.title": title,
        "rows": 1  # Number of results to retrieve
    }

    # Send the API request
    response = requests.get(ENDPOINT, params=params, timeout=10)

    # Parse the JSON response
    data = response.json()

    # Extract the relevant information from the response
    if data["status"] == "ok":
        papers = data["message"]["items"]
        if len(papers) > 0:
            paper = papers[0]
            # Access the paper information
            title_f = paper["title"][0]
            if title.lower() == title_f.lower():  # check if the result is same with the query
                return paper
    return ""


def crossref_similar_search(title, rows):
    """
    crossref_search
    """
    # Specify the API endpoint
    ENDPOINT = "https://api.crossref.org/works"

    # Set up the query parameters
    params = {
        "query.title": title,
        "rows": rows  # Number of results to retrieve
    }

    # Send the API request
    response = requests.get(ENDPOINT, params=params, timeout=10)

    # Parse the JSON response
    data = response.json()

    paper_list = []
    # Extract the relevant information from the response
    if data["status"] == "ok":
        papers = data["message"]["items"]
        if len(papers) > 0:
            for paper in papers:
                paper_list.append(paper["title"][0])
    return paper_list
            


def crossref_reference_doi_list(data):
    return "go"
