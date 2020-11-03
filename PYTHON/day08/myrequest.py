import requests
import bs4

#url = "http://192.168.43.123/JAVASCRIPT/list.html"
url = "http://localhost/JAVASCRIPT/myservlet"
response = requests.post(url)
response.encoding="utf-8"

print(response.text)