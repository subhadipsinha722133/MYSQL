import mysql.connector

try:
    conn = mysql.connector.connect(
        user="root", password="722133", host="localhost", port=3306, database="mydb"
    )
    if conn.is_connected():
        print("Connected!")
except Exception as e:
    print("cannot connect")

cur = conn.cursor()

sql = """INSERT INTO tutorial(
    Video_id INT PRIMARY KEY,
    Video_name VARCHAR(100),
    Video_views INT,
    Watchtime FLOAT)VALUES(101,'oop basics',15000,20.0)"""
cur.execute(sql)
conn.commit()
cur.close()
conn.close()
