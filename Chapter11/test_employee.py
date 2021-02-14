import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests the Employee class"""

    def setUp(self):
        """Creates test object for all test methods"""
        firstName = "jane"
        lastName = "smith"
        salary = 30000
        self.myEmployee = Employee(firstName, lastName, salary)

    def test_give_default_raise_float(self):
        """Tests give_raise fx with default value"""
        self.myEmployee.give_raise()
        self.assertEqual(self.myEmployee.get_salary(), 35000)
    
    def test_give_custom_raise_float(self):
        """Tests give_raise fx with custom increase"""
        increase = 3000
        self.myEmployee.give_raise(increase)
        self.assertEqual(self.myEmployee.get_salary(), 33000)
    
if __name__ == "__main__":
    unittest.main()
