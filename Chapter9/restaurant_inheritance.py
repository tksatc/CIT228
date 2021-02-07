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

class IceCreamStand(Restaurant):
    """Repreents ice cream stands as a type (child) of restaurants"""
    def __init__(self, restaurant_name, cuisine_type, flavors, number_served=0):
        super().__init__(restaurant_name, cuisine_type, number_served=0)
        self.flavors = [flavors]
    
    # Created to test addition of new flavors
    def add_flavor(self, flavor):
        """Adds a flavor to the flavors list"""
        self.flavor = self.flavors.append(flavor)
    
    def display_flavors(self):
        """Displays list of flavors"""
        print("\n------Ice Cream Flavors------")
        for flavor in self.flavors:
            print(flavor.title())

    
iceCreamStand1 = IceCreamStand("eddie's", "ice cream", "vanilla")
iceCreamStand1.display_flavors()


# Included to test functionality of list
#iceCreamStand1.add_flavor("chocolate")
#iceCreamStand1.display_flavors()

#iceCreamStand1.describe_restaurant()

