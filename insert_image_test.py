import os
import pandas
from pandas import read_excel
from config import Config
from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import pymysql

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

##############################################################
################### 스키마에 맞게 수정하기 ####################
##############################################################

class category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat1 = db.Column(db.String)
    cat2 = db.Column(db.String)
    cat3 = db.Column(db.String)
    cat4 = db.Column(db.String)
    cat5 = db.Column(db.String)
    cat6 = db.Column(db.String)

    def __repr__(self):
        return '<Category {}, {}, {}, {}, {}, {}, {}>'.format(self.id, self.cat1, self.cat2, self.cat3, self.cat4, self.cat5, self.cat6)

class product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    price = db.Column(db.Integer)
    image = db.Column(db.String)
    product_cat = db.Column(db.Integer)

dirs = os.walk('/home/ubuntu/real/mayweathermaybe/category/')


##############################################################
################## 크롤링 데이터를 DB에 삽입 ##################
##############################################################

pymysql.install_as_MySQLdb()
import MySQLdb

engine = create_engine("mysql+mysqldb://root:"+"testtest"+"@13.125.205.2/mayweather", encoding='utf-8')
conn = engine.connect()

categorydb = pandas.read_sql_table('category', conn)

## 카테고리 DB에서 ID 가져오기
#def find_categoryid(categorydb, cat):
#    if len(cat) == 3:
#        id = categorydb.loc[(categorydb['cat1'] == cat[0]) & (categorydb['cat2'] == cat[1]) & (categorydb['cat3'] == cat[2]), 'id']
#    if len(cat) == 4:
#        id = categorydb.loc[(categorydb['cat1'] == cat[0]) & (categorydb['cat2'] == cat[1]) & (categorydb['cat3'] == cat[2]) & (categorydb['cat4'] == cat[3]), 'id']
#    if len(cat) == 5:
#        id = categorydb.loc[(categorydb['cat1'] == cat[0]) & (categorydb['cat2'] == cat[1]) & (categorydb['cat3'] == cat[2]) & (categorydb['cat4'] == cat[3]) & (categorydb['cat5'] == cat[4]), 'id']
#    if len(cat) == 6:
#        id = categorydb.loc[(categorydb['cat1'] == cat[0]) & (categorydb['cat2'] == cat[1]) & (categorydb['cat3'] == cat[2]) & (categorydb['cat4'] == cat[3]) & (categorydb['cat5'] == cat[4]) & (categorydb['cat6'] == cat[5]), 'id']
#    return id


excel = '/home/ubuntu/real/mayweathermaybe/category/자기만족/Style/뷰티/화장품/팩_마스크/팩_마스크용품.xlsx'
sheet = 'Sheet'
df = read_excel(excel, sheet_name=sheet)
df.columns = ['category', 'brand', 'productname', 'price', 'comment', 'buy', 'link']
#category_file = excel.replace('/home/ubuntu/real/mayweathermaybe/category/', '')
#cat = category_file.split('/')
df['category'].values[:] = 4
#find_categoryid(categorydb, cat)
df['comment'] = df['comment'].fillna('0')
df['buy'] = df['buy'].fillna('0')
df['link'] = df['link'].fillna('0')
df['price'] = df['price'].apply(lambda x: int(str(x).replace(',','')))
df['comment'] = df['comment'].apply(lambda x: int(str(x).replace('상품평 ','').replace(',', '')))
df['buy'] = df['buy'].apply(lambda x: int(str(x).replace('구매 ','').replace(',', '')))
dbdf=df[['productname','price','link','category']]
dbdf.rename(columns = {'productname' : 'name'}, inplace = True)
dbdf.rename(columns = {'category' : 'product_cat'}, inplace = True)
dbdf.rename(columns = {'link' : 'image'}, inplace = True)
dbdf.to_sql(name='product', con=engine, if_exists='append', index=False)
