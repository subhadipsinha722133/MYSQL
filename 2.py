import mysql.connector

config = {"user": "root", "password": "722133", "host": "localhost", "port": 3306}

try:
    conn = mysql.connector.connect(**config)

except:
    print("Unable to connect")
