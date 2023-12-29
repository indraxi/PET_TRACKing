import pandas as pd
import requests
import bs4 
url="http://127.0.0.1:5500/index.html"
res=requests.get(url)
#print(res)
df=bs4.BeautifulSoup(res.text , features="html.parser")
#print(df)
now=df.find('div')
#print(now)
now1=now.find_all('p')
l=list(now1);
#print(l)
#for i in l:
    
l1=list(now.find_all('button'))
#print(l1)

