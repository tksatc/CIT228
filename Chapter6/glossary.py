words = {
    "input()": "a function that pauses a program to wait for user input",
    "set": "a collection in which each item must be unique",
    "list": "a collection of items in a particular order",
    "rstrip()": "a function that temporarily removes white space on the right side",
    "import": "key word that imports other libraries into Python",
    "int": "a data type that for numbers",
    "in": "a boolean keyword to check if an item exists in a collection",
    "len()": "a function that calculates the number of items in a collection",
    "reverse()": "a function that reverses the order of a collection by the index",
    "type()": "a function that returns the data type of a variable",
}

print("\nGlossary Entries")
print("------------------")

for key, value in words.items():
    print(f"\n{key}: ")
    print(f"\t {value}")
