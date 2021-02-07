from user import User
from privileges import Privileges

class Admin(User):
    """Represents an Admin use type"""
    def __init__(self, first_name, last_name, user_name, email, password, privileges, login_attempts=0):
        """Initializes attributes to describe an Admin user"""
        super().__init__(first_name, last_name, user_name, email, password, login_attempts=0)
        self.privileges = Privileges(privileges)