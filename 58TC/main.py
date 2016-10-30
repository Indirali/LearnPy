from multiprocessing  import Pool
from channel_extract import channel_url
from page_parsing import get_links_from

def get_all_links_from(channel):
	for num in range(1,101):
		get_links_from(channel,num)

if __name__ == '__main__':
	pool = Pool()
	pool.map(get_all_links_from,channel_url.split())