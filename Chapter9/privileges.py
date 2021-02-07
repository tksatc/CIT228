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