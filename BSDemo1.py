from bs4 import BeautifulSoup

info = []
with open('E:\python工程/1_1/the_blah.html') as wb_data:
	Soup = BeautifulSoup(wb_data,'lxml')
	#print(Soup)
	images = Soup.select('body > div.main-content > ul > li > img')
	titles = Soup.select('body > div.main-content > ul > li > h3 > a')
	descs = Soup.select('body > div.main-content > ul > li > p')
	#print(images,titles,descs,sep='\n--------------------------\n')

for image,title,desc in zip(images,titles,descs):
	data = {
		'title':title.get_text(),
		'desc' :desc.get_text(),
		'image':image.get('src')
		#list(cate.stripped_strings)#若有多个值
	}
	info.append(data)
	#print(data)

for i in info:
	if i['title'] == 'The blah':
		print(i['desc'])
	if i['desc'] == 'It\'s a sandwich.  That\'s all we .':
		print(i['title'])

'''
body > div.main-content > ul > li:nth-child(1) > img
body > div.main-content > ul > li:nth-child(1) > h3 > a
body > div.main-content > ul > li:nth-child(1) > p
'''


