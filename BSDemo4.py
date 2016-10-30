from bs4 import BeautifulSoup
import requests

headers = {
	'User-Agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1'
}

url = 'http://www.tripadvisor.cn/Attractions-g186338-Activities-c47-oa50-London_England.html'

mb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(mb_data.text,'lxml')
#print(soup)
imgs = soup.select('div.thumb.thumbLLR.soThumb > img')
titles = soup.select('div.title.titleLLR > div')
metas = soup.select('div.attraction_types > span')

#print(imgs)

for img,title,meta in zip(imgs,titles,metas):
	data = {
		'title' : title.get_text(),
		'img'   : img.get("src"),
		'meta'  : meta.get_text()
	}
	print(data)


'''
#a629912 > div.thumb.thumbLLR.soThumb
#lazyload_-211736093_7
#lazyload_-211736093_6 img height="54" width="54"
#a214625 > div.container.containerLLR > div.title.titleLLR > div
#a214625 > div.container.containerLLR > div.attraction_types > span
'''
