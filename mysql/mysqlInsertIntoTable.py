import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='w3school'
)

mycursor = mydb.cursor()

# 插入表
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# 插入单行
val = ("John", "Highway 21")
mycursor.execute(sql, val)
# 更改，否则表不会有改变
mydb.commit()

print(mycursor.rowcount, "record inserted")
