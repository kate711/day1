import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='w3school'
)

mycursor = mydb.cursor()

# where 选择
sql = "SELECT * FROM customers WHERE address ='Park Lanr 38'"

# sql = "SELECT * FROM customers"

mycursor.execute(sql)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
