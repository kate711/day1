import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="w3school",
    # 设置buffered
    buffered=True
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2",)

mycursor.execute(sql, adr)

"""
执行sql语句查询后,MySQLCursorBuffered游标标从服务器获取整个结果集并将他们放在缓冲区中。
Buffered游标适用于多个小结果集的查询,且多个结果集之间的数据需要一起使用。
使用buffered游标执行查询语句时 ,取行方法（如fetchone()，fechcall()等）返回的是缓冲区中的行。
nonbuffered游标不从服务器获取数据,直到调用了某个获取数据行的方法, 
在使用nonbuffered游标时,必须确保取出的结果是结果集中的所有行，才能再用同一连接执行其他语句,否则会报错InternalError(Unread result found)。
原文链接：https://blog.csdn.net/qq_43471020/article/details/84323154

"""

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")
