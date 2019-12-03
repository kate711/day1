import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="w3school"
)

mycursor = mydb.cursor()

# sql = "SELECT * FROM customers ORDER BY name DESC"

sql = "DELETE FROM customers WHERE address = 'Mouuntain 21'"

mycursor.execute(sql)

mydb.commit()

# myresult = mycursor.fetchall()

print(mycursor.rowcount, "record(s) deleted")
