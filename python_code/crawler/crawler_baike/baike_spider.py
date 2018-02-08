# -*- coding:utf-8 -*-
#python27
#import urllib2
#python36
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

root_url = 'https://baike.baidu.com/item/Python/407313'
#resp = urllib2.urlopen(root_url)
resp = urlopen(root_url)

soup = BeautifulSoup(resp.read(),'html.parser',from_encoding= 'utf-8')

new_urls = set()

#href="/item/GPL"
links = soup.find_all('a',href=re.compile(r'/item/.*'))
print (len(links))
for link in links:
	new_url = link['href']
	
	temp_url = root_url[:root_url.find('/item/')] 
	new_full_url = temp_url + new_url
	print (new_full_url)
