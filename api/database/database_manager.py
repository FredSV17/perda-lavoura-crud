from multiprocessing import connection
import flask_mysqldb
import mysql.connector
from flask_mysqldb import MySQL
import os

class DatabaseManager:
    connection = None
    cursor = None
    def __init__(self) -> None:
        self.connection = mysql.connector.connect(
            host=os.environ['SQL_CONNECTION'],
            user="root",
            password="",
            database="loss_db"
        )
        self.cursor = self.connection.cursor()
        
    def close_connection(self):
        self.cursor.close()


    # cur.execute("""INSERT INTO users(name) VALUES(%s)""",('angelo',))
    # connection.commit()
    # cur.execute("""SELECT name FROM users""")
    # result = [item[0] for item in cur.fetchall()]
    # cur.close()

