import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='w3school'
)

mycursor = mydb.cursor()

mycursor.execute('CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))')
mycursor.execute('SHOW TABLES')

for x in mycursor:
    print(x)
