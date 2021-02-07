class User:
    """A simple representation of a user profile"""

    def __init__(self, first_name, last_name, user_name, email, password, login_attempts=0):
        """Initialize attributes to describe a user"""
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.email = email
        self.password = password
        self.login_attempts = login_attempts

    def describe_user(self):
        """Prints user's information"""
        print(f"{self.first_name.title()} {self.last_name.title()}'s user name is: {self.user_name}.\nThe user's password is: {self.password} and the email is: {self.email}.")

    def greet_user(self):
        """Prints a greeting to the user"""
        print(f"Welcome back, {self.first_name.title()}!")

    def increment_login_attempts(self):
        """Increments the number of login attempts by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets login attempts to 0"""
        self.login_attempts = 0

user1 = User("halle", "barry", "hbarry", "hallewho@gmail.com", "whoville123")
user2 = User("will", "smith", "prince1", "willie@gmail.com", "hailtotheprince")
user3 = User("sophie", "starlin", "filosophizer", "sophie321@gmail.com", "samiam345")
user4 = User("melanie", "jones", "smileyface", "melanie@gmail.com", "password123")

print("\n")

users = [user1, user2, user3]

for user in users:
    user.greet_user()
    user.describe_user()
    print("\n")

user4.increment_login_attempts()
print(f"{user4.first_name.title()} has tried to login {user4.login_attempts} times.")

user4.increment_login_attempts()
print(f"{user4.first_name.title()} has tried to login {user4.login_attempts} times.")

user4.increment_login_attempts()
print(f"{user4.first_name.title()} has tried to login {user4.login_attempts} times.")

user4.increment_login_attempts()
print(f"{user4.first_name.title()} has tried to login {user4.login_attempts} times.")

user4.increment_login_attempts()
print(f"{user4.first_name.title()} has tried to login {user4.login_attempts} times.")

user4.reset_login_attempts()
print(f"{user4.first_name.title()}, you have exceeded the acceptable number of login attempts.\n"
      f"The number of attempts has been reset to: {user4.login_attempts}.\n"  
      "Your account has been locked for 60 minutes.")