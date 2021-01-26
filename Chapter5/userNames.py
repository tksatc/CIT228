current_users = ["harry", "sally", "david", "bathsheeba", "connie"]
lower_users = []
for user in current_users:
    lower_users.append(user.lower())

new_users = ["caroline", "barbara", "john", "harry", "will"]

for user in new_users:
    if user in lower_users:
        print(user, " is in use.  Please use another user name.")
    else:
        print(user, " is available.")
