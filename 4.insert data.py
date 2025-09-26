import mysql.connector

try:
    conn = mysql.connector.connect(
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

a = conn.cursor()
s = "INSERT INTO book(bookid, title,price) VALUES(%s, %s, %s)"
b = (1, "PYTHON3", 499)
a.execute(s, b)

conn.commit()
