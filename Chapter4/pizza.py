print("\n--------------------Exercise 4-1--------------------------")

pizzas = ["greek", "pepperoni, bacon, green olives", "chicken and bacon ranch"]

print("Pizzas I like\n")
for pizza in pizzas:
    print(pizza)

print("\nPizza is the best food!")

for pizza in pizzas:
    if pizza == "greek":
        print(f"\n{pizza.title()} is really good.")
    elif pizza == "pepperoni, bacon, green olives":
         print(f"{pizza.title()} is my favorite!")
    else:
         print(f"{pizza.title()} is awesome.\n")
