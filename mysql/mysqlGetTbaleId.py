import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='w3school'
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES(%s, %s)"
val = ("Michell", "Blue Village")
mycursor.execute(sql, val)

mydb.commit()
print("1 record inserted, ID", mycursor.lastrowid)
