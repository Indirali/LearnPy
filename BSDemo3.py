from bs4 import BeautifulSoup
import requests
import time

url = 'https://cn.tripadvisor.com/Attractions-g60763-Activities-New_York_City_New_York.html'
urls = ['http://www.tripadvisor.cn/Attractions-g186338-Activities-c47-oa{}-London_England.html#ATTRACTION_LIST'.format(str(i)) for i in range(30,930,30)]
url_saves = 'http://www.tripadvisor.cn/Saves#515818'

headers = {
	'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2873.0 Safari/537.36',
	'Cookie':'TAUnique=%1%enc%3AiVBY0uT%2BgWJMLggSylhLTAPs3e0blYZ%2FUV2CE5X%2F%2FrJQcF0be502LA%3D%3D; TASSK=enc%3AALckkZhsoVJPvdiJAVAio5wsEYAlDl6cLzcn%2F9ht63Msrx0i6tpZuWiaC8LuTfyELLkmIG7WmYpioSCZb3ZsP09Ak%2FcIsnwVXZfJknZ04qw4uscKNMN3QBFGSpbSFuPBdQ%3D%3D; TAPD=tripadvisor.cn; __gads=ID=9b1f6cedfb8f03d4:T=1476195747:S=ALNI_MaNgn5UwS9rVMKRTx40cs4dkUsS8g; CommercePopunder=SuppressAll*1476196315915; TAAuth2=%1%3%3A071f235c214074f2385bbd9d3fca8016%3AALknJoArSWel2ytG0633q3HRecMbI%2FDXFybDeI1X%2BSwWm3gjvJtWI%2BfpMshhYnsuXkrAzworZeQgOCTk%2FWalrseodXJUE2JxuwRL%2BNbeS3Y005dDJfvDlk3tOx2e%2Bg0HAXrexf5keGIOYOOa5iVEidGabYyOpLKBIJ0tT4fNP492fFekEAXL1gPL%2FM%2FM7hmc3QdeLTL5L4AeoGghHov7FqE%3D; TATravelInfo=V2*A.2*MG.-1*HP.2*FL.3*RVL.105127_285*RS.1; CM=%1%HanaPersist%2C%2C-1%7Ct4b-pc%2C%2C-1%7CHanaSession%2C%2C-1%7CFtrSess%2C%2C-1%7CRCPers%2C%2C-1%7CHomeAPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CRCSess%2C%2C-1%7CFtrPers%2C%2C-1%7CHomeASess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CPremiumMCSess%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7C2016sticksess%2C%2C-1%7Csesscoestorem%2C%2C-1%7CCCPers%2C%2C-1%7CCCSess%2C%2C-1%7CViatorMCPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_SESSION%2C%2C-1%7Cb2bmcsess%2C%2C-1%7Csesssticker%2C%2C-1%7C2016stickpers%2C%2C-1%7Ct4b-sc%2C%2C-1%7CViatorMCSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C3%2C-1%7Csessamex%2C%2C-1%7Cperscoestorem%2C%2C-1%7CSaveFtrPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CSaveFtrSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CRBASess%2C%2C-1%7Cperssticker%2C%2C-1%7CMetaFtrSess%2C%2C-1%7CRBAPers%2C%2C-1%7CWAR_RESTAURANT_FOOTER_PERSISTANT%2C%2C-1%7CMetaFtrPers%2C%2C-1%7C; TAReturnTo=%1%%2FAttraction_Review-g60763-d105127-Reviews-Central_Park-New_York_City_New_York.html; bdshare_firstime=1476199248501; roybatty=TNI1625!ALTjsDOt3UXXxf3s5Fi6VtCeTKvl2x6r7lmyOTWiZqvGkpfh3mznuQ4jRfrkKowlCwzZt1dAtF6G22jzNYQxfCILNOgpK7QP9GFLKk7%2BAJzj23OFtYGpTwMZ83XHoQJ1jrEkNAn6UKdGOWY2TCxzkUVu%2BIDIAhQk%2Fl8toHb9lAbm%2C1; Hm_lvt_2947ca2c006be346c7a024ce1ad9c24a=1476195747; Hm_lpvt_2947ca2c006be346c7a024ce1ad9c24a=1476199254; ki_t=1476195754036%3B1476195754036%3B1476199254423%3B1%3B5; ki_r=; NPID=; TASession=%1%V2ID.65B14F9C706FA62CCD08CAA80312F8C3*SQ.32*PR.427%7C*LS.ActionRecord*GR.89*TCPAR.80*TBR.73*EXEX.17*ABTR.57*PPRP.81*PHTB.69*FS.90*CPU.33*HS.popularity*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.7BF65BC4424AD0A7550F1F39C44E7371*LF.zhCN*FA.1*DF.0*LP.%2FLangRedirect%3Fauto%3D3%26origin%3Dzh%26pool%3DC%26returnTo%3D%252FAttractions-g60763-Activities-New_York_City_New_York%5C.html*IR.3*OD.zh*MS.-1*RMS.-1*FLO.60763*TRA.true*LD.105127;'
}

def get_attractions(url,data=None):
	wb_data = requests.get(url,headers=headers)
	time.sleep(2)
	soup = BeautifulSoup(wb_data.text,'lxml')
	titles = soup.select('div.property_title > a[target="_blank"]')
	imgs = soup.select('img[width="160"]')
	cates = soup.select('div.p13n_reasoning_v2')

	for title,img,cate in zip(titles,imgs,cates):
		data ={
		'title':title.get_text(),
		'img'  :img.get('src'),
		'cate' :list(cate.stripped_strings)
		}
		print(data)

def get_favs(url,data=None):
	wb_data = requests.get(url,headers=headers)
	soup = BeautifulSoup(wb_data.text,'lxml')
	titles = soup.select('div.info > a.location-name')
	imgs = soup.select('div.photo > div.sizedThumb > img')
	cates = soup.select('div.cvs-content > div.info > div > span > img')
	addresses = soup.select('div.info > span.format_address')

	for title,img,cate,address in zip(titles,imgs,cates,addresses):
		data = {
			'title':title.get_text(),
			'img':img.get('src'),
			'cate':cate.get('alt'),
			'address':address.get_text()
		}
		print(data)

for single_url in urls:
	get_attractions(single_url)
# get_attractions(url)
# print('==================================================')
# get_favs(url_saves)

