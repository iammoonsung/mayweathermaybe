import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time
import os
import math
import numpy as np

url_file = open('C:/Users/moonsung/Desktop/real/gmarket_crawling_data/after_underwear_urls_selected.txt','r')
urls = url_file.readlines()
urls = urls[1589:]

seen = set()

urls = [url for url in urls if not (url in seen or seen.add(url))]

cnt = 0
write_wb = [None] * len(urls)
write_ws = [None] * len(urls)

for strurl in urls:
    url = strurl.split(', ')
    url[2] = url[2].replace('\n', '')
    req = requests.get(url[0])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    cate1 = url[1]
    cate2 = url[2]
    cate3 = soup.select('#region__content-status-information > div > div > div.box__information-area > div > ul > li:nth-child(4) > span.text.text--active')
    numprod = soup.select('#region__content-status-information > div > div > div.box__information-area > div > ul > li:nth-child(4) > span.text.text--count')
        
    data = []

    if len(numprod) == 0:
        continue

    num = int(numprod[0].text.replace('(', '').replace(')', '').replace(',', ''))

    if num < 500:
        pages = math.ceil(num/100)
    else:
        pages = 5

    for page in range(pages):
        req = requests.get(url[0] + '&k=0&p=' + str(page+1))
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        titles = soup.find_all('span', class_ = "text__item")
        prices = soup.find_all('strong', class_ = "text text__value")
        links = soup.find_all('a', class_ = "link__item")
        for item in range(len(titles)):
            brand = soup.select('#section__inner-content-body-container > div:nth-child(3) > div:nth-child(' + str(item+1) + ') > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title > span > a > span.text__brand')
            eval = soup.select('#section__inner-content-body-container > div:nth-child(3) > div:nth-child(' + str(item+1) + ') > div.box__item-container > div.box__information > div.box__information-score > ul > li.list-item.list-item__feedback-count > span.text')
            buy = soup.select('#section__inner-content-body-container > div:nth-child(3) > div:nth-child(' + str(item+1) + ') > div.box__item-container > div.box__information > div.box__information-score > ul > li.list-item.list-item__pay-count > span.text')
            link = soup.select('#section__inner-content-body-container > div:nth-child(3) > div:nth-child(' + str(item+1) + ') > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title > span > a')
            
            info = []

            info.append(cate3[0].text)

            if len(brand):
                info.append(brand[0].text)
            else:
                info.append("")

            info.append(titles[item].text)
            info.append(prices[item].text)

            if len(eval):
                info.append(eval[0].text)
            else:
                info.append("")

            if len(buy):
                info.append(buy[0].text)
            else:
                info.append("")
            
            info.append(links[item*2].get('href'))
            
            data.append(info)

        time.sleep(np.random.uniform(1, 3))

    write_wb[cnt] = Workbook()
    write_ws[cnt] = write_wb[cnt].active

    for info in data:
        write_ws[cnt].append(info)
    
    os.makedirs('C:/Users/my/Desktop/Mayweather/gmarket_crawling_data/' + cate1.replace('/','_') + '/' + cate2.replace('/','_'), exist_ok=True)
    write_wb[cnt].save('C:/Users/my/Desktop/Mayweather/gmarket_crawling_data/' + cate1.replace('/','_') + '/' + cate2.replace('/','_') + '/' + cate3[0].text.replace('/','_') + '.xlsx')
    cnt += 1
    

'''
category = soup.find('span', class_ = "text text--active")
images = soup.find_all('img', class_ = "image__item")
brands = soup.find_all('span', class_ = "text__brand")
titles = soup.find_all('span', class_ = "text__item")
prices = soup.find_all('span', class_ = "text text__value")
rank = soup.find_all('span', class_ = "text")

print(len(images), len(brands), len(titles), len(prices), len(rank),category.text)

data = []

write_wb = Workbook()
write_ws = write_wb.active

'''

'''
for page in range(1):
    for item in range(100):
        req = requests.get(prod[item].get('href') + '&k=0&p=' + str(page+3))
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        category = soup.select('body > div.location-navi > ul > li.on > a')
        image = soup.findAll('img')
        name = soup.select('#itemcase_basic > h1')
        price = soup.select('#itemcase_basic > p > span > strong')
        write_ws.append([category[0].text, image[1]['src'], name[0].text, price[0].text])
'''