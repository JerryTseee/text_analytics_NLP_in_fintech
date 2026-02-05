# This script shows how to download and parse a Wikipedia page using
# Requests and Beautiful Soup. We also use the `re` module for regular
# expressions.
import re
import requests
from bs4 import BeautifulSoup # Beautiful Soup is a Python library used primarily for web scraping

# need to define headers (Wikipedia blocks requests without User-Agent headers to prevent abusive scraping)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

r = \
    requests.get(
        'https://en.wikipedia.org/wiki/Natural_language_processing',
        timeout=3,
        headers=headers)
s = BeautifulSoup(r.text, 'lxml') # Use `lxml` to parse the webpage.

# Take a look at the parsed webpage.
print(s.prettify())

# Extract all the text from the webpage. THIS IS WHAT YOU NEED MOST
# OFTEN FOR NLP AND TEXT ANALYTICS, unless you need to extract only
# part of the webpage.
print(s.get_text())

# Ways to navigate the data structure by HTML tag. This will find the
# FIRST tag of that name (not ALL the tags of that name) in the HTML
# document.
s.title
s.title.name
s.title.string
s.title.parent.name
s.p               # First 'p' tag.
s.p.get_text()
s.p['class']      # In our example, there's no 'class' HTML attribute.
s.header['class']
s.a               # First 'a' tag.

# With the `find` and `find_all` methods you can dive deeper into the
# HTML and have more control over what you extract. The difference
# between `find` and the `find_all` is that the former only finds the
# FIRST child of this tag matching the given criterial, while the
# latter gets ALL of them.
# 
# We start with a demonstration of `find`. HTML tags may have
# attributes, e.g. an 'a' tag usually has a 'href' attribute as in `<a
# href="...">...</a>`. In the following line of code we find the first
# tag that has an 'id' attribute with value 'footer'. This is probably
# the easiest way to extract part of a webpage (assuming the part of
# the webpage you would like to extract has a corresponding
# attribute).
s.find(id='footer')
# Alternatively you can also use a CSS selector using the `select`
# method. This works no matter whether the part you're trying to
# extract has tag with a specific attribute or not.
s.select('#footer')
# Keep in mind that XPath is not directly supported by BeautifulSoup.

# Extract all 'a' tags.
atags = s.find_all('a')           # Find all `<a ...>...</a>` tags.
atags[3]
atags[3].name
atags[3].get('href') # Get the actual `href` attribute (i.e. the URL).

# If we want to get all `href` attributes, we loop over all `a` tags.
{tag.get('href') for tag in s.find_all('a')}

# Find all tags whose names start with the letter 'b' (in this case
# 'body', 'b', and 'br').
{tag.name for tag in s.find_all(re.compile('^b'))}

# Find all tags whose name contains the letter 't'.
{tag.name for tag in s.find_all(re.compile('t'))}

# We can also pass a list to the `find_all` method, in which case bs4
# allows a string match against any item in that list.
{tag.name for tag in s.find_all(['a', 'body'])}

# Find all the tags in the document, but none of the text
# strings. `True` matches anything it can.
{tag.name for tag in s.find_all(True)}
