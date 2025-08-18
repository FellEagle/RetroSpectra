# Import the function that fetches data from Wikipedia
from model import fetch_wikipedia_data

# -------------------------------
# Function: process_query
# Purpose: Handle user query and return structured data
# -------------------------------
def process_query(query):
    # Call the fetch_wikipedia_data function from model.py
    data = fetch_wikipedia_data(query)

    # If no data is returned, send back an error message
    if not data:
        return {"error": "No data found for this topic."}

    # Otherwise, return the structured Wikipedia data (title, summary, etc.)
    return data
