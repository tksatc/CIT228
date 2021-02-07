from user import User
from privileges import Privileges
from admin import Admin

admin = Admin("john", "doe", "jdoe123", "jdoe@gmail.com", "aloevera", "can delete post")

admin.privileges.add_privilege("can overwrite post")   #-> for testing list functionality

print("\n-------Admin Privileges-------")

admin.privileges.show_privileges()
