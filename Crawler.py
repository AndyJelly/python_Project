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
 
    
    
##########################################################################
import re
import requests
import json


commenturl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=\
comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3'
def getCommentCounts(newsurl):
    m = re.search('doc-i(.*).shtml',newsurl)
    newsid = m.group(1)
    comments = requests.get(commenturl.format(newsid))
    jd = json.loads(comments.text)
    return jd['result']['count']['total']

newsurl ='http://news.sina.com.cn/c/gat/2018-01-24/doc-ifyqyqni2029115.shtml'
getCommentCounts(newsurl)


import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
newsurl ='http://news.sina.com.cn/c/gat/2018-01-24/doc-ifyqyqni2029115.shtml'

resp = requests.get(newsurl)
resp.encoding = 'utf-8'
soup = BeautifulSoup(resp.text,'html.parser')
#print(soup.text)
title = soup.select('.main-title')[0].text
time = soup.select('.date')[0].text
source = soup.select('.source')[0].text
#print(source)
#print (time)
dt = datetime.strptime(time, '%Y年%m月%d日 %H:%M')
#print(dt)
#print (dt.strftime('%Y-%m-%d'))
#artical = []
#for p in soup.select('#article p')[:-2]:
#    artical.append(p.text.strip())
#print(artical)
#print (' '.join(artical))

body = ' '.join([ p.text.strip() for p in soup.select('#article p')[:-2]])

editor = soup.select('.show_author')[0].text.strip('责任编辑：')
#print (editor)


newsid = newsurl.split('/')[-1].rstrip('.shtml').lstrip('doc-i')
import re


print(newsid)

comenturl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=\
comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3'
print (comenturl)

comment = requests.get(comenturl)


jd = json.loads(comment.text)
totalComments = jd['result']['count']['total']
 
    
    
##########################################################################################
import requests
from bs4 import BeautifulSoup
resp = requests.get('http://sports.sina.com.cn/g/laliga/')
resp.encoding = 'utf-8'
soup = BeautifulSoup(resp.text,'html.parser')

print(soup.select('.match_news_list li a')[2].contents)
