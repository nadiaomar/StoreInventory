import psycopg2
import mysql.connector as mysql
import random 

conn = None
cur = None

try:
	# conn = psycopg2.connect("dbname='nhdinventory' user='postgres' host='localhost' password='test123'")
	DBUSER = 'nadia'
	DBPASS = 'test123'
	DBHOST = 'localhost'
	DBNAME = 'inventory'


	conn = mysql.connect(user=DBUSER, password=DBPASS, host=DBHOST, database=DBNAME)
	cur = conn.cursor()

except:
	print("I am unable to connect to the database")	

cur.execute('SELECT sku, name, description, msrp FROM Products;');
rows = cur.fetchall()


print "\nShow me the databases:\n"

skus = []
names = []
descriptions = []
msrps = []


for row in rows:
	print row

	sku = row[0]
	name = row[1]
	description = row[2]
	msrp = row[3]

	skus.append(sku)
	names.append(name)
	descriptions.append(description)
	msrps.append(msrp)


print("Hi! Welcome to Home Depot.")
print(skus)

for n in range(len(names)):
	print "(" , n, ") : ", skus[n], names[n]

index = int(raw_input("What would you like to purchase?\n"))



name = names[index]
sku = skus[index]
description = descriptions[index]
msrp = msrps[index]


print(name)	
print(msrp)
print(sku)
print(description)



template = "SELECT onhand, instock FROM Inventory WHERE sku = '{}';"
command = str.format(template, sku)

# formmated = str.format(template, obj1, obj2, ......)

cur.execute(command);


rows = cur.fetchall()

onhand = rows[0][0]
instock = rows[0][0]
leftover = None

print(name)


amount = onhand + 1000


while onhand < amount:
	amount = int(raw_input("How many would you like?\n"))
	

	if amount > onhand:
		print("We don't have that many in stock.")
		template = "Would you like {} instead? [Yes/No]"
		question = str.format(template, onhand)
		print(question)
		# cur.execute(command);
		response = str(raw_input())

		if response == "Yes":
			template = "UPDATE Inventory SET onhand = {} WHERE sku = '{}';"
			command = str.format(template, 0, sku)
			cur.execute(command)
			conn.commit()
			amount = onhand
			onhand = 0 

	if amount <= onhand:
		temp = "UPDATE Inventory SET onhand = {} WHERE sku = '{}';"
		leftover = onhand - amount
		comm = str.format(temp, leftover, sku)
		cur.execute(comm)
		conn.commit()


print("Your final amount is %s") % amount

total = amount * msrp
print("Your total is %s") % total


template1 = "UPDATE Inventory SET onhand = {} WHERE sku = '{}';"
takefrominstock = random.randint(0, instock)
onhand = leftover + takefrominstock 	
command1 = str.format(template1, onhand, sku)
print(command1)
cur.execute(command1)
conn.commit()
#print(command1)



template2 = "UPDATE Inventory SET instock = {} WHERE sku = '{}';"
rand_instock = random.randint(0,10)
instock = instock + rand_instock
command2 = str.format(template2, instock, sku)
cur.execute(command2)
conn.commit()
#print(command2)






	# message to say we dont have in stock
	# get input
	# if yes, update db to remove that amount
	#newamount = str(raw_input("We don't have that many, would you like %d instead?\n"))
	


 
