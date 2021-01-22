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

# Exercise 3 - manipulate a string
print("----------------------------------------")
print("Exercise 3")
author = "john muir"
noun = "mountains"
verb = "are calling"
ending = "I must go"
quote = "The " + noun + " " + verb + " and " + ending
print(quote)
print(author.upper())

# Exercise 4 - tabs and newlines
print("----------------------------------------")
print("Exercise 4\n")
print("Months\t\t\tDays")
print("\nJanuary\t\t\tSunday")
print("\nFebruary\t\tMonday")
print("\nMarch\t\t\tTuesday")
print("\nApril\t\t\tWednesday")
print("\nMay\t\t\tThursday")
print("\nJune\t\t\tFriday")
print("\nJuly\t\t\tSaturday")
print("\nAugust")
print("\nSeptember")
print("\nOctober")
print("\nNovember")
print("\nDecember\n")