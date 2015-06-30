import requests
import bs4
import time
import re
import random
import psycopg2

conn = None
cur = None

try:
	conn = psycopg2.connect("dbname='nhdinventory' user='postgres' host='localhost' password='test123'")
	cur = conn.cursor()

except:
	print("I am unable to connect to the database")	
	
# conn = psycopg2.connect("dbname='nhdinventory' user='postgres' host='localhost' password='test123'")
# cur = conn.cursor()
index_url = 'http://www.homedepot.com/b/Electrical-Home-Electronics-Home-Audio/N-5yc1vZc641'

response = requests.get(index_url)
soup = bs4.BeautifulSoup(response.text)


content = soup.find("div", { "id" : "content" })

core = content.find("div", {'id': 'plp_core'})
	

spad = core.findAll('div', {'class': 'spad'})

for d in spad:

	atag = d.find('a', {'class':'item_description'})

	name = atag.getText().strip().encode('utf8')
	URL = atag.get('href')
response = requests.get(index_url)
soup = bs4.BeautifulSoup(response.text)


content = soup.find("div", { "id" : "content" })

core = content.find("div", {'id': 'plp_core'})



	SKU = d.find('span', {'class': None}).getText().encode('utf8')

	MSRPblob = d.find('span', {'class':'xlarge item_price'}).getText()
	regexPattern = "\$\d*\.\d{2}"
	patt = re.compile(regexPattern)
	
	MSRP_with_dollar_sign = patt.match(MSRPblob).group().encode('utf8')
	MSRP_without_dollar_sign = MSRP_with_dollar_sign[1:]

	# This makes it a number type
	MSRP = float(MSRP_without_dollar_sign)

	fullSecond = 0.2
	time.sleep(fullSecond)


	item_response = requests.get(URL)
	item = bs4.BeautifulSoup(item_response.text)


	p_description = item.find("div", {'id': 'product_description'})

	main = p_description.find('div', {'class': 'main_description'})

	description = main.find('p', {'class':'normal'}).getText().strip().encode('utf8')

	command1 = "INSERT INTO Inventory (sku, onhand, instock) VALUES ('{}', {}, {})"

	onhand = random.randint(0,10)
	instock = random.randint(10,30)

	command1Complete = str.format(command1, SKU, onhand, instock)

	print(command1Complete)

	cur.execute(command1Complete)
	conn.commit()

	command2 = "INSERT INTO Products(sku, name, msrp, wholesale, description) VALUES('{}', '{}', {}, {}, '{}');"

	wholesalePercentage = 1 - random.uniform(.05, .50)
	whPrice = wholesalePercentage * MSRP
	formattedWhPrice = "%.2f" % whPrice

	wholesale = float(formattedWhPrice)
	print(wholesale)

	Command2Complete = str.format(command2, SKU, name, MSRP, wholesale, description)

	print(Command2Complete)

	cur.execute(Command2Complete)
	conn.commit()

	# create vars instock, onhand
	# use str.format() to format the command
	# execute the command

	# write command2 to add the remaining info to the Products table
	# Use random num generator to make wholesale price some % of msrp