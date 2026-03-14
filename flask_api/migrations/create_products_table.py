from ..database import Database

def up():
    db = Database()
    db.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id          INT AUTO_INCREMENT PRIMARY KEY,
            category_id INT NOT NULL,
            name        VARCHAR(100) NOT NULL,
            description TEXT,
            price       DECIMAL(10, 2) NOT NULL DEFAULT 0.00,
            stock       INT NOT NULL DEFAULT 0,
            image       VARCHAR(255),
            created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
        )
    ''')
    print('Table products created successfully')

def down():
    db = Database()
    db.execute('DROP TABLE IF EXISTS products')
    print('Table products dropped successfully')