import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='w3school'
)

mycursor = mydb.cursor()

# mycursor.execute('CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))')
# mycursor.execute('CREATE TABLE users (name VARCHAR(255), fav VARCHAR(255))')
mycursor.execute('CREATE TABLE products (id VARCHAR(255), name VARCHAR(255))')
# mycursor.execute('SHOW TABLES')
# mycursor.execute('DROP TABLE products')
mycursor.execute('SHOW TABLES')

for x in mycursor:
    print(x)

