# Exercise 1 - name
print("----------------------------------------")
print("Exercise 1")
name = "tonya starlin"
print(name.title())
print(name.upper())
print(name.lower())
print("My first initial is: ", name[0].upper())

# Exercise 2 - sentence formatting
print("----------------------------------------")
print("Exercise 2")
noun = "monkey"
adj = "hungry"
verb = "ate"
ending = "all the bananas"
sentence1 = "the " + adj + " little " + noun + " " + verb + " " + ending
sentence2 = f"the {adj} little {noun} {verb} {ending}"
print(sentence1.upper())
print(sentence2.lower())