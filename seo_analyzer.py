import requests
from bs4 import BeautifulSoup
from collections import Counter
import re

print("=== SEO Website Analyzer ===")

url = input("Enter website URL: ")

try:
    response = requests.get(url)
except:
    print("Invalid URL")
    exit()

html = response.text

soup = BeautifulSoup(html, "html.parser")

print("\n--- SEO REPORT ---\n")

score = 0

# TITLE TAG
title = soup.title.string if soup.title else None

if title:
    print("Title:", title)
    print("Title Length:", len(title))
    score += 20
else:
    print("Title: Missing")

# META DESCRIPTION
meta = soup.find("meta", attrs={"name": "description"})

if meta and meta.get("content"):
    description = meta.get("content")
    print("\nMeta Description:", description)
    print("Length:", len(description))
    score += 20
else:
    print("\nMeta Description: Missing")

# HEADINGS
h1_tags = soup.find_all("h1")
h2_tags = soup.find_all("h2")

print("\nH1 Tags:", len(h1_tags))
print("H2 Tags:", len(h2_tags))

if len(h1_tags) == 1:
    score += 15

# IMAGES
images = soup.find_all("img")

missing_alt = 0

for img in images:
    if not img.get("alt"):
        missing_alt += 1

print("\nTotal Images:", len(images))
print("Images without ALT:", missing_alt)

if missing_alt == 0:
    score += 15

# LINKS
links = soup.find_all("a")

internal = 0
external = 0

for link in links:
    href = link.get("href")

    if href:
        if url in href:
            internal += 1
        elif "http" in href:
            external += 1

print("\nInternal Links:", internal)
print("External Links:", external)

if internal > 5:
    score += 10

# KEYWORD EXTRACTION
text = soup.get_text().lower()

words = re.findall(r'\b[a-z]{4,}\b', text)

common_words = Counter(words).most_common(10)

print("\nTop Keywords:")

for word, count in common_words:
    print(word, "-", count)

score += 20

# SEO SCORE
print("\n--- SEO SCORE ---")

print("Score:", score, "/ 100")

# RECOMMENDATIONS
print("\n--- SEO RECOMMENDATIONS ---")

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

print("\nAnalysis Complete.")