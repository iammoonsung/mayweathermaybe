import requests
from tqdm import tqdm
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time
import os
import numpy as np

base = 'http://browse.gmarket.co.kr'

data = []

cate_urls = [

#brand clothes
'http://category.gmarket.co.kr/listview/L100000103.aspx',      #female
'http://category.gmarket.co.kr/listview/L100000104.aspx',      #male
'http://category.gmarket.co.kr/listview/L100000105.aspx',      #casual

#brand clothing goods
'http://category.gmarket.co.kr/listview/L100000106.aspx',      #shoes/bag
'http://category.gmarket.co.kr/listview/L100000107.aspx',      #jewerly/watch
'http://category.gmarket.co.kr/listview/L100000096.aspx',      #luxury

#sports brand
'http://category.gmarket.co.kr/listview/L100000099.aspx',      #outdoor
'http://category.gmarket.co.kr/listview/L100000043.aspx',      #sports

#fashion 
'http://category.gmarket.co.kr/listview/L100000003.aspx',      #female
'http://category.gmarket.co.kr/listview/L100000046.aspx',      #male
'http://category.gmarket.co.kr/listview/L100000070.aspx',      #underwear
'http://category.gmarket.co.kr/listview/L100000035.aspx',      #kids cloth

#clothing goods
'http://category.gmarket.co.kr/listview/L100000049.aspx',      #shoes
'http://category.gmarket.co.kr/listview/L100000064.aspx',      #bag
'http://category.gmarket.co.kr/listview/L100000095.aspx',      #kids shoes/bag
'http://category.gmarket.co.kr/listview/L100000027.aspx',      #jewerly/watch
'http://category.gmarket.co.kr/listview/L100000096.aspx',      #luxury

#beauty
'http://category.gmarket.co.kr/listview/L100000005.aspx',      #cosmetics/perfumes
'http://category.gmarket.co.kr/listview/L100000071.aspx',      #body/hair

#kids
'http://category.gmarket.co.kr/listview/L100000006.aspx',      #birth/infant care
'http://category.gmarket.co.kr/listview/L100000042.aspx',      #toy
'http://category.gmarket.co.kr/listview/L100000035.aspx',      #kids cloth
'http://category.gmarket.co.kr/listview/L100000095.aspx',      #kids shoes/bag

#food
'http://category.gmarket.co.kr/listview/L100000020.aspx',      #fresh food
'http://category.gmarket.co.kr/listview/L100000036.aspx',      #processed food
'http://category.gmarket.co.kr/listview/L100000068.aspx',      #health food
'http://category.gmarket.co.kr/listview/L100000094.aspx',      #coffee/drink

#necessaries
'http://category.gmarket.co.kr/listview/L100000074.aspx',      #necessaries
'http://category.gmarket.co.kr/listview/L100000071.aspx',      #body/hair

#home deco
'http://category.gmarket.co.kr/listview/L100000031.aspx',      #furniture/DIY
'http://category.gmarket.co.kr/listview/L100000039.aspx',      #bedding
'http://category.gmarket.co.kr/listview/L100000093.aspx',      #light, interior design
'http://category.gmarket.co.kr/listview/L100000014.aspx',      #daily necessaries
'http://category.gmarket.co.kr/listview/L100000085.aspx',      #kitchen supplies
'http://category.gmarket.co.kr/listview/L100000041.aspx',      #flower, event goods

#stationery
'http://category.gmarket.co.kr/listview/L100000045.aspx',      #stationery
#<<<< http://browse.gmarket.co.kr/list?category=200000981 >>>> office machine

#hobby/companion
'http://category.gmarket.co.kr/listview/L100000091.aspx',      #instrument/hobby
'http://category.gmarket.co.kr/listview/L100000038.aspx',      #companion animal goods,

#computer
'http://category.gmarket.co.kr/listview/L100000002.aspx',      #laptop, PC
'http://category.gmarket.co.kr/listview/L100000082.aspx',      #monitor, printer
'http://category.gmarket.co.kr/listview/L100000055.aspx',      #peripheral
'http://category.gmarket.co.kr/listview/L100000075.aspx',      #storage

#digital
'http://category.gmarket.co.kr/listview/L100000056.aspx',      #mobile, tablet
'http://category.gmarket.co.kr/listview/L100000033.aspx',      #camera
'http://category.gmarket.co.kr/listview/L100000111.aspx',      #game
'http://category.gmarket.co.kr/listview/L100000102.aspx',      #audio

#home appliances
'http://category.gmarket.co.kr/listview/L100000032.aspx',      #video
'http://category.gmarket.co.kr/listview/L100000008.aspx',      #kitchen
'http://category.gmarket.co.kr/listview/L100000077.aspx',      #season
'http://category.gmarket.co.kr/listview/L100000092.aspx',      #life, beauty
'http://category.gmarket.co.kr/listview/L100000102.aspx',      #audio
'http://category.gmarket.co.kr/listview/L100000083.aspx',      #health, medical

#sports
'http://category.gmarket.co.kr/listview/L100000043.aspx',      #sports wear/running shoes
'http://category.gmarket.co.kr/listview/L100000037.aspx',      #fitness, swim
'http://category.gmarket.co.kr/listview/L100000098.aspx',      #racket
'http://category.gmarket.co.kr/listview/L100000058.aspx',      #golf
'http://category.gmarket.co.kr/listview/L100000097.aspx',      #bicycle, board, leisure
'http://category.gmarket.co.kr/listview/L100000017.aspx',      #camping, fishing
'http://category.gmarket.co.kr/listview/L100000099.aspx',      #hiking, outdoor

#health
'http://category.gmarket.co.kr/listview/L100000083.aspx',      #health, medical
'http://category.gmarket.co.kr/listview/L100000068.aspx',      #health food

#rental
'http://category.gmarket.co.kr/listview/L100000112.aspx',      #rental service

#car
'http://category.gmarket.co.kr/listview/L100000030.aspx',      #car

#tool
'http://category.gmarket.co.kr/listview/L100000076.aspx',      #tool

#book
'http://category.gmarket.co.kr/listview/L100000028.aspx',      #book, record, e-learning

#coupon
'http://category.gmarket.co.kr/listview/L100000048.aspx',      #e-coupon
'http://category.gmarket.co.kr/listview/L100000084.aspx'       #gift card
]

