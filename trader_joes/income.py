import csv
import matplotlib.pyplot as plt
import numpy as np

"""Charts median household incomes by county"""

filename = "trader_joes/data/household_income.csv"

market = ["grand traverse", "leelanau", "benzie", "wexford", "kalkaska", 
            "missaukee"]
xtra_market = ["charlevoix", "emmet", "crawford", "manistee"]

# Open csv
with open(filename) as inc:
    reader = csv.reader(inc)
    header_row = next(reader)
    state_total = next(reader)

    prime_counties, anc_counties = [], []
    prime_median, anc_median = [], []
    prime_mean, anc_mean = [], []

    # Extract counties, median, mean incomes
    for row in reader:
        county = row[0].lower()
        median = (row[1])
        mean = (row[2])
        
        # Separate prime market counties from ancillary market counties
            # Append to appropriate market list
        if county in market:
            prime_counties.append(county)
            prime_median.append(median)
            prime_mean.append(mean)
        elif county in xtra_market:
            anc_counties.append(county)
            anc_median.append(median)
            anc_mean.append(mean)

barWidth = 0.25
bar1 = np.arange(len(prime_counties))
bar2 = [x + barWidth for x in bar1]

plt.xticks([r + barWidth for r in range(len(prime_counties))], prime_counties)
plt.bar(bar1, prime_median, width=barWidth, label="Median Income")
plt.bar(bar2, prime_mean, width=barWidth, label="Mean Income")

plt.ylabel("Income")
plt.xlabel("County")
plt.title("Median & Mean Household Income\nPrime Market")
plt.legend(loc='best')
plt.xticks(rotation = 45)   # County labels shown diagonally

plt.show()
