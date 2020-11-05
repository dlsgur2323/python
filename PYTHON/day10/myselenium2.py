import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
import json

options = Options()
options.headless = False
browser = webdriver.Chrome(executable_path="./chromedriver.exe", options=options)
browser.get("https://www.youtube.com/?gl=KR")

time.sleep(5)
login_btn = browser.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a')
login_url = login_btn.get_attribute("href")
browser.get(login_url)

email = browser.find_element_by_xpath('//*[@id="identifierId"]')
email.send_keys("dlsgur2323@gmail.com")

next_btn = browser.find_element_by_xpath('//*[@id="identifierNext"]/div/button')
next_btn.click()
