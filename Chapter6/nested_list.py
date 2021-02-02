destinations = {
    "arizona" : "grand canyon",
    "utah" : ["zion national park", "arches national park", "salt flats"],
    "alaska" : "denali",
    "colorado" : "ouray",
}

print("\nDictionary entries: ", destinations)
print("\n**********Bucket List Travel***********")

for state, location in destinations.items():
    if type(location) == list:
        print(f"\nIn {state.title()}, visit: \t")
        for l in location:
            print("\t", l.title())
    else:
        print(f"\nIn {state.title()}, visit: {location.title()}\n")
    
