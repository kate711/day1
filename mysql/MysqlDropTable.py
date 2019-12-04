import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="w3school"
)

mycursor = mydb.cursor()

# sql = "DROP TABLE customers"
sql = "DROP TABLE IF EXISTS products"

mycursor.execute(sql)

sql1 = "SHOW TABLES"

mycursor.execute(sql1)

result = mycursor.fetchall()

for x in result:
    print(x)
