"""
Web Scraper for Books.toscrape.com
Purpose: Extract book prices and titles for competitor price monitoring
Target: E-commerce sellers, pricing strategists, business analysts

Features:
- Handles pagination (multiple pages)
- Manages missing fields (fallback to N/A)
- Graceful error handling for network issues
- Exports to structured CSV format
"""

import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def scrape():
    """
    Scrape book prices from books.toscrape.com
    
    Process:
    1. Iterate through 5 pages (pagination)
    2. Extract product name and price from each page
    3. Handle missing fields by using 'N/A' as fallback
    4. Handle errors gracefully without stopping scrape
    5. Export all data to CSV with proper headers
    """
    all_data = []

    # Decision: Scrape 5 pages
    # Reason: Covers ~100 products for reasonable dataset size
    for page in range(1, 6):
        url = BASE_URL.format(page)

        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            books = soup.find_all("article", class_="product_pod")

            for book in books:
                # Extract product name with fallback for missing h3
                name = book.h3.a["title"] if book.h3 else "N/A"

                # Extract price with None fallback
                price_tag = book.find("p", class_="price_color")
                price = price_tag.text if price_tag else None

                all_data.append({
                    "name": name,
                    "price": price
                })

        except Exception as e:
            # Log error but continue - don't stop entire scrape for one page failure
            print("Error:", e)

    # Export to CSV with UTF-8 encoding for special characters
    with open("data/raw_data.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price"])
        writer.writeheader()
        writer.writerows(all_data)

    print("Scraping Done")

if __name__ == "__main__":
    scrape()