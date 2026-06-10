import pandas as pd

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
options.add_argument("--disable-gpu")
options.add_argument("--window-size=1920,1080")

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=options
)

url = "https://owasp.org/Top10/2025/"
driver.get(url)

top_ten = []

links = driver.find_elements(
    By.XPATH,
    "//a[contains(@href, 'A0')]"
)

for link in links:
    title = link.text.strip()
    href = link.get_attribute("href")

    if title and href:
        top_ten.append(
            {
                "Title": title,
                "Link": href
            }
        )

top_ten = top_ten[:10]

print(top_ten)

owasp_df = pd.DataFrame(top_ten)

owasp_df.to_csv(
    "assignment8/owasp_top_10.csv",
    index=False
)

driver.quit()
