import datetime
import mysql.connector
cnx = mysql.connector.connect(user='iot',password='***', host='172.16.16.151', database='northwind')
cursor = cnx.cursor()

query = ('SELECT * FROM CUSTOMERS')
cursor.execute(query)

for row in cursor:
    print(row)

cursor.close()
cnx.close()