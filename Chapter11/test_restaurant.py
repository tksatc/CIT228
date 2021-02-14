import unittest
from restaurant import Restaurant

class TestRestaurant(unittest.TestCase):
    """Tests for class Restaurant"""

    def setUp(self):
        """Create a restaurant and responses for use in test methods"""
        restaurantName = "my house"
        typeCuisine = "any"
        numberServed = 201
        self.my_restaurant = Restaurant(restaurantName, typeCuisine, numberServed)
    
    def test_set_number_served_int(self):
        """Tests the set_number_served fx"""
        newNumberServed = 248
        self.my_restaurant.set_number_served(newNumberServed)
        self.assertEqual(self.my_restaurant.number_served, 248)

    def test_set_number_served_str(self):
        """Tests set number served fx if a string is passed to it"""
        newNumberServed = "248"
        self.my_restaurant.set_number_served(newNumberServed)
        self.assertEqual(self.my_restaurant.number_served, 248)
    
    def test_increment_number_served_int(self):
        """Tests the increment number fx"""
        incrementNumberBy = 42
        self.my_restaurant.increment_number_served(incrementNumberBy)
        self.assertEqual(self.my_restaurant.number_served, 243)
        
    
    def test_increment_number_served_str(self):
        """Tests the increment number fx if a string is passed"""
        incrementNumberBy = "42"
        self.my_restaurant.increment_number_served(incrementNumberBy)
        self.assertEqual(self.my_restaurant.number_served, 243)
    
if __name__ == "__main__":
    unittest.main()
