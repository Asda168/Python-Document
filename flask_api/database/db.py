import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='flask_db',
                user='root',
                password=''
            )
        except Error as e:
            print(f'Connection error: {e}')

    def disconnect(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()

    def execute(self, query, params=None):
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            self.connection.commit()
            return cursor
        except Error as e:
            print(f'Execute error: {e}')
            return None
        finally:
            self.disconnect()

    def fetch_one(self, query, params=None):
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            return cursor.fetchone()
        except Error as e:
            print(f'Fetch one error: {e}')
            return None
        finally:
            self.disconnect()

    def fetch_all(self, query, params=None):
        try:
            self.connect()
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            return cursor.fetchall()
        except Error as e:
            print(f'Fetch all error: {e}')
            return []
        finally:
            self.disconnect()