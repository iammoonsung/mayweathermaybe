from urllib.request import urlopen
from urllib.parse import urlencode, quote_plus, unquote, quote

import urllib
import requests
import json
import pandas as pd

import numpy as np
import datetime

def getTodayWeather(nx, ny) :
    CallBackURL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'

#    if base_hour <= datetime.datetime.now().hour :
#        CallBackURL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'
#    else :
#        CallBackURL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
    
    params = '?' + urlencode({
        quote_plus("serviceKey"): "SA9AA7saC0AbWyhwr9MkjMhWcHRZnem3B4uasXtonSpiC6EqlQv%2Bacm6NCGD%2BUXaY6KjE5HHLtJca5XGxPzvjA%3D%3D",
        quote_plus("numOfRows"): "82",
        quote_plus("pageNo"): "1",
        quote_plus("dataType"): "JSON",
        quote_plus("base_date"): "202008" +str(datetime.datetime.now().day),
#        quote_plus("base_time"): ("%02d"% base_hour)+"00",
        quote_plus("base_time"): "0500",
        quote_plus("nx"): str(nx),
        quote_plus("ny"): str(ny)
    })
    

    req = urllib.request.Request(CallBackURL + unquote(params))
    response_body = urlopen(req).read()
    
    data = json.loads(response_body)
#    print(data)

    res = pd.DataFrame(data['response']['body']['items']['item'])
    
    return res



def getTommoWeather(nx, ny) :
    CallBackURL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'

#    if base_hour <= datetime.datetime.now().hour :
#        CallBackURL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'
#    else :
#        CallBackURL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
    
    params = '?' + urlencode({
        quote_plus("serviceKey"): "SA9AA7saC0AbWyhwr9MkjMhWcHRZnem3B4uasXtonSpiC6EqlQv%2Bacm6NCGD%2BUXaY6KjE5HHLtJca5XGxPzvjA%3D%3D",
        quote_plus("numOfRows"): "82",
        quote_plus("pageNo"): "2",
        quote_plus("dataType"): "JSON",
        quote_plus("base_date"): "202008" +str(datetime.datetime.now().day),
#        quote_plus("base_time"): ("%02d"% base_hour)+"00",
        quote_plus("base_time"): "0500",
        quote_plus("nx"): str(nx),
        quote_plus("ny"): str(ny)
    })
    
    

    req = urllib.request.Request(CallBackURL + unquote(params))
    response_body = urlopen(req).read()
    
    data = json.loads(response_body)
#    print(data)

    res = pd.DataFrame(data['response']['body']['items']['item'])
    
    return res




def getShortWeather(nx, ny) :
    CallBackURL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtFcst'

#    if base_hour <= datetime.datetime.now().hour :
#        CallBackURL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'
#    else :
#        CallBackURL = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getVilageFcst'
    
    params = '?' + urlencode({
        quote_plus("serviceKey"): "SA9AA7saC0AbWyhwr9MkjMhWcHRZnem3B4uasXtonSpiC6EqlQv%2Bacm6NCGD%2BUXaY6KjE5HHLtJca5XGxPzvjA%3D%3D",
        quote_plus("numOfRows"): "30",
        quote_plus("pageNo"): "1",
        quote_plus("dataType"): "JSON",
        quote_plus("base_date"): "202008" +str(datetime.datetime.now().day),
#        quote_plus("base_time"): ("%02d"% base_hour)+"00",
        quote_plus("base_time"): "1200",
        quote_plus("nx"): str(nx),
        quote_plus("ny"): str(ny)
    })
    
    

    req = urllib.request.Request(CallBackURL + unquote(params))
    response_body = urlopen(req).read()
    
    data = json.loads(response_body)
#    print(data)

    res = pd.DataFrame(data['response']['body']['items']['item'])
    
    return res



def getHourDust() :
    CallBackURL = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty'
    sidoname = quote('종로구')
    params = '?' + urlencode({
        quote_plus("serviceKey"): "SA9AA7saC0AbWyhwr9MkjMhWcHRZnem3B4uasXtonSpiC6EqlQv%2Bacm6NCGD%2BUXaY6KjE5HHLtJca5XGxPzvjA%3D%3D",
        quote_plus("stationName"): sidoname,
        quote_plus("dataTerm"): "DAILY",
#        quote_plus("ver"): "4",
    })
    
    print(CallBackURL + unquote(params))

    req = urllib.request.Request(CallBackURL + unquote(params))
    response_body = urlopen(req)
    data = response_body.read().decode('utf-8')

    
    return data



def calcWbgt(RH_, Ta_) :
    l=[]
    for i in range(8) :
        RH = RH_.iloc[i]
        Ta = Ta_.iloc[i]
        Tw = Ta*np.arctan(0.151977*(RH+8.313659)**0.5) + np.arctan(Ta + RH) - np.arctan(RH-0.167633) + 0.00391838*RH**1.5*np.arctan(0.023101*RH) - 4.686035
        wbgt = -0.2442 + 0.55399*Tw + 0.45535*Ta - 0.0022*Tw**2 + 0.00278*Tw*Ta
        wbgt = round(wbgt,2)
        l.append(wbgt)
    
    return l


def calcWindchill(vel_, Ta_) :
    l=[]
    for i in range(8) :
        vel = vel_.iloc[i]
        Ta = Ta_.iloc[i]
        Twc = 13.12 + 0.6215*Ta -11.37*(vel**0.16) + 0.3965*Ta*(vel**0.16)
        windchill = round(Twc,2)
        l.append(windchill)
    
    return l


