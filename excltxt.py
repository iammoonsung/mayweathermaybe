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

with open('C:/Users/moonsung/Desktop/real/links.txt', 'w') as f:
    for dirpath, dirnames, filenames in dirs:
        for filename in filenames:
            if '.xlsx' in filename:
                filename = filename.replace('~$', '')
                excel = dirpath.replace('\\', '/') + '/' + filename
                f.write('%s\n' %excel)