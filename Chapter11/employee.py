class Employee:
    """Models an employee"""
    def __init__(self, first, last, salary):
        """Instantiate an employee object"""
        self.first_name = first
        self.last_name = last
        self.salary = salary

    def get_salary(self):
        """Retrieves salary"""
        return self.salary
    
    def set_salary(self, salary):
        """Sets a salary"""
        self.salary = float(salary)

    def give_raise(self, increase=5000):
        """Adds an amount to salary"""
        self.salary += float(increase)

"""
For Testing Purposes

employee = Employee("tonya", "starlin", 50000)
print(f"{employee.first_name.title()}, your annual salary is: ${employee.salary: ,.2f}")

employee.give_raise()
print(f"New salary is: ${employee.salary: ,.2f}")

employee.give_raise(10000)
print(f"New salary is: ${employee.salary: ,.2f}")
"""