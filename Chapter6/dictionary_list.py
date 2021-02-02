desserts = {
    "ice cream" : "vanilla bean",
    "brownie" : "double fudge",
    "cheesecake" : "irish cream",
}

entrees = {
    "pork" : "tenderloin",
    "chicken" : "boneless skinless breast",
    "beef" : "chuck roast",
    "fish" : "cod",
}

sides = {
    "veg" : "kohlrabi",
    "salad" : "tossed",
    "pasta" : "greek",
}

meals = [entrees, sides, desserts]

print("\n")
for course in meals:
    print(course)
