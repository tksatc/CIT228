prompt = input("Enter a number: ")
number = int(prompt)

if number % 10 == 0:
    print(prompt, " is a multiple of 10.")
else:
    print(prompt, " is not a multiple of 10.")
