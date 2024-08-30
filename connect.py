import mysql.connector

try:
    conn = mysql.connector.connect(
        # user="root", password="722133", host="localhost", port=3306
        user="root",
        password="722133",
        host="127.0.0.1",
        port=3306,
    )

except Exception as obj:
    print("cannot connect")
else:
    print("connected")
