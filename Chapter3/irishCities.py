print(f"\n-------------------------------Exercise 3-10----------------------------------")

irishCities = ["dublin", "galway", "waterford", "belfast", "kilkenny", "tralee", "sligo", "londonderry", "wexford", "cork", "limerick"]
print("Original list: ", irishCities)

irishCities.insert(5, "castlebar")
irishCities.append("ballymena")
print("List after additions: ", irishCities)

tempSort = sorted(irishCities)
print("Temporary sorted list: ", tempSort)

irishCities.reverse()
print("Reverse-sort list: ", irishCities)

irishCities.sort()
print("Sorted list: ", irishCities)

del irishCities[5]
irishCities.pop()
irishCities.remove("dublin")
print("List after deletions: ", irishCities)

print(f"There are {len(irishCities)} in the final list.")