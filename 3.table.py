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


cur = aa.cursor()
s = "CREATE TABLE book (bookid integer (4),title varchar(20),price float(5,2))"
cur.execute(s)
