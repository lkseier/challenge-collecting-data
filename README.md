# Imo-Eliza-Scraping
Eliza-Scraping Project
Description
The Eliza-Scraping project is a Python-based web scraper designed to extract real estate listings data from the Immovan website (https://immovan.be/). This tool aims to fetch property details, including house URLs and related information, by leveraging HTTP requests and parsing the response content. The project supports handling both JSON and HTML responses, making it flexible for scraping dynamic web pages. It is intended for personal use or educational purposes to demonstrate web scraping techniques using libraries like requests, BeautifulSoup, and json.
Installation
To set up the Eliza-Scraping project on your local machine, follow these steps:
1.Clone the Repository:
git clone https://github.com/your-username/eliza-scraping.git
cd eliza-scraping
2.Install Dependencies: Ensure you have Python 3.6+ installed. Then, install the required libraries using pip:,
pip install requests beautifulsoup4
3.Verify Installation: Run the following command to check if the dependencies are correctly installed:,
python -c "import requests, bs4; print('Dependencies installed successfully!')"
4.Optional Configuration:
•  Update the url variable in test2.py with the desired Immovan page or adjust the number_pages variable as needed.
•  Ensure you have an active internet connection to fetch data.,
Usage
To run the scraper and extract data, follow these steps:
Execute the Script: Navigate to the project directory and run the main script:
python test2.py
Output:
•  The script will print the HTTP status code and, if successful, the parsed data (e.g., house URLs or listing details).
•  Check the console for errors or debug messages if the scraping fails.,
Customization:
•  Modify the url in the script to target different pages or property types.
•  Adjust the soup.find_all(class="matn_content") selector to match the HTML structure of the target page if it changes.,
Notes:
•  Respect the website’s robots.txt and terms of service to avoid legal issues.
•  The script includes basic error handling for JSON parsing and empty responses.,
Visuals
Currently, the project outputs data to the console. For a more visual representation, you can:
•  Export the scraped data (e.g., house URLs) to a CSV file and open it in a spreadsheet application like Excel or Google Sheets.
•  Integrate a plotting library (e.g., Matplotlib) to create charts of property counts or prices (future enhancement).
•  Example output might look like this in the console:
Request was successful.
Status code: 200, properties data: {'nhouse_urls': ['url1', 'url2']}
Timeline
•  June 2025: Initial concept and prototype development started.
•  June 19, 2025 (04:01 PM CEST): Basic scraping functionality implemented with requests and BeautifulSoup. Initial debugging of JSON parsing errors.
•  Future Goals: Add data storage (e.g., SQLite database), enhance error handling, and include visualization features.
Personal Situation
This project was developed as a personal learning exercise to explore web scraping and data extraction techniques. As a hobbyist programmer, I aimed to build a tool to automate the collection of real estate data for research purposes. The development took place during spare time, with challenges like handling dynamic web content and debugging JSON errors. The project reflects my growing interest in data science and web technologies.
How You Did It
The Eliza-Scraping project was built using the following approach:
Research: Identified the Immovan website as a target and studied its structure using browser developer tools.,
Library Selection: Chose requests for HTTP requests, BeautifulSoup for HTML parsing, and json for handling potential JSON responses.,
Coding Process:
•  Wrote the initial script (test2.py) to send GET requests to the Immovan URL.
•  Implemented basic status code checks and attempted JSON parsing.
•  Added BeautifulSoup to handle cases where the response might be HTML.,
Debugging: Encountered a JSONDecodeError due to invalid or empty responses, which was addressed by adding content checks and fallback HTML parsing.,
Testing: Ran the script locally to verify functionality and adjusted the code based on error outputs.,
Documentation: Created this README to document the process and guide future use or collaboration.,
The project is still in an early stage, with plans to refine the code, add robust error handling, and potentially share it with the community.