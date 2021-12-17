import pandas as pd
from bs4 import BeautifulSoup
from urllib.request import urlopen
htmlname = input('url:')+".html"
# urlopen 函數讀取 html 檔案
html = urlopen("file:"+htmlname)
# 指定 BeautifulSoup 的解析器為 lxml
bs = BeautifulSoup(html, "lxml")
model=urlopen('file:modify.html')
bs1=BeautifulSoup(model,"lxml")
modify_table=bs1.find('table')
bs.find('table').replace_with(modify_table)
csv_name=input('csv nsme:')+".csv"
data=pd.read_csv(csv_name)
if('推出日期' in data.index):
    bs.find(id="d1").string=data.loc['推出日期'][0]
if('感光元件像素' in data.index):
    bs.find(id="d3").string=data.loc['感光元件像素'][0]
if('感光元件大小' in data.index):    
    bs.find(id="d4").string=data.loc['感光元件大小'][0]
if('感光元件種類' in data.index):
    bs.find(id="d5").string=data.loc['感光元件種類'][0]
if('感光元件種類' in data.index):
    bs.find(id="d6").string=data.loc['鏡頭接環'][0]
if('自動對焦情況' in data.index):
    bs.find(id="d7").string=data.loc['自動對焦情況'][0]
if('最大解像度' in data.index):    
    bs.find(id="d8").string=data.loc['最大解像度'][0]
if('動畫解像度' in data.index):    
    bs.find(id="d9").string=data.loc['動畫解像度'][0]
if('動畫種類' in data.index):    
    bs.find(id="d10").string=data.loc['動畫種類'][0]
if('場景模式' in data.index):    
    bs.find(id="d11").string=data.loc['場景模式'][0]
if('測光模式' in data.index):    
    bs.find(id="d12").string=data.loc['測光模式'][0]
if('曝光補償' in data.index):    
    bs.find(id="d13").string=data.loc['曝光補償'][0]
if('白平衡設定' in data.index):    
    bs.find(id="d14").string=data.loc['白平衡設定'][0]
if('連拍' in data.index):    
    bs.find(id="d15").string=data.loc['連拍'][0]
if('快門速度' in data.index):    
    bs.find(id="d16").string=data.loc['快門速度'][0]
if('ISO 感光值' in data.index):    
    bs.find(id="d17").string=data.loc['ISO 感光值'][0]
if('LCD 熒光幕' in data.index):    
    bs.find(id="d18").string=data.loc['LCD 熒光幕'][0]
if('儲存媒體' in data.index):    
    bs.find(id="d19").string=data.loc['儲存媒體'][0]
if('電池種類' in data.index):    
    bs.find(id="d20").string=data.loc['電池種類'][0]
if('電池壽命' in data.index):    
    bs.find(id="d21").string=data.loc['電池壽命'][0]
if('機身重量' in data.index):    
    bs.find(id="d22").string=str(data.loc['機身重量'][0])
if('重量(含電池)' in data.index):    
    bs.find(id="d23").string=data.loc['重量(含電池)'][0]
if('體積' in data.index):    
    bs.find(id="d24").string=data.loc['體積'][0]
if('附註' in data.index):    
    bs.find(id="d25").string=data.loc['附註'][0]
with open(htmlname,'w') as wr:
    wr.write(str(bs.prettify()))