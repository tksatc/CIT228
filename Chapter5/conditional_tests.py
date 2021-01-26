print("-------------------Hands-On 1---------------------------")

cities = ["traverse city", "cadillac", "petoskey", "glen arbor"]
pet = "Sophie"

print("\n=============True Results==============")
if "Traverse City" == "Traverse City":
    print("Traverse City == Traverse City True")
else:
    print("Traverse City == Traverse City False")

if 33 > 15:
    print("33 > 15 True")
else:
    print("33 > 15 False")

if 44 != 22:
    print("44 != 22 True")
else:
    print("44 != 22 False")

if "Lemon" == "Lemon":
    print("Lemon == Lemon True")
else:
    print("Lemon == Lemon False")

if "cadillac" in cities:
    print("cadillac is in the cities list? True")
else:
    print("cadillac is in the cities list? False")

if pet.lower() == "sophie" and "petoskey" in cities:
    print("sophie is the lower case of Sophie and petoskey is in the cities list? True")
else:
        print("sophie is the lower case of Sophie and petoskey is in the cities list? False")
 
if 12 <= 30 or 21 > 28:
    print("12 <= 30 or 21 > 28? True")
else:
    print("12 <= 30 or 21 > 28? False")

print("\n=============False Results==============")

if "glen arbor" not in cities:
    print("glen arbor not in cities list? True")
else:
    print("glen arbor not in cities list? False")

if 100 == 101:
    print("100 == 101 True")
else:
    print("100 == 101 False")

if "Lemon" == "lemon":
    print("Lemon == lemon True")
else:
    print("Lemon == lemon False")

if 32 < 28:
    print("32 < 28 True")
else:
    print("32 < 28 False")

if "suttons bay" in cities:
    print("suttons bay in cities list? True")
else:
    print("suttons bay in cities list? False")
