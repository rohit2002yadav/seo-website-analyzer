
SEO Website Analyzer

A Python-based tool that analyzes a webpage for basic SEO factors and generates a simple SEO report.

Project Overview
The SEO Website Analyzer takes a website URL as input and analyzes the webpage for several SEO best practices. It then generates a report that includes SEO insights and recommendations.

Features
- Title tag presence and length
- Meta description detection
- Heading structure (H1 and H2 tags)
- Image ALT attribute analysis
- Internal and external link analysis
- Keyword extraction from webpage content
- Basic SEO score calculation
- SEO improvement recommendations

Technologies Used
- Python
- BeautifulSoup
- Requests
- Regular Expressions (re)
- Collections (Counter)

Project Structure

seo-website-analyzer
│
├── seo_analyzer.py
├── requirements.txt
└── README.md

Installation

Clone the repository:
git clone https://github.com/YOUR_USERNAME/seo-website-analyzer.git

Navigate into the project directory:
cd seo-website-analyzer

Install dependencies:
pip install -r requirements.txt

How to Run

python seo_analyzer.py

Enter website URL: https://example.com

Example Output

=== SEO Website Analyzer ===

--- SEO REPORT ---

Title: Example Domain
Title Length: 14

Meta Description: Missing

H1 Tags: 1
H2 Tags: 0

Total Images: 0
Images without ALT: 0

Internal Links: 1
External Links: 1

Top Keywords:
example - 4
domain - 2

--- SEO SCORE ---
Score: 70 / 100

Learning Outcomes
- Web scraping using Python
- Parsing HTML using BeautifulSoup
- Extracting SEO signals from webpages
- Keyword frequency analysis
- Automating SEO auditing tasks

Future Improvements
- Export SEO reports to CSV
- Crawl multiple pages
- Add page speed analysis
- Build a web interface

Author
Rohit Yadav