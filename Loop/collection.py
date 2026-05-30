# Create a sample collection (object)
users = {
    'Asda' : 'active', 
    'Tesco' : 'inactive', 
    'Sainsbury' : 'active' 
}

# Iterate over a copy
# user: singular for loop variable
# status: value of the current item
# Example: users = {'user': 'status'}

for user, status in users.copy().items(): #filter inactive users
    if status == 'inactive': # The value of the current item is 'inactive'
        del users[user] # Delete the current item

# Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print(active_users)
    