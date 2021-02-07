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

restaurant1 = Restaurant("thud suan", "thai")

print("\n-----------Initial State with initial number of guests served------------")
restaurant1.open_restaurant()
restaurant1.describe_restaurant()

restaurant1.number_served = 12

print("\n---------Directly Updated number of guests served----------")
print(f"{restaurant1.restaurant_name.title()} has now served {restaurant1.number_served} people.")

print("\n---------------Update Using Setter-----------------------")

restaurant1.set_number_served(43)
print(f"{restaurant1. restaurant_name.title()} has served {restaurant1.number_served} guests as of today.")

print("\n----------------------Using Increment Method----------------------")

restaurant1.increment_number_served(52)

print(f"The total number of guests served is: {restaurant1.number_served}.")