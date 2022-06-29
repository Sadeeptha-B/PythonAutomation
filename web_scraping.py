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
from selenium.webdriver.chrome.service import Service
from decouple import config

website = 'https://www.thesun.co.uk/sport/football/'
path = config('driver_path', default='')

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
driver.get(website)

