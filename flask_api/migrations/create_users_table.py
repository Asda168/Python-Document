from ..database import Database

def up():
    db = Database()
    db.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id          INT AUTO_INCREMENT PRIMARY KEY,
            username    VARCHAR(100) NOT NULL UNIQUE,
            email       VARCHAR(100) NOT NULL,
            password    VARCHAR(255) NOT NULL,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
    ''')
    print('Table users created successfully')

def down():
    db = Database()
    db.execute('DROP TABLE IF EXISTS users')
    print('Table users dropped successfully')