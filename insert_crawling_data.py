import os
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

class category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cat1 = db.Column(db.String)
    cat2 = db.Column(db.String)
    cat3 = db.Column(db.String)
    cat4 = db.Column(db.String)
    cat5 = db.Column(db.String)
    cat6 = db.Column(db.String)

    def __repr__(self):
        return '<Category {}, {}, {}, {}, {}, {}, {}>'.format(self.id, self.cat1, self.cat2, self.cat3, self.cat4, self.cat5, self.cat6, self.cat7)

class product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String)
    brand = db.Column(db.String)
    productname = db.Column(db.String)
    price = db.Column(db.Integer)
    comment = db.Column(db.Integer)
    buy = db.Column(db.Integer)
    link = db.Column(db.String)

dirs = os.walk('C:/Users/my/Desktop/Mayweather/gmarket_crawling_data/category/')


'''
file = 'C:/Users/my/Desktop/Mayweather/category/남성의류/가디건_조끼/가디건.xlsx'
sheet = 'Sheet'

df = read_excel(file, sheet_name=sheet)
print(df.loc[1])

'''

'''
for dirpath, dirnames, filenames in dirs:
    if not dirnames:
        category_file = dirpath.replace('C:/Users/my/Desktop/Mayweather/category/', '')
        cat = category_file.replace('\\', '/')
        print(cat)

'''

#db.session.query(category).delete()
#db.session.commit()
#db.session.query(product).delete()
#db.session.commit()

'''
cate = []

for dirpath, dirnames, filenames in dirs:
    if not dirnames:
        category_file = dirpath.replace('C:/Users/my/Desktop/Mayweather/gmarket_crawling_data/category/', '')
        cat = category_file.split('\\')

        if len(cat) == 3:
            tmp = category(cat1 = cat[0], cat2 = cat[1], cat3 = cat[2])
            if cat[2] in cate:
                print(cat)
            cate.append(cat[2])
        elif len(cat) == 4:
            tmp = category(cat1 = cat[0], cat2 = cat[1], cat3 = cat[2], cat4 = cat[3])
            if cat[3] in cate:
                print(cat)
            cate.append(cat[3])
        elif len(cat) == 5:
            tmp = category(cat1 = cat[0], cat2 = cat[1], cat3 = cat[2], cat4 = cat[3], cat5 = cat[4])
            if cat[4] in cate:
                print(cat)
            cate.append(cat[4])
        elif len(cat) == 6:
            tmp = category(cat1 = cat[0], cat2 = cat[1], cat3 = cat[2], cat4 = cat[3], cat5 = cat[4], cat6 = cat[5])
            if cat[5] in cate:
                print(cat)
            cate.append(cat[5])
        #db.session.add(tmp)
        #db.session.commit()
'''


pymysql.install_as_MySQLdb()
import MySQLdb

engine = create_engine("mysql+mysqldb://root:"+"dkswnsgh226"+"@localhost/test", encoding='utf-8')
conn = engine.connect()

end = 0


for dirpath, dirnames, filenames in dirs:
    for filename in filenames:
        if '.xlsx' in filename:
            filename = filename.replace('~$', '')
            excel = dirpath.replace('\\', '/') + '/' + filename
            sheet = 'Sheet'
            df = read_excel(excel, sheet_name=sheet)
            if df.empty:
                continue
            df.columns = ['category', 'brand', 'productname', 'price', 'comment', 'buy', 'link']
            df['comment'] = df['comment'].fillna('0')
            df['buy'] = df['buy'].fillna('0')
            df['price'] = df['price'].apply(lambda x: int(str(x).replace(',','')))
            df['comment'] = df['comment'].apply(lambda x: int(str(x).replace('상품평 ','').replace(',', '')))
            df['buy'] = df['buy'].apply(lambda x: int(str(x).replace('구매 ','').replace(',', '')))
            df.to_sql(name='product', con=engine, if_exists='append', index=False)


