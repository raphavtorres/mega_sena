import mysql.connector

db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='mega_sena'
)

cursor = db.cursor()
