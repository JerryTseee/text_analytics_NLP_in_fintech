# This script connects to NewsData.io through their API and fetches
# top breaking news from the past 48 hours. You can obtain a free API
# key by creating an account on https://newsdata.io, then enter the
# API key into the file named `code-API-key-newsdataio.txt`.

import requests
import json                     # For pretty printing.

# Read API key from file or paste as text string, for example:
API_KEY = 'pub_3292db9aea7e492e8b797baa8b380d18' # go to newsdata.io to get a free key yourself
# or
# with open('../code-API-key-newsdataio.txt', 'r') as f: 
#     API_KEY = f.read().strip()

# Retrieve the latest news.
response = \
    requests.get(
        f'https://newsdata.io/api/1/latest?apikey={API_KEY}')
# sort_keys=True` `sorts the JSON keys alphabetically (e.g.,
# "article_id" before "category", and top-level like "nextPage" before
# "results").
print(
    json.dumps(
        response.json(),
        indent=4,
        sort_keys=True))

# Retrieve the latest news about Apple company (stock ticker: AAPL).
stock = 'AAPL'
response = \
    requests.get(
        ('https://newsdata.io/api/1/latest?'
         f'apikey={API_KEY}'
         f'&q={stock}'
         '&category=business'
         '&language=en'))

# Print everything. But on the free tier, many fields are empty or
# filled with placeholders.
print(
    json.dumps(
        response.json(),
        indent=4,
        sort_keys=True))

# Print only a few selected fields.
for article in response.json()['results']:
    print(f"Title: {article['title']}")
    print(f"Published: {article['pubDate']}")
    print(f"Source: {article['source_name']}")
    print(f"Creator: {article['creator']}")
    print(f"Description: {article['description']}")
    print(f"Content: {article['content']}") # Only in paid plan.
    print(f"Link: {article['link']}")
    print('-' * 80)  # Separator for readability.
