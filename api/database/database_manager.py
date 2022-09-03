import flask_mysqldb
import mysql.connector
from flask_mysqldb import MySQL    

class DatabaseManager:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="flaskdocker"
    )
    cur = connection.cursor()


    # cur.execute("""INSERT INTO users(name) VALUES(%s)""",('angelo',))
    # connection.commit()
    # cur.execute("""SELECT name FROM users""")
    # result = [item[0] for item in cur.fetchall()]
    # cur.close()

