import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='w3school'
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

# mycursor.execute('SELECT name, address FROM customers')

# fetchall() 从最后执行的语句中获取所取有行
# myresult = mycursor.fetchall()

# fetchone() 返回结果的第一行
myresult = mycursor.fetchone()
print(myresult)

for x in myresult:
    print(x)
