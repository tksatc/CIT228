import random
problems = int(input("How many math problems would you like to practice? "))
counter = 0
numberCorrect = 0
run = True

while run and counter < problems:
    randNumber1 = random.randrange(1, 1000)
    randNumber2 = random.randrange(1, 1000)
    correctAnswer = int(randNumber1 - randNumber2)
    yourAnswer = int(input(f"What is the integer value of {randNumber1} - {randNumber2}? "))
    
    if correctAnswer == yourAnswer:
        print("Great job! Your answer is correct.")
        numberCorrect += 1
    else:
        print("Sorry, the correct answer is ", correctAnswer)
    counter +=1

    if counter < problems:
        playAgain = input("Would you like to continue practicing?  Enter 'q' to quit, or any key to continue: ")

        if playAgain.lower() == "q":
            run = False

print("You answered ",numberCorrect, " questions correctly!")
print("Thanks for playing!")
