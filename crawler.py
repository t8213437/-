#coding:utf-8
import requests
import json
import time
from bs4 import BeautifulSoup

f = open('web.json', 'w', encoding='utf-8')
data = []
for i in range(1,55):
    url = "http://www.appledaily.com.tw/realtimenews/section/new/" + str(i)
    if i % 5 == 0:
        time.sleep(10)
    response = requests.get(url)
    #print(response.text)

    soup = BeautifulSoup(response.text, "html.parser")

    for item in soup.findAll('li', {'class' : 'rtddt'}):
        #f.write('{\"time\" : \"' + item.a.time.text + '\",\t')
        #f.write('\"h2\" : \"' + item.a.h2.text + '\",\t')
        #f.write('\"h1\" : \"' + item.a.h1.text + '\"}\n')
        d = {"time" : item.a.time.text, "h2" : item.a.h2.text, "h1" : item.a.h1.text}
        data.append(d)
        print(item.a.h1.text)

file = json.dumps(data  , ensure_ascii = False)
f.write(file)
f.close()

#f2 = open('web.json', 'r', encoding='utf-8')

#file2 = json.load(f2)

#print(file2)
