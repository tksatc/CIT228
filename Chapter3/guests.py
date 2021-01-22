print("\n---------------------Exercise 3-4---------------------------------")

guests = ["thomas jefferson", "mei ling ellis", "declan wynne"]
invite1 = f"{guests[0].title()}, are you able to come to dinner tomorrow?"
invite2 = f"{guests[1].title()}, are you able to come to dinner tomorrow?"
invite3 = f"{guests[2].title()}, are you able to come to dinner tomorrow?"
print(invite1)
print(invite2)
print(invite3)

print("\n---------------------Exercise 3-5---------------------------------")

print(f"{guests[0].title()}, we'll miss you tomorrow night!")

guests[0] = "aretha franklin"
invite1 = f"{guests[0].title()}, are you able to come to dinner tomorrow?"
invite2 = f"{guests[1].title()}, are you able to come to dinner tomorrow?"
invite3 = f"{guests[2].title()}, are you able to come to dinner tomorrow?"
print(invite1)
print(invite2)
print(invite3)

print("\n---------------------Exercise 3-6 & 3-9--------------------------------")

print("I found a bigger dining table!")

guests.insert(0, "amanda hoffman")
guests.insert(2, "dave anderson")
guests.append("randy burgess")
invite1 = f"{guests[0].title()}, are you able to come to dinner tomorrow?"
invite2 = f"{guests[1].title()}, are you able to come to dinner tomorrow?"
invite3 = f"{guests[2].title()}, are you able to come to dinner tomorrow?"
invite4 = f"{guests[3].title()}, are you able to come to dinner tomorrow?"
invite5 = f"{guests[4].title()}, are you able to come to dinner tomorrow?"
invite6 = f"{guests[5].title()}, are you able to come to dinner tomorrow?"

print(len(guests), " guests are invited to dinner tomorrow.")

print(invite1)
print(invite2)
print(invite3)
print(invite4)
print(invite5)
print(invite6)

print("\n---------------------Exercise 3-7---------------------------------")

print("My new table won't be here in time and I can only invite 2 people for dinner.")
poppedGuest = guests.pop()
print(poppedGuest.title(), ", I'm so sorry, I cannot have you for dinner tomorrow.")
poppedGuest = guests.pop()
print(poppedGuest.title(), ", I'm so sorry, I cannot have you for dinner tomorrow.")
poppedGuest = guests.pop()
print(poppedGuest.title(), ", I'm so sorry, I cannot have you for dinner tomorrow.")
poppedGuest = guests.pop()
print(poppedGuest.title(), ", I'm so sorry, I cannot have you for dinner tomorrow.")

print(invite1)
print(invite2)

del guests[0]
del guests[0]

print("Guest list: ", guests)
