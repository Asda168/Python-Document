from .create_users_table      import up as users_up,      down as users_down
from .create_categories_table import up as categories_up,  down as categories_down
from .create_products_table   import up as products_up,    down as products_down

def migrate():
    users_up()
    categories_up()
    products_up()

def rollback():
    products_down()
    categories_down()
    users_down()