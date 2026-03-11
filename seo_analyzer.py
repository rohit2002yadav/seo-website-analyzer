# =====================================================
# SEO Website Analyzer
# -----------------------------------------------------
# This script analyzes a webpage for basic SEO elements
# such as:
# - Title tag
# - Meta description
# - Heading structure
# - Image ALT attributes
# - Internal and external links
# - Keyword frequency
#
# It then generates a simple SEO score and suggestions
# for improving the page.
# =====================================================


# Import required libraries

import requests                 # Sends HTTP requests to download webpage content
from bs4 import BeautifulSoup   # Parses and navigates HTML structure
from collections import Counter # Counts frequency of keywords
import re                       # Used for pattern matching and text processing


# Print program title
print("=== SEO Website Analyzer ===")


# Ask the user to enter a website URL for analysis
url = input("Enter website URL: ")


# Attempt to download the webpage
# If the request fails (invalid URL, network issue, etc.)
# the program will stop with an error message
try:
    response = requests.get(url)
except:
    print("Invalid URL")
    exit()


# Extract raw HTML code from the HTTP response
html = response.text


# Parse the HTML using BeautifulSoup
# This converts the raw HTML into a searchable structure
soup = BeautifulSoup(html, "html.parser")


# Display the report heading
print("\n--- SEO REPORT ---\n")


# Initialize the SEO score variable
# Points will be added based on SEO best practices
score = 0


# =====================================================
# TITLE TAG ANALYSIS
# =====================================================

# Extract the title tag from the webpage
# If the page does not contain a title, set it to None
title = soup.title.string if soup.title else None

# Check if the title exists
if title:
    print("Title:", title)
    print("Title Length:", len(title))
    
    # Award points if the page has a title tag
    score += 20
else:
    print("Title: Missing")


# =====================================================
# META DESCRIPTION ANALYSIS
# =====================================================

# Locate the meta description tag in the HTML
meta = soup.find("meta", attrs={"name": "description"})

# Check if a meta description exists and contains content
if meta and meta.get("content"):
    description = meta.get("content")
    
    print("\nMeta Description:", description)
    print("Length:", len(description))
    
    # Award points if meta description exists
    score += 20
else:
    print("\nMeta Description: Missing")


# =====================================================
# HEADING TAG ANALYSIS
# =====================================================

# Extract all H1 and H2 heading tags
h1_tags = soup.find_all("h1")
h2_tags = soup.find_all("h2")

# Print the number of headings found
print("\nH1 Tags:", len(h1_tags))
print("H2 Tags:", len(h2_tags))

# SEO best practice recommends using exactly one H1 tag
if len(h1_tags) == 1:
    score += 15


# =====================================================
# IMAGE SEO ANALYSIS
# =====================================================

# Extract all image tags from the page
images = soup.find_all("img")

# Counter for images missing ALT attributes
missing_alt = 0

# Check each image for ALT text
for img in images:
    if not img.get("alt"):
        missing_alt += 1

print("\nTotal Images:", len(images))
print("Images without ALT:", missing_alt)

# If every image has ALT text, award SEO points
if missing_alt == 0:
    score += 15


# =====================================================
# LINK ANALYSIS
# =====================================================

# Extract all hyperlinks (<a> tags)
links = soup.find_all("a")

internal = 0
external = 0

# Loop through all links to classify them
for link in links:
    href = link.get("href")

    if href:
        # If the link contains the current website URL
        # it is treated as an internal link
        if url in href:
            internal += 1

        # Links starting with "http" are treated as external
        elif "http" in href:
            external += 1

print("\nInternal Links:", internal)
print("External Links:", external)

# Pages with more internal links typically have better SEO structure
if internal > 5:
    score += 10


# =====================================================
# KEYWORD EXTRACTION
# =====================================================

# Extract all visible text from the webpage
text = soup.get_text().lower()

# Use regex to extract words with at least 4 characters
# This helps ignore very short words like "a", "an", "to"
words = re.findall(r'\b[a-z]{4,}\b', text)

# Count the frequency of words and get top 10
common_words = Counter(words).most_common(10)

print("\nTop Keywords:")

# Display most common keywords and their counts
for word, count in common_words:
    print(word, "-", count)

# Award points for keyword analysis
score += 20


# =====================================================
# FINAL SEO SCORE
# =====================================================

print("\n--- SEO SCORE ---")

# Display final score out of 100
print("Score:", score, "/ 100")


# =====================================================
# SEO RECOMMENDATIONS
# =====================================================

print("\n--- SEO RECOMMENDATIONS ---")

# Suggest improvements based on issues detected

if not title:
    print("- Add a title tag")

if not meta:
    print("- Add a meta description")

if len(h1_tags) != 1:
    print("- Use exactly one H1 tag")

if missing_alt > 0:
    print("- Add ALT text to images")

if internal < 5:
    print("- Add more internal links")


# End of analysis
print("\nAnalysis Complete.")