import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="w3school"
)

mycursor = mydb.cursor()

# 省略where子句，所有记录都将更新
sql = "UPDATE customers SET address = %s WHERE address = %s"
val = ('Valley 345', 'Canyon 123')

mycursor.execute(sql, val)
mydb.commit()

print(mycursor.rowcount, "record(s) affected")
