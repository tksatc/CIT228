"""Charts median household incomes by county"""


import csv
import matplotlib.pyplot as plt
import numpy as np

filename = "trader_joes/data/household_income.csv"

market = ["grand traverse", "leelanau", "benzie", "wexford", "kalkaska", 
            "missaukee"]

# Open csv
with open(filename) as inc:
    reader = csv.reader(inc)
    header_row = next(reader)
    state_total = next(reader)

    prime_counties, prime_titles = [], []
    prime_median, prime_mean = [], []

    # Extract counties, median, mean incomes
    for row in reader:
        county = row[0].lower()
        median = int((row[1]))
        mean = int((row[2]))
        
        # Separate prime market counties from ancillary market counties
            # Append to appropriate market list
        if county in market:
            prime_counties.append(county)
            prime_titles.append(county.title())         # to display counties in title case
            prime_median.append(median)
            prime_mean.append(mean)

barWidth = 0.25
bar1 = np.arange(len(prime_counties))
bar2 = [x + barWidth for x in bar1]

plt.xticks([r + barWidth for r in range(len(prime_median))], prime_titles)
plt.bar(bar1, prime_median, width=barWidth, color="darkorange", label="Median Income")
plt.bar(bar2, prime_mean, width=barWidth, color='darkgreen', label="Mean Income")

plt.ylabel("Income")
plt.xlabel("County")
plt.title("Median & Mean Household Income\nPrime Market", fontsize=16)
plt.legend(loc='best')
plt.xticks(rotation = 45)   # County labels shown diagonally

plt.savefig("prime_income.png")

plt.show()
