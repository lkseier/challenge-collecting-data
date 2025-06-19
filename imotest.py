import requests
import pandas as pd
from parsel import Selector
from seleniumbase import Driver
import json
import time
from bs4 import BeautifulSoup
#define url
base_url = "https://immovlan.be/fr/detail/maison/a-vendre"
#initilize undetected selenium driver, headless mode
driver = Driver(uc=True, headless=True)
houses_urls = []

#loop through pages
for page in range(1, 10):  # Adjust range as needed
    url = f"{base_url}={page}"
    print(f"Scraping page {page}: {url}")
    
    # Open the URL with Selenium
    driver.get(url)
    sel = Selector(text=driver.page_source)
    # find all house links using xpath
    xpath_houses = "//div[@class= 'will-change-transform']/a/@href"
    page_houses_urls = sel.xpath(xpath_houses).getall()

    if page_houses_urls:
        houses_urls.extend(page_houses_urls)
    else:
        print(f"No houses found on page {page}.")
        for listing in sel.css(".main_content"):
            # Extract title, price, and address using CSS selectors
            title = listing.select_one("detail__header_title_main").text.strip() if listing.select_one(".detail__header_title_main") else "No title"
            price = listing.select_one("detail__header_price_data").text.strip() if listing.select_one(".detail__header_price_data") else "No price"
            address = listing.select_one("detail__header_address").text.strip() if listing.select_one(".detail__header_address") else "No address"

     #Add property to list
            properties = []
            properties.append({
            "title": title,
            "price": price,
            "address": address})
    #Add a delay to avoid overwhelming the server
            time.sleep(2)

#save to json
with open("real_estate_data.json", "w", encoding="utf-8") as f:
    json.dump(properties, f, indent=4, ensure_ascii=False)
# Print the number of properties found
print(f"Found {len(properties)} properties.")
# Print the first property to verify the data
if properties:
    print("First property:", properties[0])
