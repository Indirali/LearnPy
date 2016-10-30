from multiprocessing  import Pool
from channel_extract import channel_list
from page_parsing import get_links_from,get_item_info
import time
import pymongo

client = pymongo.MongoClient('localhost',27017)
ceshi = client['ceshi']
url_list = ceshi['url_list']

def get_all_links_from(channel):
	for num in range(1,101):
		get_links_from(channel,num)

if __name__ == '__main__':
	pool = Pool()
	#pool.map(get_all_links_from,channel_list.split())
	for item in url_list.find():
		if item['url']!="http://jump.zhineng.58.com/jump":
			get_item_info(item['url'])
		else:
			pass
		