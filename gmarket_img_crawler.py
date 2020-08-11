from selenium import webdriver
from selenium.webdriver import ActionChains
from openpyxl import Workbook
from tqdm import tqdm
import numpy as np
import time
import math
import os

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome('C:/Users/my/Desktop/Mayweather/chromedriver_win32/chromedriver', chrome_options=options)
action = webdriver.ActionChains(driver)

url_file = open('C:/Users/my/Desktop/Mayweather/gmarket_crawling_data/after_underwear_urls_selected.txt','r')
urls = url_file.readlines()

seen = set()
urls = [url for url in urls if not (url in seen or seen.add(url))]

cnt = 0
write_wb = [None] * len(urls)
write_ws = [None] * len(urls)

for strurl in urls:
    url = strurl.split(', ')
    url[2] = url[2].replace('\n', '')
    cate1 = url[1]
    cate2 = url[2]
    driver.get(url[0])
    cate3 = driver.find_element_by_css_selector('#region__content-status-information > div > div > div.box__information-area > div > ul > li:nth-child(4) > span.text.text--active')
    numprod = driver.find_element_by_css_selector('#region__content-status-information > div > div > div.box__information-area > div > ul > li:nth-child(4) > span.text.text--count')

    if not numprod:
        continue

    cate3 = cate3.text.replace(' ', '')
    numprod = numprod.text
    num = int(numprod.replace('(', '').replace(')', '').replace(',', ''))

    if num < 200:
        pages = math.ceil(num/100)
    else:
        pages = 2
    
    data = [['category', 'brand', 'productname', 'price', 'comment', 'buy', 'img']]

    for page in range(pages):
        driver.get(url[0] + '&k=0&p=' + str(page+1))
        if page == 0:
            titles = driver.find_elements_by_css_selector('#section__inner-content-body-container > div:nth-child(3) > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title > span > a')
            prices = driver.find_elements_by_css_selector('#section__inner-content-body-container > div:nth-child(3) > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-price > div > strong')
            img = driver.find_elements_by_css_selector('#section__inner-content-body-container > div:nth-child(3) > div > div.box__item-container > div.box__image > a > img')
        else:
            titles = driver.find_elements_by_css_selector('#section__inner-content-body-container > div:nth-child(2) > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-title > span > a')
            prices = driver.find_elements_by_css_selector('#section__inner-content-body-container > div:nth-child(2) > div > div.box__item-container > div.box__information > div.box__information-major > div.box__item-price > div > strong')
            img = driver.find_elements_by_css_selector('#section__inner-content-body-container > div:nth-child(2) > div > div.box__item-container > div.box__image > a > img')
                    
        for item in tqdm(range(len(titles)), desc=cate3 + str(page+1), mininterval=0.3):

            action = ActionChains(driver)
            action.move_to_element(titles[item]).perform()            
            title = titles[item].find_elements_by_css_selector("*")
            
            if len(title) == 4:
                brand = title[1].text
                productname = title[3].text
            else:
                brand = ""
                productname = title[1].text
            if page == 0:
                score_parent = driver.find_element_by_css_selector('#section__inner-content-body-container > div:nth-child(3) > div:nth-child(' + str(item+1) + ') > div.box__item-container > div.box__information > div.box__information-score > ul')
            else:
                score_parent = driver.find_element_by_css_selector('#section__inner-content-body-container > div:nth-child(2) > div:nth-child(' + str(item+1) + ') > div.box__item-container > div.box__information > div.box__information-score > ul')
            
            scores = score_parent.find_elements_by_css_selector("*")

            comment = "0"
            buy = "0"

            if scores:
                scores = [sc.text.replace('\n건', '') for sc in scores]
                for score in scores:
                    if '상품평' in score:
                        comment = score.replace('상품평 ', '')
                    if '구매' in score:
                        buy = score.replace('구매 ' ,'')
            
            info = [cate3, brand, productname, prices[item].text.replace(',', ''), comment, buy, img[item].get_attribute('src')]

            data.append(info)

    write_wb[cnt] = Workbook()
    write_ws[cnt] = write_wb[cnt].active

    for info in data:
        write_ws[cnt].append(info)
    
    os.makedirs('C:/Users/my/Desktop/Mayweather/gmarket_img_crawling_data/' + cate1.replace('/','_') + '/' + cate2.replace('/','_'), exist_ok=True)
    write_wb[cnt].save('C:/Users/my/Desktop/Mayweather/gmarket_img_crawling_data/' + cate1.replace('/','_') + '/' + cate2.replace('/','_') + '/' + cate3.replace('/','_') + '.xlsx')
    cnt += 1
    if cnt == 10:
        break