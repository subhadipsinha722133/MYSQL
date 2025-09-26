import mysql.connector

try:
    aa = mysql.connector.connect(
        # user="root", password="722133", host="localhost", port=3306
        user="root",
        password="722133",
        host="127.0.0.1",
        port=3306,
        database="da1",
    )

except Exception as e:
    print("cannot connect")
else:
    print("connected")

ca = aa.cursor()
s = "UPDATE book SET price =price + 10 WHERE price >200"
ca.execute(s)
aa.commit()
