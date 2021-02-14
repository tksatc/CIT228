response = input("\nWould you like me to add numbers for you?  Press 'q' to quit, any other key to play: ")

while response != "q":
    firstNumber = input("Enter your first number: ")
    if firstNumber == "q":
        print("Play again soon!")
        break
    secondNumber = input("Enter your second number: ")
    if secondNumber == "q":
        print("Play again soon!")
        break
    
    try:
        answer = int(firstNumber) + int(secondNumber)
    except ValueError:
        print("Oops!  You entered text instead of a number.  Try again. ")
    else:
        print(f"{firstNumber} + {secondNumber} = {answer}.")
        playAgain = input("Would you like to see more? Press 'q' to quit, any other key to continue: ")

        if playAgain == "q":
            print("See you next time!")
            break

