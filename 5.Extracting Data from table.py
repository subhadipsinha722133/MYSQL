import mysql.connector

try:
    aa = mysql.connector.connect(
        # user="root", password="722133", host="localhost", port=3306
        user="root",
        password="722133",
        host="127.0.0.1",
        port=3306,
        database="py",
    )

except Exception as e:
    print("cannot connect")
else:
    print("connected")


c = aa.cursor()
v = " SELECT * FROM book"
c.execute(v)
result = c.fetchall()
for row in result:
    print(row)
