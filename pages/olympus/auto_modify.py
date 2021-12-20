import pandas as pd
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import csv
import os
"""
擷取data網站
"""
response=urlopen('file:target_data.html')
bs=response
soup=BeautifulSoup(bs,'html.parser')
f=open('URLs.csv',"w",encoding='utf8')
w=csv.writer(f)
w.writerow(['name','url'])
for i in soup.findAll("div",{"class":"model_no"}):
    name=i.a.string
    url="https://www.dcfever.com/cameras/full"+i.find("a")['href']
    temp=[name,url]
    w.writerow(temp)
f.close()
URLs=pd.read_csv('URLs.csv')
file=open("/Users/zicheng/.bitnami/stackman/machines/xampp/volumes/root/htdocs/geodarn/pages/OLYMPUS.html",'r')
html_file=file.read()
file.close()
soup=BeautifulSoup(html_file,'lxml')
f=open('html_names.csv','w',encoding='utf8')
w=csv.writer(f)
w.writerow(['name','html_name'])
for i in soup.find('table').findAll('tbody'):
    for j in i.findAll('tr'):
        for k in j.findAll('td'):
            w.writerow([k.a.text,k.a['href'][8:-5]])
f.close()
html_names=pd.read_csv('html_names.csv')
df=URLs.merge(html_names,on="name")
try:
    os.remove('/Users/zicheng/.bitnami/stackman/machines/xampp/volumes/root/htdocs/geodarn/pages/olympus/URLs.csv')
except OSError as e:
    print(e)
try:
    os.remove('/Users/zicheng/.bitnami/stackman/machines/xampp/volumes/root/htdocs/geodarn/pages/olympus/html_names.csv')
except OSError as e:
    print(e)
"""
擷取網站中的data，輸出data的csv
"""
for i in range(29):
    url=df.loc[i]['url']
    response=requests.get(url)
    bs=response.content
    soup=BeautifulSoup(bs,'html.parser')
    filename=df.loc[i]['html_name']+".csv"
    f=open(filename,"w",encoding='utf8')
    w=csv.writer(f)
    for i in soup.find("table").findAll("tr"):
        cell=i.findAll("td")
        temp=[]
        for x in cell:
            temp.append(x.text)
        w.writerow(temp)
    f.close()
"""
編寫html
"""
for i in range(29):
    model=urlopen('file:modify.html')
    bs=BeautifulSoup(model,"lxml")
    bs.find('title').string="CAMERA | Olympus | Introduction | "+df.loc[i]['name'][8:]
    bs.find(id="d0").string=df.loc[i]['name'][8:]
    bs.find(id="d2").string=df.loc[i]['name']
    bs.find(id="img")['src']="img/"+df.loc[i]['html_name']+".jpg"
    htmlname=df.loc[i]['html_name']+".html"
    data=pd.read_csv(df.loc[i]['html_name']+".csv")
    if('推出日期' in data.index):
        bs.find(id="d1").string=str(data.loc['推出日期'][0])
    if('感光元件像素' in data.index):
        bs.find(id="d3").string=str(data.loc['感光元件像素'][0])
    if('感光元件大小' in data.index):    
        bs.find(id="d4").string=str(data.loc['感光元件大小'][0])
    if('感光元件種類' in data.index):
        bs.find(id="d5").string=str(data.loc['感光元件種類'][0])
    if('感光元件種類' in data.index):
        bs.find(id="d6").string=str(data.loc['鏡頭接環'][0])
    if('自動對焦情況' in data.index):
        bs.find(id="d7").string=str(data.loc['自動對焦情況'][0])
    if('最大解像度' in data.index):    
        bs.find(id="d8").string=str(data.loc['最大解像度'][0])
    if('動畫解像度' in data.index):    
        bs.find(id="d9").string=str(data.loc['動畫解像度'][0])
    if('動畫種類' in data.index):    
        bs.find(id="d10").string=str(data.loc['動畫種類'][0])
    if('場景模式' in data.index):    
        bs.find(id="d11").string=str(data.loc['場景模式'][0])
    if('測光模式' in data.index):    
        bs.find(id="d12").string=str(data.loc['測光模式'][0])
    if('曝光補償' in data.index):    
        bs.find(id="d13").string=str(data.loc['曝光補償'][0])
    if('白平衡設定' in data.index):    
        bs.find(id="d14").string=str(data.loc['白平衡設定'][0])
    if('連拍' in data.index):    
        bs.find(id="d15").string=str(data.loc['連拍'][0])
    if('快門速度' in data.index):    
        bs.find(id="d16").string=str(data.loc['快門速度'][0])
    if('ISO 感光值' in data.index):    
        bs.find(id="d17").string=str(data.loc['ISO 感光值'][0])
    if('LCD 熒光幕' in data.index):    
        bs.find(id="d18").string=str(data.loc['LCD 熒光幕'][0])
    if('儲存媒體' in data.index):    
        bs.find(id="d19").string=str(data.loc['儲存媒體'][0])
    if('電池種類' in data.index):    
        bs.find(id="d20").string=str(data.loc['電池種類'][0])
    if('電池壽命' in data.index):    
        bs.find(id="d21").string=str(data.loc['電池壽命'][0])
    if('機身重量' in data.index):    
        bs.find(id="d22").string=str(data.loc['機身重量'][0])
    if('重量(含電池)' in data.index):    
        bs.find(id="d23").string=str(data.loc['重量(含電池)'][0])
    if('體積' in data.index):    
        bs.find(id="d24").string=str(data.loc['體積'][0])
    if('附註' in data.index):    
        bs.find(id="d25").string=str(data.loc['附註'][0])
    with open(htmlname,'w') as wr:
        wr.write(str(bs.prettify()))
    remove_file_name='/Users/zicheng/.bitnami/stackman/machines/xampp/volumes/root/htdocs/geodarn/pages/olympus/'+df.loc[i]['html_name']+'.csv'
    try:
        os.remove(remove_file_name)
    except OSError as e:
        print(e)
    else:
        print("Success",(i+1))