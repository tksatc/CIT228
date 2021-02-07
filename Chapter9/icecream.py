from restaurant import Restaurant

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