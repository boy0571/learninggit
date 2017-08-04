# -*- coding: utf-8 -*-
import string
import urllib2
import re
import datetime

def weather(date):
    myurl = 'http://shanghai.tianqi.com/'+date+'.html'
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent':user_agent}
    req = urllib2.Request(myurl,headers=headers)
    myResponse = urllib2.urlopen(req)
    myPage = myResponse.read()
    unicodePage = myPage.decode("gbk").encode('utf-8')
    myItem = re.findall('天气预报：(.*?)。" name="description">',unicodePage,re.S)
    print myItem
    return myItem[0]

starttime = datetime.datetime(2014,1,2)
for i in range(1370):
    starttime=starttime+datetime.timedelta(days=1)
    if starttime.month>9:
        if starttime.day>9:
            date =str(starttime.year)+str(starttime.month)+str(starttime.day)
        else:
            date = str(starttime.year) + str(starttime.month) + '0'+str(starttime.day)


    else:
        if starttime.day>9:
            date = str(starttime.year) + '0'+str(starttime.month) + str(starttime.day)
        else:
            date = str(starttime.year) + '0' + str(starttime.month) + '0'+str(starttime.day)
    print date
    fi_weather=weather(date)
    print fi_weather
    f=open('weather_20170424','a')
    f.write(date)
    f.write(',')
    f.write(fi_weather)
    f.write('\n')
    f.close()
