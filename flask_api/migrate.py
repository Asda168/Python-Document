import sys
from migrations.create_users_table import up, down

def migrate(action='up'):
    if action == 'up':
        print('Running migrations...')
        up()
        print('Migrations completed')
    elif action == 'down':
        print('Rolling back migrations...')
        down()
        print('Rollback completed')
    else:
        print(f'Unknown action: {action}')

if __name__ == '__main__':
    action = sys.argv[1] if len(sys.argv) > 1 else 'up'
    migrate(action)