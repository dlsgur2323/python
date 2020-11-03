import requests
import bs4

#url = "http://192.168.43.123/JAVASCRIPT/list.html"
#url = "http://localhost/JAVASCRIPT/myservlet?p=hello_get"
#url = "http://localhost/JAVASCRIPT/myservlet?"
url = "https://finance.naver.com/item/main.nhn?code=055550"

#paramdict = {
#    "p" : "hello_post"
#    }
#response = requests.post(url, params=paramdict)
response = requests.post(url)
response.encoding="EUC-KR"

print(response.text)