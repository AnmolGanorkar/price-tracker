import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "http://books.toscrape.com/catalogue/page-{}.html"

def scrape():
    all_data = []

    for page in range(1, 6):  # pagination
        url = BASE_URL.format(page)

        try:
            res = requests.get(url)
            soup = BeautifulSoup(res.text, "html.parser")

            books = soup.find_all("article", class_="product_pod")

            for book in books:
                name = book.h3.a["title"] if book.h3 else "N/A"

                price_tag = book.find("p", class_="price_color")
                price = price_tag.text if price_tag else None

                all_data.append({
                    "name": name,
                    "price": price
                })

        except Exception as e:
            print("Error:", e)

    # save raw data
    with open("data/raw_data.csv", "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=["name", "price"])
        writer.writeheader()
        writer.writerows(all_data)

    print("Scraping Done")

if __name__ == "__main__":
    scrape()