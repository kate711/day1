import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='w3school'
)

mycursor = mydb.cursor()

# %s 转义查询值
sql = "SELECT * FROM customers WHERE address = %s"
adr = ('Yellow Garden 2',)

mycursor.execute(sql, adr)
myresult = mycursor.fetchall()

for x in myresult:
    print(x)
