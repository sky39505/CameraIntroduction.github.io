import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
path="/Users/zicheng/.bitnami/stackman/machines/xampp/volumes/root/htdocs/geodarn/pages/olympus"
a=os.listdir(path)
re=urlopen("file:re.html")
s=BeautifulSoup(re,'lxml')
r=s.find("li")
for i in range(len(a)):
    count=0
    if a[i][0]!="." and a[i][-5:]==".html" and a[i]!="re.html":
        response=urlopen("file:"+a[i])
        soup=BeautifulSoup(response,'lxml')
        for j in soup.find("nav",{"class":"fl_right"}).findAll("li"):
            if count==6:
                j.replace_with(r)
                count+=1
            else:
                count+=1
    if a[i][0]!="." and a[i][-5:]==".html" and a[i]!="re.html":
        with open(a[i],'w')as wr:
            wr.write(str(soup.prettify()))