print("\n-------------------Exercise 5-8--------------------")

userNames = ["admin", "harry", "debra", "carrie", "daniel"]

if userNames[:]:
    for user in userNames:
        if user == "admin":
            print("Hello ", user.title(), ", would you like to see a status report?")
        else:
            print("Hello, ", user.title(), ", thank you for logging in again.")

print("\n-------------------Exercise 5-9 with no users--------------------")

userNames.clear()

if userNames[:]:
    print("We have users.")
else:
    print("We need to find some users!")

