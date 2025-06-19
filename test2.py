import requests
import json
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Define the URL for the real estate listings
number_pages = 1  # Adjust this as needed
url = "https://immovlan.be/en/real-estate?transactiontypes=for-sale,in-public-sale&propertytypes=house&noindex={number_pages}"
req = requests.get(url)
if req.status_code == 200:
    print("Request was successful.")
    if req.text:
        try:
            properties = req.json()
            print(f"Status code: {req.status_code}\nProperties data: {properties}")
            house_urls = properties.get('house_urls', {})
        except json.JSONDecodeError:
            print("Response is not in JSON format.")
            properties = {}
            house_urls = {}
    else:
        print("Response text is empty.")
        properties = {}
        house_urls = {}
else:
    print(f"Request failed with status code: {req.status_code}")
    properties = {}
    house_urls = {}
 
# Note: The above code assumes that the response from the URL is in JSON format.
cookies_url = "https://immovlan.be/cookies"
req = requests.get(cookies_url)
cookies = req.cookies

soup = BeautifulSoup(req.content, 'html.parser')
for property in properties:
    for listing in soup.find_all(class_="main_content"):
        title = listing.select_one("detail__header_title_main").text.strip() if listing.select_one(".detail__header_title_main") else "No title"
        price = listing.select_one("detail__header_price_data").text.strip() if listing.select_one(".detail__header_price_data") else "No price"
        address = listing.select_one("detail__header_address").text.strip() if listing.select_one(".detail__header_address") else "No address"

        # Add property to list
        properties.append({
            "title": title,
            "price": price,
            "address": address
        })
# Save to JSON
with open("real_estate_data.json", "w", encoding="utf-8") as f:
    json.dump(properties, f, indent=4, ensure_ascii=False)
# Print the number of properties found
print(f"Found {len(properties)} properties.")