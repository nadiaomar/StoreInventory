import requests
import bs4
import time
import re


index_url = 'http://www.homedepot.com/b/Electrical-Home-Electronics-Home-Audio/N-5yc1vZc641'

response = requests.get(index_url)
soup = bs4.BeautifulSoup(response.text)


content = soup.find("div", { "id" : "content" })

core = content.find("div", {'id': 'plp_core'})

print("=============================")

# feedarray = feed.findAll('span', {'class': 'cond'})

# for x in feedarray:
# 	print(x)
# 	print("=============================")


spad = core.findAll('div', {'class': 'spad'})

for d in spad:
	# print(d)
	print("-------------------------")

	atag = d.find('a', {'class':'item_description'})

	name = atag.getText().strip()
	URL = atag.get('href')

	SKU = d.find('span', {'class': None}).getText()

	MSRPblob = d.find('span', {'class':'xlarge item_price'}).getText()
	regexPattern = "\$\d*\.\d{2}"
	patt = re.compile(regexPattern)
	MSRP = patt.match(MSRPblob).group()

	print(name)
	print(MSRP)
	print(SKU)
	print(URL)

	fullSecond = 1
	time.sleep(fullSecond)


	item_response = requests.get(URL)
	item = bs4.BeautifulSoup(item_response.text)


	p_description = item.find("div", {'id': 'product_description'})

	print("=============================")

	main = p_description.find('div', {'class': 'main_description'})

	description = main.find('p', {'class':'normal'}).getText()
	print(description)


						