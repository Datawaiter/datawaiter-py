
# coding=utf-8
import requests
import parsel

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'}

url = 'https://www.777zw.net/book/23/cef92b4ead/1.html'
print(requests.get(url))