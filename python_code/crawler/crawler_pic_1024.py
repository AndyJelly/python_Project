# -*- coding:utf-8 -*-
import requests
import os
from bs4 import BeautifulSoup as bs
import re
from contextlib import closing

root_url = 'http://pp.postcc.us/'
#达盖尔版块
module_url = 'thread0806.php?fid=16&search=&page=%d'

headers = {
	'Accept-Encoding':'gzip, deflate',
	'Origin':'http://pp.postcc.us',
	'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

def get_title_url(request_url):
	resp = requests.get(request_url,headers=headers)
	resp.encoding = 'utf-8'
	soup = bs(resp.text,'html.parser')
	links = soup.find_all('a',href = re.compile(r'^htm_data'))
	page_urls = set()
	for link in links:
		page_link = root_url + link['href']
		page_urls.add(page_link)
	return page_urls

#获取每个页面中的图片url
def get_pic_of_page(page_url):
	try:
		resp = requests.get(page_url,headers=headers)
		resp.raise_for_status()
	except exceptions.Timeout as e:
		print ("exceptions.Timeout")
	except exceptions.HTTPError as e:
		print ("exceptions.HTTPError: %d" % resp.status_code)
	else:
		resp.encoding = 'utf-8'
		soup = bs(resp.text,'html.parser')
		links = soup.find_all('input',src=re.compile(r'^http://www'))
		pic_urls = set()
		for link in links:
			pic_link = link['src']
			pic_urls.add(pic_link)
		return pic_urls


def downloadPicByURL(pic_url,pic_name):
	#存储流数据
	try:
		response = requests.get(pic_url,stream = True,timeout = 60,headers=headers)
		response.raise_for_status()
	except exceptions.Timeout as e:
		#pass
		print("exceptions.Timeout")
	except exceptions.HTTPError as e:
		#pass
		print ("exceptions.HTTPError: %d" % resp.status_code)
	else:
		with closing(response) as resp:
			with open(pic_name,'wb') as fd:
				#每128个字节写入一次
				for chunk in resp.iter_content(128):
					fd.write(chunk)

if __name__ == '__main__':
	#循环获取前两页的url
	count = 0
	for i in range(3,4):
		request_url = root_url + module_url % i
		page_urls = get_title_url(request_url)
	print (len(page_urls))
	while len(page_urls):
		page_link = page_urls.pop()
		print ('page url: %s' % page_link)
		pic_urls = get_pic_of_page(page_link)
		print (len(pic_urls))
		while len(pic_urls):
			pic_url  = pic_urls.pop()
			pic_name = 'D:\\1024\\CL1024pic_' + str(count) + '.jpg'
			downloadPicByURL(pic_url,pic_name)
			count = count + 1
			print ('%s  download success!' % pic_url)


		
