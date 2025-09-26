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
cur.execute("SHOW DATABASES ")

for data in cur:
    print(data[0])
print(list(cur))
cur.close()
conn.close()
