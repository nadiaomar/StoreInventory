import psycopg2

try:
    conn = psycopg2.connect("dbname='nhdinventory' user='postgres' host='localhost' password='test123'")
    cur = conn.cursor()
    cur.execute("INSERT INTO Inventory(onhand, instock) VALUES (3, 22);")

    # rows = cur.fetchall()

    # for row in rows:
    # 	print row

    conn.commit()


except:
    print "I am unable to connect to the database"