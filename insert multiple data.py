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


a = aa.cursor()
s = "INSERT INTO book(bookid, title,price) VALUES(%s, %s, %s)"
b = [(2, "PHP", 299), (3, "SQL", 400), (4, "c++", 300), (5, "java", 300), (6, "C", 300)]
a.executemany(s, b)

aa.commit()
