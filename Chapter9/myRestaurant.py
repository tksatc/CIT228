from restaurant import Restaurant
from icecream import IceCreamStand

iceCreamStand1 = IceCreamStand("eddie's", "ice cream", "vanilla")
iceCreamStand1.display_flavors()


#Included to test functionality of list
iceCreamStand1.add_flavor("chocolate")
iceCreamStand1.display_flavors()

iceCreamStand1.describe_restaurant()
