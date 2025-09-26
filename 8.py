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
# cur.execute("SHOW DATABASES ")

# print(list(cur))
cur.execute("USE mydb")
cur.execute(
    """CREATE TABLE IF NOT EXISTS tutorial2(
    Video_id INT PRIMARY KEY,
    Video_name VARCHAR(100) NOT NULL,
    Video_views INT,
    Watchtime FLOAT)"""
)
cur.execute("DESC tutorial")
for data in cur:
    print(data[0])
# print(list[0])
cur.close()
conn.close()
