import mysql.connector

try:
    conn = mysql.connector.connect(
        user="root", password="722133", host="localhost", port=3306
    )
    if conn.is_connected():
        print("Connected!")
except:
    print("cannot connect")


cur = conn.cursor()
cur.execute("CREATE DATABASE mydb")
cur.close()
conn.close()
