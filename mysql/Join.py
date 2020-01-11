import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="w3school"
)

# mycursor = mydb.cursor()
#
# # sql = "INSERT INTO users (name, fav) VALUES (%s, %s)"
# # 插入多行
# val = [
#     ('John', '154'),
#     ('Peter', '154'),
#     ('Amy', '154'),
#     ('Hannah', ''),
#     ('Michael', '')
# ]
#
# # mycursor.execute('ALTER TABLE products id VARCHAR(255), name VARCHAR(255)')
# sql = "INSERT INTO products (name, id) VALUES (%s, %s)"
# # val1 = [
# #     ('154', 'Chocolate Heaven' ),
# #     ('154','Tasty lemons'),
# #     ('154', 'Vailla Dreams')
# # ]
# # # executemany
# mycursor.executemany(sql, val)
# # mycursor.executemany(sql1, val1)
# # # 更改，否则表不会有改变
# mydb.commit()
# #
# print(mycursor.rowcount, "record inserted")
#
# mycursor.execute("ALTER TABLE users ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
#
# mycursor.execute('SHOW TABLES')
# for x in mycursor:
#     print(x)
#

mycursor = mydb.cursor()

sql = "SELECT users.name AS user, products.name AS favorite FROM users INNER JOIN products ON users.fav = products.id"

# None
print(mycursor.execute(sql))

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