cate1s = []
urls = []

for url in tqdm(cate_urls, desc='mid url', mininterval=1):
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    categories = soup.select('#gnb > ul > li > a:nth-child(1)')
    present = soup.select('#divCategoryLogo > img')
    cate1s.append(present[0].get('alt'))
    for category in categories:
        urls.append([category.get('href').split("'")[3], present[0].get('alt')])

    time.sleep(np.random.uniform(1, 3))

with open('C:/Users/my/Desktop/Mayweather/gmarket_img_crawling_data/mid_urls.txt', 'w') as f:
    for category in urls:
        f.write('%s, %s\n' %(category[0], category[1]))

cate2s = []
cate = []

for url in tqdm(urls, desc='small category', mininterval=3):
    req = requests.get(url[0])
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    present = soup.select('#region__content-status-information > div > div > div.box__information-area > div > ul > li:nth-child(3) > span.text.text--active')

    if len(present) == 0:
        print(url)
        continue

    categories = soup.select('#region__content-filter > div > div:nth-child(1) > div > div.box__filter-body > div > ul > li > ul > li > a > span')
    next_urls = soup.select('#region__content-filter > div > div:nth-child(1) > div > div.box__filter-body > div > ul > li > ul > li > a')
    
    cate2s.append(present[0].text)
    for c in range(len(categories)): 
        cate.append([base+next_urls[c].get('href'), url[1], present[0].text, categories[c].text])

    time.sleep(np.random.uniform(1, 3))

seen = set()
cate = [url for url in cate if not (url[0] in seen or seen.add(url[0]))]

with open('C:/Users/my/Desktop/Mayweather/gmarket_img_crawling_data/urls.txt', 'w') as f:
    for category in cate:
        f.write('%s, %s, %s, %s\n' %(category[0], category[1], category[2], category[3]))
