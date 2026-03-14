from ..database import Database

def up():
    db = Database()
    db.execute('''
        CREATE TABLE IF NOT EXISTS categories (
            id          INT AUTO_INCREMENT PRIMARY KEY,
            name        VARCHAR(100) NOT NULL UNIQUE,
            description TEXT,
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
        )
    ''')
    print('Table categories created successfully')

def down():
    db = Database()
    db.execute('DROP TABLE IF EXISTS categories')
    print('Table categories dropped successfully')