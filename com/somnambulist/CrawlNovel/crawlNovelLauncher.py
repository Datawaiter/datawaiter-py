
# coding=utf-8
import requests
import parsel


url = 'http://www.biqu5200.net/0_7/'

response = requests.get(url)
response.encoding = response.apparent_encoding
data = response.text
##print(data)
selector = parsel.Selector(data)
#获取小说名称
novle_name = selector.css('#info h1::text').get()
print(novle_name)
#获取章节名称
# chapters = selector.css('.section-list.fix li a').getall()
# for chapter in chapters :
#     chapter_selector = parsel.Selector(chapter)
#     #章节名称
#     chapter_name = chapter_selector.xpath('.//text()').get()
#     href = chapter_selector.xpath('.//@href').get()
#     #章节url
#     chapter_href = url+href
#     print(chapter_href)
#     print(requests.get(chapter_href))
#     break