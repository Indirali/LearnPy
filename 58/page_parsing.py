from bs4 import BeautifulSoup
import requests
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list']
item_info = ceshi['item_info']

def get_links_from(channel,pages,who_sells=0):
	#http://sjz.58.com/iphonesj/0/pn2/
	list_view = '{}{}/pn{}/'.format(channel,str(who_sells),str(pages))
	wb_data = requests.get(list_view)
	time.sleep(1)
	soup = BeautifulSoup(wb_data.text,'lxml')
	if soup.find('td','t'):
		for link in soup.select('td.t a.t'):
			item_link = link.get('href').split('?')[0]
			url_list.insert_one({'url':item_link})
			print(item_link)
	else:
		pass
#get_links_from("http://sjz.58.com/gouwuka/",2)

def get_item_info(url):
	wb_data = requests.get(url)
	soup = BeautifulSoup(wb_data.text,'lxml')
	# no_longer_exist = '404' in soup.find('script',type="text/javascript").get('src').split('/')
	# if no_longer_exist:
	# 	pass
	# else:
	title = soup.title.text
	price_now = soup.select("div.price_li > span.price_now > i")
	price = soup.select("div.price_li > span.price_now > b")
	address = soup.select("div.info_massege.left > div.palce_li > span > i")
	look_time = soup.select("p.info_p > span.look_time")
	cates = soup.select("div.quality > span.qlabel > span")
	data = {
			"title":title.strip(),
			"price_now":price_now[0].text if price_now!=[] else None,
			"price":price[0].text if price!=[] else None ,
			"address":address[0].text if address!=[] else None,
			"look_time":look_time[0].text if look_time!=[] else None,
			"cate":list(cate.get_text() for cate in cates ) if cates!=[] else None
		}
	print(data)
	item_info.insert_one(data)


get_item_info('http://zhuanzhuan.58.com/detail/788741580514951172z.shtml')
#get_item_info('http://zhuanzhuan.58.com/detail/787480808256815108z.shtml')





