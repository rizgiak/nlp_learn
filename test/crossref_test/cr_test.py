import requests

# Specify the API endpoint
endpoint = "https://api.crossref.org/works"

# Set up the query parameters
params = {
    "query.title": "Conjugated polymers for visible-light-driven photocatalysis",
    "rows": 10  # Number of results to retrieve
}

# Send the API request
response = requests.get(endpoint, params=params)

# Parse the JSON response
data = response.json()

# Extract the relevant information from the response
if data["status"] == "ok":
    papers = data["message"]["items"]
    for paper in papers:
        # Access the paper information
        title = paper["title"][0]
        # authors = paper["author"]
        # Extract other desired information

        # Process or display the information as needed
        print("Title:", title)
        # print("Authors:", authors)
        print("")
