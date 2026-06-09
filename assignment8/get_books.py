import json
import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# Task 3
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install())
)

url = "https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart"
driver.get(url)

results = []

book_entries = driver.find_elements(
    By.CSS_SELECTOR,
    "li.cp-search-result-item-info"
)

print(len(book_entries))

for book in book_entries:
    title = book.find_element(
        By.CSS_SELECTOR,
        "span.title-content"
    ).text

    print(title)

driver.quit()
