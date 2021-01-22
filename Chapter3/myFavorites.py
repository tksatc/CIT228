#Hands-on 1, 2
print("---------------------------------------Hands on 1--------------------------------------------------")

favoriteFoods = ["greek salad", "cuban pork", "pineapple fried rice", "tacos", "dill pickle soup", "lasagna"]
print("Favorite Foods: ", favoriteFoods)

favoriteNumbers = [3, 23, 12, 7, 29, 43]
print("Favorite Numbers: ", favoriteNumbers)

favoriteMovies = ["christmas vacation", "the princess bride", "the king's speech"]
print("Favorite Movies: ", favoriteMovies)

favorites = [favoriteFoods[1], favoriteFoods[2], favoriteNumbers[0], favoriteNumbers[4], favoriteMovies[0].title(), favoriteMovies[1].title()]
print("Favorites: ", favorites)

print("Last food item: ", favoriteFoods[-1])

numMessage = f"2nd, 4th, and 6th numbers = {favoriteNumbers[1]} {favoriteNumbers[3]} {favoriteNumbers[5]}"
print(numMessage)

print(f"All movies: {favoriteMovies[0]} {favoriteMovies[1]} {favoriteMovies[2]}")
print(f"First food, first number, and first movie: {favoriteFoods[0]} {favoriteNumbers[0]} {favoriteMovies[0].title()}")

print("\n---------------------------------------Hands on 2--------------------------------------------------")

favoriteMovies.append("the holiday")
print("Added movie: ", favoriteMovies)

favoriteNumbers.insert(3, 102)
print("Added number at sub 3: ", favoriteNumbers)

favoriteFoods.insert(5, "chili")
print("Added food at sub 5: ", favoriteFoods)

del (favoriteFoods[0])
print("Deleted food [0]: ", favoriteFoods)

favoriteNumbers.pop(3)
print("Deleted number at sub 3: ", favoriteNumbers)

favoriteNumbers.pop(1)
print("Deleted number at sub 2: ", favoriteNumbers)

print("\n---------------------------------------Hands on 3--------------------------------------------------")

favoriteMovies.sort()
print("Sorted list: ", favoriteMovies)

favoriteFoods.sort()
print("Sorted list: ", favoriteFoods)

sorted(favoriteNumbers)
print("Temp sorted list: ", favoriteNumbers)
print("Unsorted list: ", favoriteNumbers)

favoriteMovies.reverse()
print("Sorted in reverse: ", favoriteMovies)

