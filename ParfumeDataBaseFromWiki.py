import requests
from bs4 import BeautifulSoup
from lxml import html
import numpy as np
import csv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
"""
def scrape_website(url, xpath_expression):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page
            soup = BeautifulSoup(response.text, "html.parser")

            # Use lxml's html module to create an XPath element
            root = html.fromstring(response.text)

            # Use the XPath expression to extract data
            extracted_data = root.xpath(xpath_expression)

            extracted_text = [elem.text_content() for elem in extracted_data]

            return extracted_text
        else:
            print(f"Failed to retrieve the webpage at {url}. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
"""

driver = webdriver.Chrome()

# Function to scrape a website using Selenium
def scrape_website_selenium(url, xpath_expression):
    global driver
    try:
        # Create a new instance of the Chrome web driver (you need to have Chrome installed)
        driver = webdriver.Chrome()

        # Open the URL in the web driver
        driver.get(url)

        # Find the element using XPath
        element = driver.find_element(By.XPATH,xpath_expression)

        # Extract the text content of the element
        extracted_data = element.text

        time.sleep(15)

        return extracted_data
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return None
    finally:
        # Close the web driver to release resources
        driver.quit()

liste = np.arange(1,32,2)
number_of_scents = [54,84,19,56,9,179,113,42,72,13,7,99,30,18,5,19]
listem = []
for i in range(0,16):
    listem.append(np.arange(number_of_scents[i]))

# Define a list of URLs and corresponding XPath expressions
urls_and_xpaths = []
csv_file_path_read = "xpath_fragrance.csv"

# Open the CSV file in read mode
with open(csv_file_path_read, mode='r', newline='') as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Iterate through the CSV file line by line and append each line to the list
    for row in csv_reader:
        if row:  # Check if the row is not empty
            urls_and_xpaths.append(row[0])  # Assuming there's only one column in the CSV

"""
csv_file_path_write = "scent.csv"

# Open the CSV file in write mode
with open(csv_file_path_write, mode='w', newline='') as csv_file:
    # Create a CSV writer object
    csv_writer = csv.writer(csv_file)

    # Iterate through the list and scrape data from each URL using the specified XPath expression
    for item in urls_and_xpaths:
        url = "https://www.wikiparfum.com/en/ingredients"
        xpath_expression = item
        print(xpath_expression)
        extracted_data = scrape_website_selenium(url, xpath_expression)
        print(extracted_data)
        csv_writer.writerow([extracted_data])
        if extracted_data:
            # Write each extracted data as a new row in the CSV file
            for data in extracted_data:
                csv_writer.writerow([data])
"""
"""
citrus = 54
green = 84
watery = 19
aromatic_fougere = 56
aldehydic = 9
floral = 179
fruity = 113
spicy = 42
woody = 72
chypre = 13
tobacco = 7
gourmand = 99
ambery = 30
leather = 18
musk_skin = 5
conceptual = 19
"""
