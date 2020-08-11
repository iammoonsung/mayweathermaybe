import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
import time
import os
import numpy as np

req = requests.get('http://item.gmarket.co.kr/Item?goodscode=1794089558')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
image = soup.select('#container > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ul > li:nth-child(1) > a > img')
imglinks = image[0].get('src')
print(imglinks)