transportModes = {
    "car" : {
        "make" : "nissan",
        "model" : "altima",
    },

    "truck" : {
        "make" : "toyota",
        "model" : "tundra",
    },
    
    "bike" : {
        "make" : "schwinn",
        "model" : "ten speed",
    },

}

print("\n---------Modes of Transportation----------")

for mode, detail in transportModes.items():
    print(f"\nMode: {mode.title()}")

    make = detail["make"]
    model = detail["model"]

    print(f"\tMake: {make.title()}")
    print(f"\tModel: {model.title()}")
