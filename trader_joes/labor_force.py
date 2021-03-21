"""Creates a chart showing labor force in the prime market"""

import csv
import matplotlib.pyplot as plt

filename = "trader_joes/data/labor_force.csv"

market = ["grand traverse", "leelanau", "benzie", "wexford", "kalkaska", 
            "missaukee"]

with open(filename) as f:
    
    # Open csv
    reader = csv.reader(f)
    header_row = next(reader)
    state_total = next(reader)

    counties, counties_titles, force, avail_labor = [], [], [], []

    # Extract counties and labor force numbers
    for row in reader:
        counties.append(row[0].lower())
        counties_titles.append(row[0].title())
        force.append(int(row[1]))
        avail_labor.append(int(row[3]))

plt.bar(counties_titles, force, color="maroon", label="Labor")
plt.bar(counties_titles, avail_labor, bottom=force, color="cadetblue", label="Unemployed")

plt.xlabel("County")
plt.ylabel("Population")
plt.title("Labor Force", fontsize=18)
plt.legend(loc='best')

plt.show()
