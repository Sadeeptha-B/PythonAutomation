# XPath - xml path language
# Query language for selecting nodes from an xml document

# // - Pick matching node located at any level
# //tagName[1]: Indexed from 1, //tagName[@AttributeName="Value"]
# XPath functions - contains(), starts-with(): tagName[contains(@AttributeName,"Value")]
# tagName[() and/or ()]
# //article/div:- / to select the children from the node set on the left side of this character
# //h1/text(), //article//text
# //h1/.., ./*, @- Select attribute

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from decouple import config
import pandas as pd
from datetime import datetime
import os,sys

application_path = os.path.dirname(sys.executable)  # Executable path

month_day_year = datetime.now().strftime("%d%m%Y") 
website = 'https://www.thesun.co.uk/sport/football/'
driver_path = config('driver_path', default='')

## Setting up webdriver
# ==========================================================================================
options = Options()
options.headless = True   # headless mode
service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

# Scrape website
# Get first occurence - driver.find_element
# Can use id, path, xpath for searching method
containers = driver.find_elements(by='xpath', value="//div[@class='teaser__copy-container']")
titles, subtitles, links = [], [], []

for container in containers:
    title = container.find_element(by='xpath', value="./a/h2").text
    subtitle = container.find_element(by='xpath', value="./a/p").text
    link = container.find_element(by='xpath', value="./a").get_attribute("href")

    titles.append(title)
    subtitles.append(subtitle)
    links.append(link)

## Write to csv
news_items = {'titles':titles, 'subtitles':subtitles, 'links': links}
df_headlines = pd.DataFrame(news_items)   

# Specify path
file_name = f'headline-{month_day_year}.csv' 
csv_path = os.path.join(application_path,file_name) 

df_headlines.to_csv(csv_path)
driver.quit()

# Creating executable: pyinstaller library
# Command: pyinstaller --onefile web_scraping.py 
# Pyinstaller requires Python310/Scripts to be added to path
