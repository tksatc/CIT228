print("\n--------------Exercise 9-1----------------")

class Restaurant:
    """A simple attempt to represent a restaurant"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initializes restaurant attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Prints restaurant descriptors"""
        print(f"{self.restaurant_name.title()} serves {self.cuisine_type.title()} food.")
        
    def open_restaurant(self):
        """Announces restaurant's opening"""
        print(f"{self.restaurant_name.title()} is now open!")

restaurant = Restaurant("agave", "mexican")

print(f"Restaurant: {restaurant.restaurant_name.title()}")
print(f"Cuisine: {restaurant.cuisine_type.title()}")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print("\n--------------Exercise 9-2----------------")

restaurant1 = Restaurant("opa", "greek")
restaurant2 = Restaurant("a taste of india", "indian")
restaurant3 = Restaurant("bubba's", "american")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
