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
from openpyxl import Workbook
from openpyxl import load_workbook
import time
import os
import numpy as np

dirs = os.walk('C:/Users/moonsung/Desktop/real/category/')

def find_categoryid(categorydb, cat):
    if len(cat) == 3:
        id = categorydb.loc[(categorydb['cat1'] == cat[0]) & (categorydb['cat2'] == cat[1]) & (categorydb['cat3'] == cat[2]), 'id']
    if len(cat) == 4:
        id = categorydb.loc[(categorydb['cat1'] == cat[0]) & (categorydb['cat2'] == cat[1]) & (categorydb['cat3'] == cat[2]) & (categorydb['cat4'] == cat[3]), 'id']
    if len(cat) == 5:
        id = categorydb.loc[(categorydb['cat1'] == cat[0]) & (categorydb['cat2'] == cat[1]) & (categorydb['cat3'] == cat[2]) & (categorydb['cat4'] == cat[3]) & (categorydb['cat5'] == cat[4]), 'id']
    if len(cat) == 6:
        id = categorydb.loc[(categorydb['cat1'] == cat[0]) & (categorydb['cat2'] == cat[1]) & (categorydb['cat3'] == cat[2]) & (categorydb['cat4'] == cat[3]) & (categorydb['cat5'] == cat[4]) & (categorydb['cat6'] == cat[5]), 'id']
    return id

f =  open('C:/Users/moonsung/Desktop/real/links.txt', 'r')
fs = f.readlines()
for excel in fs:
    excel=excel.replace('\n', '')
    print(excel)
    break
    df = read_excel(excel, sheet_name='sheet')
    if df.empty:
        continue
    df2 = []
    
    wb = load_workbook(filename = excel, read_only=False, data_only=False)
    sheet = wb.active
    count = len(sheet['G'])
    for i in range(1, count+1):
        url = sheet['G' + str(i)].value
        req = requests.get(url)
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        image = soup.select('#container > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > ul > li:nth-child(1) > a > img')
        imglinks = image[0].get('src')
        sheet['G' + str(i)].value = imglinks
        cell = sheet['G' + str(i)]
        time.sleep(np.random.uniform(1, 3))

    wb.save(excel)