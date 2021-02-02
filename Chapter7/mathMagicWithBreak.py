import random
problems = int(input("How many math problems would you like to practice? "))
counter = 0
numberCorrect = 0
numberIncorrect = 0

while counter < 11 and counter < problems:
    randNumber1 = random.randrange(1, 1000)
    randNumber2 = random.randrange(1, 1000)
    correctAnswer = int(randNumber1 - randNumber2)
    yourAnswer = int(input(f"\nWhat is the integer value of {randNumber1} - {randNumber2}? "))
    
    if correctAnswer == yourAnswer:
        print("Great job! Your answer is correct.")
        numberCorrect += 1
    else:
        print("Sorry, the correct answer is ", correctAnswer)
        numberIncorrect += 1
        if numberIncorrect > 5:
            print("You might want to talk to a tutor for some help.")
            break

    counter +=1

print("You answered ", numberCorrect, " questions correctly!")



print("Thanks for playing!")
