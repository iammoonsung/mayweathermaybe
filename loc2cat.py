from k2c import find_category, find_categoryid
from weather_cate import weatherGrouping


with open('/home/ubuntu/real/mayweathermaybe/weather2keyword.txt', 'r') as f:
    weather_keywords = []
    data = f.readlines()
    for info in data[1:]:
        infolist = info.replace("'",'').replace('"','').replace('[','').replace(']','').replace('\n','').split(',')
        weather_keywords.append([infolist[0], infolist[1:]])


def loc2cat(nx, ny, wk=weather_keywords, catnumber=1, minscore=0.3, mode='id'):
    weather = weatherGrouping(nx, ny)
    categories = []
    for info in wk:
        if info[0] == weather:
            for keyword in info[1]:
                categories += find_category(keyword.strip(), catnumber=catnumber, minscore=minscore)
            if mode == 'cat':
                return categories
            elif mode == 'id':
                ids = find_categoryid(categories)
                return ids
            else:
                print("Invalid mode: 'id' or 'cat' is needed")
                return False
    