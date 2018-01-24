from bs4 import BeautifulSoup
html_sample = """
<html>
<body>
<h1 id="title">Hello world</h1>
<a href="#" class="link">This is Link1</a>
<a href="# link2" class="link">This is Link2</a>
</body>
</html>
"""
soup = BeautifulSoup(html_sample,'html.parser')
#header = soup.select('h1')
#print(header[0])
alink = soup.select('a')
for link in alink:
    #print(link)
    print(link.text)
    print(link['href'])
    print(link['class'])

title = soup.select('#title')
print(title[0])

cls = soup.select('.link')
for  cla in cls:
    print(cla)

###################################################
import requests
from bs4 import BeautifulSoup
resp = requests.get('http://news.sina.com.cn/china/')
resp.encoding = 'utf-8'
soup = BeautifulSoup(resp.text,'html.parser')
#print (len(soup.select('.news-item')))
for news in soup.select('.news-item'):
    #print(news)
    if news.select('h2') :
        h2 = news.select('h2')[0].text
        a = news.select('a')[0]['href']
        time = news.select('.time')[0].text
        print(time,h2,a)
        
 ###################################################################
 import requests
from bs4 import BeautifulSoup
resp = requests.get('http://news.sina.com.cn/c/gat/2018-01-24/doc-ifyqyqni2029115.shtml')
resp.encoding = 'utf-8'
soup = BeautifulSoup(resp.text,'html.parser')
#print(soup.text)
title = soup.select('.main-title')[0].text
time = soup.select('.date')[0].text
source = soup.select('.source')[0].text
print(source)
 
 
