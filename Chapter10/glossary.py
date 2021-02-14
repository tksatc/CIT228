import json

def writeToFile(fileObject):      
    """Stores data in a JSON file"""
    replace = input("This action will overwrite any existing data in the file.  Proceed?  'q' to quit, "
        "any other key to continue.")
    if replace != "q":
        try:
            with open(filename, "w") as f:
                json.dump(fileObject, f)
        except IOError:
            pass
        else:
            print(f"{filename} has been created.")

def readFile():     
    """Loads information from JSON file"""
    try:
        with open(filename) as f:
            glossary = json.load(f)
    except FileNotFoundError:
        print(f"{filename} was not found.  Please make another choice. ")
    else:
        for key, value in glossary.items():
            print("\n", key, " is: ", value)

def addToFile(new_entry):        
    """Adds items to JSON file"""
    try:
        with open(filename, "r+") as f:
            glossary = json.load(f)
            glossary.update(new_entry)
            f.seek(0)
            json.dump(glossary, f)           
    except IOError:
        print(f"There was a problem accessing the {f} file.")
    else:
        print(f"New entry has been added to {filename}.")

def getKey():
    """Getter to retrieve index"""
    term = input("Enter the term: ").split()[0]
    term = term.lower()
    return term

def getvalue():
    """Getter to retrieve value"""
    definition = input("Enter the definition: ").lower()
    return definition

def useMenu():          
    """Let's a user choose an action"""
    choice = int(input("\nEnter the number for the action you wish to take: \n"
            "1 - Create a file\n"
            "2 - Read the contents of a file\n"
            "3 - Add an entry to a file\n"
            "4 - Quit\n"))
    
    while choice != 1 and choice != 2 and choice != 3 and choice != 4:
        print("\nYou didn't enter a valid choice. Please try again.")
        choice = int(input("\nEnter the number for the action you wish to take: \n"
            "1 - Create a file\n"
            "2 - Read the contents of a file\n"
            "3 - Add an entry to a file\n"
            "4 - Quit\n"))
    return choice

entries = {
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

filename = "Chapter10/glossary.json"

option = useMenu()
while option != 4:
    if option == 1:
        writeToFile(entries)
    elif option == 2:
        readFile()
    elif option == 3:
        term = getKey()
        definition = getvalue()
        newEntry = {term:definition}
        addToFile(newEntry)
    else:
        print("Please choose from the available options.")
    option = useMenu()

# Chapter 6 code
#print("\nGlossary Entries")
#print("------------------")

#for key, value in entries.items():
    #print(f"\n{key}: ")
    #print(f"\t {value}")

#filename = "Chapter10/glossary"
