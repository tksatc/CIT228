class Restaurant:
    """A simple attempt to represent a restaurant"""

    def __init__(self, restaurant_name, cuisine_type, number_served=0):
        """Initializes restaurant attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served=0

    def describe_restaurant(self):
        """Prints restaurant descriptors"""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} food.\n{self.number_served} guests have been served.")
        
    def open_restaurant(self):
        """Announces restaurant's opening"""
        print(f"{self.restaurant_name.title()} is now open!")

    def set_number_served(self, new_number_served):
        """Updates number of guests served"""
        self.number_served = new_number_served

    def increment_number_served(self, number_increment):
        """Increments number served"""
        self.number_served += number_increment
        print(f"\nThe number of additional guests served is: {number_increment}.")