import sys
from . import migrate, rollback

action = sys.argv[1] if len(sys.argv) > 1 else 'up'

if action == 'up':
    print('Running migrations...')
    migrate()
    print('Migrations completed')
elif action == 'down':
    print('Rolling back migrations...')
    rollback()
    print('Rollback completed')
else:
    print(f'Unknown action: {action}')