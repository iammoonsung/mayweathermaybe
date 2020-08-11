import os
import pandas
from pandas import read_excel
from config import Config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pymysql
import requests
from bs4 import BeautifulSoup
from openpyxl import load_workbook
from openpyxl import Workbook
import time
import numpy as np

excel = 'C:/Users/moonsung/Desktop/real/category/실용/렌탈/렌탈/공기청정기 렌탈/청호나이사.xlsx'
df2 = []
wb = load_workbook(filename = excel, read_only=False, data_only=False)
sheet = wb.active
count = len(sheet['G'])
print(count)
for i in range(1, count+1):
    url = sheet['G' + str(i)].value
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    image = soup.select('#container > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ul > li:nth-child(1) > a > img')
    imglinks = image[0].get('src')
    sheet['G' + str(i)].value = imglinks
    cell = sheet['G' + str(i)]

wb.save(excel)
