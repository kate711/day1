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
# 插入多行
val = [
    ('John', 'Highway 21'),
    ('Amy', 'Apple st 652'),
    ('Peter', 'Lowstreet 4'),
    ('Hannah', 'Mouuntain 21'),
    ('Michael', 'Valley 345'),
    ('Sandy', 'Ocean Grass 1'),
    ('Richard', 'Sky st 331'),
    ('Susan', 'One way 98'),
    ('Vicky', 'Yellow Garden 2'),
    ('Ben', 'Park Lanr 38'),
    ('William', 'Central st 954'),
    ('Chuck', 'Main Road 989'),
    ('Viola', 'Sideway 1633')
]
# executemany
mycursor.executemany(sql, val)
# 更改，否则表不会有改变
mydb.commit()

print(mycursor.rowcount, "record inserted")
