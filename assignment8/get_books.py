import json
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Task 3

options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)


url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)

results = []
results = []

book_cards = driver.find_elements(
    By.CSS_SELECTOR,
    "li"
)

for book in book_cards:
    title_elements = book.find_elements(
        By.CSS_SELECTOR,
        "span.title-content"
    )

    if len(title_elements) > 0:
        title = title_elements[0].text

        author_elements = book.find_elements(
            By.CSS_SELECTOR,
            "a.author-link"
        )

        authors = []
        for author in author_elements:
            authors.append(author.text)

        author_text = "; ".join(authors)

        format_elements = book.find_elements(
            By.CSS_SELECTOR,
            "span.display-info-primary"
        )

        format_year = ""
        if len(format_elements) > 0:
            format_year = format_elements[0].text

        results.append(
            {
                "Title": title,
                "Author": author_text,
                "Format-Year": format_year
            }
        )

books_df = pd.DataFrame(results)

print(books_df)

books_df.to_csv(
    "assignment8/get_books.csv",
    index=False
)

with open("assignment8/get_books.json", "w") as file:
    json.dump(results, file, indent=4)

driver.quit()