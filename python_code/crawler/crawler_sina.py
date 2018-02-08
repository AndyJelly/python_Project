import requests
from bs4 import BeautifulSoup
import json
import re
from datetime import datetime
import threading
import pandas
import sqlite3


def parserListLink(url):
	newsdetails = []
	res = requests.get(url)
	jd = json.loads(res.text.lstrip('  newsloadercallback(').rstrip(');'))
	for ent in jd['result']['data']:
		print (ent['url'])
		newsdetails.append(getNewsDatil(ent['url']))
	return newsdetails

def getCommentrCount(newsurl):
	commenturl = 'http://comment5.news.sina.com.cn/page/info?version=1&format=json&channel=gn&newsid=\
comos-{}&group=undefined&compress=0&ie=utf-8&oe=utf-8&page=1&page_size=3'

	m = re.search('doc-i(.*).shtml',newsurl)
	newsid = m.group(1)
	comments = requests.get(commenturl.format(newsid))
	jd = json.loads(comments.text)
	return jd['result']['count']['total']

def getNewsDatil(newsurl):
	result = {}
	res = requests.get(newsurl)
	res.encoding = 'utf-8'
	soup = BeautifulSoup(res.text,'html.parser')
	result['title'] = soup.select('.main-title')[0].text
	result['source'] = soup.select('.source')[0].text
	result['dt'] = datetime.strptime(soup.select('.date')[0].text, '%Y年%m月%d日 %H:%M')
	result['editor'] = soup.select('.show_author')[0].text.strip('责任编辑：')
	result['article'] = ' '.join([ p.text.strip() for p in soup.select('#article p')[:-2]])
	result['comments'] = getCommentrCount(newsurl)
	return result

if __name__ == '__main__':
	url ="""
http://api.roll.news.sina.com.cn/zt_list?channel=news&\
cat_1=gnxw&cat_2==gdxw1||=gatxw||=zs-pl||=mtjj&level==1||=2&\
show_ext=1&show_all=1&show_num=22&tag=1&format=json&page={}&\
callback=newsloadercallback&_=1516979383123
	"""
	news_total = []
	for i in range(1,3):
		print (url.format(i))
		newsary = parserListLink(url.format(i))
		news_total.extend(newsary)
	print (len(news_total))
	df = pandas.DataFrame(news_total)
	df.to_excel('news.xlsx')

	with sqlite3.connect('news.sqlite') as db:
		df.to_sql('news',con=db)
		
		#pandas.read_sql_query('SELECT * FROM news',con =db)
	#print(len(news_total))
