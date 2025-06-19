import requests
from bs4 import BeautifulSoup
import json
import time
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

session = requests.Session()
retry_strategy = Retry(
    total=5,
    backoff_factor=1,
    status_forcelist=[403, 500, 502, 503, 504])

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount("https://", adapter)
session.mount("http://", adapter)

properties = [] # List to store property data
for number_pages in range(1, 10):
    url = "https://immovlan.be/fr/detail/maison/a-vendre?page={number_pages}"
    # Set the headers to mimic a browser request
    headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/58.0.3029.110 Safari/537.3"}
    response = session.get(url, headers=headers)
    # Format the URL with the current number of pages
    current_url = url.format(number_pages=number_pages)
    # Make the request to the current URL
    response = requests.get(current_url)
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve page {number_pages}: {response.status_code}")
        continue
    if soup.title:
        print(f"Scraping page {number_pages}: {soup.title.string}")
    else:
        print(f"Failed to find title for page {number_pages}")
        continue
    soup = BeautifulSoup(response.content, 'html.parser')
    for listing in soup.find_all(class_="main_content"):
        title = listing.select_one("detail__header_title_main").text.strip() if listing.select_one(".detail__header_title_main") else "No title"
        price = listing.select_one("detail__header_price_data").text.strip() if listing.select_one(".detail__header_price_data") else "No price"
        address = listing.select_one("detail__header_address").text.strip() if listing.select_one(".detail__header_address") else "No address"

     #Add property to list
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


