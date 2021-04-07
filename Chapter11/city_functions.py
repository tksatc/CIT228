def city_country(city, country, population=""):
    """Displays a formatted city and country string"""

    if population:
        cityCountry = f"{city}, {country} - population: {population}"
    else:
        cityCountry = f"{city}, {country}"
    
    return cityCountry.title()

"""  FOR TESTING PURPOSES ONLY - DELETE BEFORE SUBMISSION
newCity = "new york"
newCountry = "united states"
newPop = "2000000"


print("\n", city_country(newCity, newCountry, newPop))
"""