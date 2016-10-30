from bs4 import BeautifulSoup
import requests
url = "http://zhuanzhuan.58.com/detail/783567581020700676z.shtml"

def get_links_from(who_sells=0):
	urls = []
	list_view = "http://sjz.58.com/diannao/{}/pn2/".format(str(who_sells))
	wb_data = requests.get(list_view)
	soup = BeautifulSoup(wb_data.text,"lxml")
	links = soup.select("td.t  a.t")
	for link in links:
		urls.append(link.get('href').split('?')[0])
	return urls
	#print(urls)

def get_item_info(who_sells=0):
	
	urls = get_links_from(who_sells)
	for url in urls:
		wb_data = requests.get(url)
		soup = BeautifulSoup(wb_data.text,"lxml")
		title = soup.title.text
		price_now = soup.select("div.price_li > span.price_now > i")
		price = soup.select("div.price_li > span.price_now > b")
		address = soup.select("div.info_massege.left > div.palce_li > span > i")
		look_time = soup.select("p.info_p > span.look_time")
		cate = soup.select("div.biaoqian_li")
		data = {
			"title":title.strip(),
			"price_now":price_now[0].text,
			"price":price[0].text if price!=[] else None ,
			"address":address[0].text,
			"look_time":look_time[0].text,
			"cate":list(cate[0].stripped_strings)
		}
		datas.append(data)

datas = []
get_item_info()
print(datas)