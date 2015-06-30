import psycopg2

try:
    conn = psycopg2.connect("dbname='nhdinventory' user='postgres' host='localhost' password='test123'")
    cur = conn.cursor()

    command = "INSERT INTO Inventory(onhand, instock) VALUES (3, 22);"
    print(command)
    cur.execute(command)

    # rows = cur.fetchall()

    # for row in rows:
    # 	print row

    conn.commit()

except:
    print "I am unable to connect to the database"