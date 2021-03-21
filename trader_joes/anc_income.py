"""Charts ancillary market median household incomes by county"""

import csv
import matplotlib.pyplot as plt
import numpy as np

filename = "trader_joes/data/household_income.csv"

xtra_market = ["charlevoix", "emmet", "crawford", "manistee"]

# Open csv
with open(filename) as inc:
    reader = csv.reader(inc)
    header_row = next(reader)
    state_total = next(reader)

    anc_counties, anc_titles = [], []
    anc_median, anc_mean = [], []

    # Extract counties, median, mean incomes
    for row in reader:
        county = row[0].lower()
        median = int((row[1]))
        mean = int((row[2]))
        
        # Separate prime market counties from ancillary market counties
            # Append to appropriate market list
        if county in xtra_market:
            anc_counties.append(county)
            anc_titles.append(county.title())           # to display counties in title case
            anc_median.append(median)
            anc_mean.append(mean)

barWidth = 0.25
bar1 = np.arange(len(anc_counties))
bar2 = [x + barWidth for x in bar1]

plt.xticks([r + barWidth for r in range(len(anc_titles))], anc_titles)
plt.bar(bar1, anc_median, width=barWidth, color="gold", label="Median Income")
plt.bar(bar2, anc_mean, width=barWidth, color='olivedrab', label="Mean Income")

plt.ylabel("Income")
plt.xlabel("County")
plt.title("Median & Mean Household Income\nPrime Market", fontsize=16)
plt.legend(loc='best')
plt.xticks(rotation = 45)   # County labels shown diagonally

plt.savefig("ancillary_income.png")

plt.show()
