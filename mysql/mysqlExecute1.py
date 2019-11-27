import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='w3school'
)

print(mydb)

# mycursor = mydb.cursor()
# # mycursor.execute('CREATE DATABASE w3school')
# mycursor.execute('SHOW DATABASES')
# for x in mycursor:
#     print(x)
