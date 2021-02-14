filename = 'Chapter10/learning_python.txt'

# Exercise 10-1, Read()
try:
    with open(filename) as textFile:
        contents = textFile.read()
except FileNotFoundError:
    print(f"{filename} was not found")
else:
    print("\n-------------Read() Output---------------")
    print(contents.strip())

# Exercise 10-1, Loop
try:
    with open(filename) as textFile:
        print("\n--------------For Loop Output----------------")
        for line in textFile:
            print(line.strip())
except FileNotFoundError:
    print(f"{filename} was not found")

# Exercise 10-1, List
try:
    with open(filename) as textFile:
        myLines = textFile.readlines()
        print("\n-------------Output from List----------------")
except FileNotFoundError:
    print(f"{filename} was not found")
else:
    for line in myLines:
        print(line.strip())

# Exercise 10-2
try:
    with open(filename) as textFile:
        print("\n--------------Replacing Text------------------")
        for line in textFile:
            print("\nOriginal: ", line.strip())
            print("Modified: ", line.replace("Python", "Java").strip())
except FileNotFoundError:
        print(f"{filename} was not found")   
