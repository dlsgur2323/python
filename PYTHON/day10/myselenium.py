import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import json

options = Options()
options.headless = True
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://finance.daum.net/quotes/A005930")

tag_names = browser.find_element_by_css_selector("#boxSummary > div > span:nth-child(1) > span.currentB > span.numB.up > strong")

print(tag_names.text)
