prompt = input("\nHow many people are in your group? ")
groupSize = int(prompt)
if groupSize > 8:
    print("You'll have to wait a bit for a table.")
else:
    print("Your table is ready.")