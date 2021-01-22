# Hands-On 3

animals = ["horse", "cow", "goat", "pig", "chicken", "donkey"]
newAnimals = animals[:]
newAnimals.append("goose")
newAnimals.append("duck")
newAnimals.append("rabbit")
newAnimals.append("bull")

print("\n--------------Original List-------------")
for animal in animals:
    print(animal)

print("\n--------------New List-------------")
for newAnimal in newAnimals:
    print(newAnimal)

# Exercise 4-10

print("The first three items in the list are: ", newAnimals[:3])
print("Three items from the middle of the list are: ", newAnimals[3:6])
print("The last three items in the list are: ", newAnimals[7:])
