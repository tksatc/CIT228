rivers = {
    "missouri" : "the united states",
    "tigris" : ["iran", "iraq", "turkey", "syria"],
    "euphrates" : ["iraq", "syria", "turkey"],
    "nile" : "egypt",
}

print("\nRivers and Countries")
print("----------------------------------------------------------------")

for river, countries in rivers.items():
    if type(countries) == list:
        print(f"The {river.title()} River flows through: ")
        for c in countries:
            print("\t", c.title())
    else:
        print(f"The {river.title()} River flows through: \n\t{countries.title()}")

print("\nRivers")
print("----------------------------------------------------------------")

for river in rivers:
    print(river.title())

print("\nCountries")
print("----------------------------------------------------------------")

for river, countries in rivers.items():
    print(countries)
