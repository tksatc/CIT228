import os
import random

"""
filename = "Chapter10/guest.txt"

try:
    with open(filename, "w") as textFile:
        guestName = input("Please enter your name: ").lower()
        textFile.write(guestName)
        print(f"Thank you, {guestName.title()}.")
except IOError:
    print("There was a problem working with the file.")
"""

filename = "Chapter10/guest_book.txt"

# Checks for existing file, deletes if found
if os.path.exists(filename):
    os.remove(filename)

# Creates empty list to store room numbers
roomNumbers = []

# Attempts to accept user input to create a reservation & writes the reservation to a file
try:
    with open(filename, "w") as guestBook:
        guest = input("Please enter your name to book a room (press 'q' to quit): ").lower()

        while guest != "q":
            roomNumber = random.randint(1, 50)
            while roomNumber in roomNumbers:
                roomNumber = random.randint(1, 50)
            print(f"{guest.title()}, your room number is: {roomNumber}.")
            roomNumbers.append(roomNumber)
            guest += ", room # " + str(roomNumber) + "\n"
            guestBook.write(guest)
            #print(guest)
            guest = input("Please enter your name to book a room (press 'q' to quit): ").lower()

# Catches file exceptions
except IOError:
   print("There was a problem writing to the file.")

# Attempts to read from a file to display full reservation list
try:
    with open(filename) as guestBook:
        print("\n-----------------Room Assignments----------------------")
        for guest in guestBook:
            print(guest.title())
        print("\n----------------Guest Bookings--------------------")

# Catches exception
except FileNotFoundError:
    print(f"Unable to find the {filename} file.")