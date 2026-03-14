from ..database import Database

class UserModel:
    def __init__(self):
        self.db = Database()

    def create_user(self, username, email, password):
        query  = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        params = (username, email, password)
        return self.db.execute(query, params)

    def find_by_credentials(self, email, password):
        query  = "SELECT * FROM users WHERE email = %s AND password = %s"
        params = (email, password)
        return self.db.fetch_one(query, params)

    def find_by_email(self, email):
        query  = "SELECT * FROM users WHERE email = %s"
        params = (email,)
        return self.db.fetch_one(query, params)