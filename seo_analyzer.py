import requests
from bs4 import BeautifulSoup

# Ask user for URL
url = input("Enter website URL: ")

# Download webpage
response = requests.get(url)

# Get HTML code
html = response.text

# Parse HTML
soup = BeautifulSoup(html, "html.parser")

# Extract title
title = soup.title.string if soup.title else "No title found"

print("\nWebsite Title:", title)