from sqlalchemy import create_engine
import pandas as pd
import pymysql
import fasttext

pymysql.install_as_MySQLdb()
import MySQLdb

engine = create_engine((
        'mysql+pymysql://{user}:{password}@13.125.205.2:3306/{database}').format(
        user='root', password='testtest',
        database='mayweather'), encoding='utf-8')
conn = engine.connect()
categorydb = pd.read_sql_table('category', conn)

model = fasttext.load_model('category_classifier_v5.bin')

def find_category(keyword, model = model, catnumber = 1, minscore = 0.3):
    result = []
    category = model.predict(keyword, catnumber)
    for i in range(len(category[0])):
        if category[1][i] >= minscore:
            result.append(category[0][i].replace('__label__', ''))
    
    return result


def find_categoryid(category, df = categorydb):
    ids = []
    for cat in category:
        for i in range(4,8):
            id = df.loc[(df['cat'+str(i)] == cat), 'id'].tolist()
            if id:
                ids.append(id[0])
    
    return list(set(ids))