def wv(df) :
    if df.iloc[0]['fcstDate'][6:8] == str(datetime.datetime.now().day+1) :
        temp_max = df[df['category']=='TMX'].fcstValue.astype(float).mean()
        temp_min = df[df['category']=='TMN'].fcstValue.astype(float).mean()
        temp_avg = df[df['category']=='T3H'].fcstValue.astype(float).mean()
        tempdiff = temp_max - temp_min

        precp_dur = len(df[df['category']=='POP'][df[df['category']=='POP'].fcstValue.astype(float)>85])*3
        onehr_precp = df[df['category']=='R06'].fcstValue.astype(float).max()/6
        precp_amount = df[df['category']=='R06'].fcstValue.astype(float).sum()

        rh_avg = df[df['category']=='REH'].fcstValue.astype(float).mean()

        wspd_avg = df[df['category']=='WSD'].fcstValue.astype(float).mean()

        cloud_avg = df[df['category']=='SKY'].fcstValue.astype(float).mean()

        wbgt = calcWbgt(df[df['category']=='REH'].fcstValue.astype(float), df[df['category']=='T3H'].fcstValue.astype(float))
        wbgt_avg = np.mean(wbgt)
        wbgt_max = np.max(wbgt)
        wbgt_min = np.min(wbgt)

        windchill = calcWindchill(df[df['category']=='WSD'].fcstValue.astype(float), df[df['category']=='T3H'].fcstValue.astype(float))
        windchill_avg = np.mean(windchill)
        windchill_max = np.max(windchill)
        windchill_min = np.min(windchill)

        snow = df[df['category']=='S06'].fcstValue.astype(float).sum()

    else :
        temp_min_prev = df[df['category']=='TMN'].fcstValue.astype(float).mean()
        temp_min_prev = df[df['category']=='TMX'].fcstValue.astype(float).mean()
        precp_amount_prev = df[df['category']=='R06'].fcstValue.astype(float).sum()
        
    globals().update(locals())


def manyDust(pm, misepm) :
    count = 0
    if pm > 30 :
        if pm > 80 :
            count += 2
        else :
            count += 1
    if misepm > 15 :
        if misepm > 30 :
            count += 2
        else :
            count += 1

    return count


# sample values

pm = 10.
misepm = 10.


def weatherGrouping(nx, ny) :
    titleList = ['눈오는 날', '거센 소나기', '잠깐 소나기', '요즘 비오네', '꿉꿉한 비', '추운 비', '선선한 비', '쪄 죽을 날', '더운 날', '괜찮게 더운 날', '해가 쨍쨍한 날', '얼어 죽을 날', '추운 날', '괜찮게 추운 날', '흐린 추운 날', '일교차 큰 날', '미세먼지 많은 날', '좋은 날', '진짜 좋은 날', '피곤한 날']
    
    df_prev = getTodayWeather(nx,ny)
    wv(df_prev)
    df = getTommoWeather(nx, ny)
    wv(df)
    
    f = np.zeros(20)
    
    if snow > 0 :
        f[0] = 1
    else :
        if precp_amount > 0 :
            if precp_dur > 4 :
                if precp_amount_prev > 0 :
                    f[3] = 1
                else :
                    if wbgt_avg > 23 :
                        f[4] = 1
                    else :
                        if windchill_avg < 5 :
                            f[5] = 1
                        else :
                            if onehr_precp > 10 :
                                f[3] = 1
                            else :
                                f[6] = 1
            else :
                if wspd_avg > 3 :
                    f[1] = 1
                else :
                    if onehr_precp > 10 :
                        f[1] = 1
                    else :
                        f[2] = 1
        else :
            if wbgt_max > 28 :
                if temp_avg > 28 :
                    if wspd_avg > 2 :
                        if cloud_avg > 5 :
                            f[9] = 1
                        else :
                            f[8] = 1
                    else :
                        f[7] = 1
                else :
                    if (temp_max - temp_max_prev) > 2. :
                        if cloud_avg < 3 :
                            f[10] = 1
                        else :
                            f[8] = 1
                    else :
                        if manyDust(pm, misepm) > 1 :
                            f[16] = 1
                        else :
                            f[9] = 1
            else :
                if windchill_min < 0 :
                    if (temp_min - temp_min_prev) < -2. :
                        if wspd_avg > 3 :
                            f[11] = 1
                        else :
                            f[12] = 1
                    else :
                        if wspd_avg > 3 :
                            f[12] = 1
                        else :
                            if manyDust(pm, misepm) > 1 :
                                f[16] = 1
                            else :
                                if cloud_avg < 3 :
                                    f[13] = 1
                                else :
                                    f[14] = 1
                else :
                    if tempdiff > 10 :
                        if manyDust(pm, misepm) > 1 :
                            f[16] = 1
                        else :
                            if temp_max - prev['temp_max'] > 2. :
                                f[15] = 1
                            else :
                                if temp_min - prev['temp_min'] < -2. :
                                    f[15] = 1
                                else :
                                    f[17] = 1
                    else :
                        if manyDust(pm, misepm) > 1 :
                            f[16] = 1
                        else :
                            if cloud_avg < 5 :
                                f[18] = 1
                            else :
                                f[17] = 1
    
    result = []
    for i, x in enumerate(f) :
        if x == 1 :
            result.append(titleList[i])
                                
    return result[0]