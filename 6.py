import mysql.connector

try:
    conn = mysql.connector.connect(
        user="root", password="722133", host="localhost", port=3306
    )
    if conn.is_connected():
        print("Connected!")
except Exception as e:
    print("cannot connect")

cur = conn.cursor()
# cur.execute("SHOW DATABASES ")
# for data in cur:
# print(data[0])
# print(list(cur))
cur.execute("USE mydb")
cur.execute(
    """CREATE TABLE IF NOT EXISTS tutorial(
    Video_id INT PRIMARY KEY,
    Video_name VARCHAR(100) NOT NULL,
    Video_views INT,
    Watchtime FLOAT)"""
)
cur.close()
conn.close()
