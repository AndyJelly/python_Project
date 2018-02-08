# -*- coding:utf-8 -*-

from baike_spider import url_manager, html_download, html_parser, html_outputer

class SpiderMain(object):
	def __init__(self):
		#url管理
		self.urls = url_manager.UrlManager()
		#url下载
		self.downloader = html_download.HtmlDownloader()
		#html解析
		self.parser = html_parser.HtmlParser()
		#下载为html文件
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		count = 1 
		self.urls.add_new_url(root_url)
		while self.urls.has_new_url():
			try:
				#获取url
				new_url = self.urls.get_new_url()
				print 'craw %d :%s' % (count,new_url)
				#下载html数据
				html_count = self.downloader.download(new_url)
				#解析获取到的html数据，并返回解析到的urls
				new_urls, new_data = self.parser.parser(new_url,html_count)
				#将获取到的urls，放到url管理器中
				self.urls.add_new_urls(new_urls)
				#收集爬到的数据
				self.outputer.collect_data(new_data)
				
				if count == 1000:
					break
				count += 1
			except:
				print 'craw failed'

		#生成html文件
		self.outputer.output_html()

if __name__ == '__main__':
	root_url = 'https://baike.baidu.com/item/Python/407313'
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)
