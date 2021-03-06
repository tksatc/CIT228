"""Create subplots and chart populations in primary and ancillary markets"""

import csv
import matplotlib.pyplot as plt
import numpy as np

filename = "trader_joes/data/customer_demog.csv"
market = ["grand traverse", "leelanau", "benzie", "wexford", "kalkaska", 
            "missaukee"]
xtra_market = ["charlevoix", "emmet", "crawford", "manistee"]
 
# Open .csv file
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    state_total = next(reader)

    prime_counties, anc_counties = [], []
    prime_pops, anc_pops = [], []
    prime_titles, anc_titles = [], []

    # Extract counties, populations, median incomes
    for row in reader:
        county = row[6].lower()
        population = int(row[8])
        
        # Separate prime market counties from ancillary market counties
            # Append to appropriate market list
        if county in market:
            prime_counties.append(county)
            prime_titles.append(county.title())     # Title case for chart display
            prime_pops.append(population)
        elif county in xtra_market:
            anc_counties.append(county)
            anc_titles.append(county.title())       # Title case for chart display
            anc_pops.append(population)

# Plot setup for prime market counties
ax1 = plt.subplot(1, 2, 1)
ax1.bar(prime_titles, prime_pops, color='seagreen', label="County")

plt.ylabel("Population")
plt.xlabel("County")
plt.title("Population by County in Primary Market", fontsize=14)
plt.xticks(rotation = 45)

# Plot setup for ancillary market counties
ax2 = plt.subplot(1, 2, 2)
ax2.bar(anc_titles, anc_pops, color='darkorange', label="County")

plt.ylabel("Population")
plt.xlabel("County")
plt.title("Population by County in Ancillary Market", fontsize=14)
plt.xticks(rotation = 45)
plt.suptitle("Routine Consumer Markets", fontsize=16)
plt.subplots_adjust(top=.9, wspace=.5)

plt.savefig("market_population.png")

plt.show()