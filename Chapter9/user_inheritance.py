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

class Privileges:
    """Represents user privileges"""
    def __init__(self, privileges):
        self.privileges = [privileges]

    # Created to test list functionality
    def add_privilege(self, privilege):
        """Adds a privilege to the list"""
        self.privilege = self.privileges.append(privilege)
    
    def show_privileges(self):
        """Displays Admin privileges"""
        for privilege in self.privileges:
            print(privilege.title())

class Admin(User):
    """Represents an Admin use type"""
    def __init__(self, first_name, last_name, user_name, email, password, privileges, login_attempts=0):
        """Initializes attributes to describe an Admin user"""
        super().__init__(first_name, last_name, user_name, email, password, login_attempts=0)
        self.privileges = Privileges(privileges)

admin = Admin("john", "doe", "jdoe123", "jdoe@gmail.com", "aloevera", "can delete post")

admin.privileges.add_privilege("can overwrite post")   #-> for testing list functionality

print("\n-------Admin Privileges-------")

admin.privileges.show_privileges()
