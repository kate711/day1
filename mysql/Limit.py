import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="w3school"
)

mycursor = mydb.cursor()
# 前5条
# mycursor.execute("SELECT * FROM customers LIMIT 5")

# 从第三条纪录开始返回五条
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
