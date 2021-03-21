"""Creates a horizontal bar graph to chart age groups by county"""

import csv
import matplotlib.pyplot as plt

filename = "trader_joes/data/customer_demog.csv"

market = ["grand traverse", "leelanau", "benzie", "wexford", "kalkaska", 
            "missaukee", "charlevoix", "emmet", "crawford", "manistee"]
# Open .csv
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    state_total = next(reader)  

    counties, counties_titles = [], []
    under18, age18_29, age30_39, age40_49 = [], [], [], []
    age50_59, age60_69, age70_79, age80_plus = [], [], [], []

    
    # Extract counties, populations
    for row in reader:
        county = row[6].lower()

        # Retrieve counties and populations, add to lists if in county list
        if county in market:        
            counties.append(row[6])
            counties_titles.append(row[6])
			
            under18.append(int(row[15]))
            age18_29.append(int(row[18]))
            age30_39.append(int(row[21]))
            age40_49.append(int(row[24]))
            age50_59.append(int(row[27]))
            age60_69.append(int(row[30]))
            age70_79.append(int(row[33]))
            age80_plus.append(int(row[36]))

# Calculate left margin for bar subsets
x2 = under18
x3 = list(map(lambda a,b: a+b, under18, age18_29))
x4 = list(map(lambda a,b,c: a+b+c, under18, age18_29, age30_39))
x5 = list(map(lambda a,b,c,d: a+b+c+d, under18, age18_29, age30_39, age40_49))
x6 = list(map(lambda a,b,c,d,e: a+b+c+d+e, under18, age18_29, age30_39, age40_49, 
                age50_59))
x7 = list(map(lambda a,b,c,d,e,f: a+b+c+d+e+f, under18, age18_29, age30_39, 
                age40_49, age50_59, age60_69))
x8 = list(map(lambda a,b,c,d,e,f,g: a+b+c+d+e+f+g, under18, age18_29, age30_39, 
                age40_49, age50_59, age60_69, age70_79))

# Design bar subsets
plt.barh(counties, under18, color='MediumAquamarine', label="Under 18")
plt.barh(counties, age18_29, left=x2, color='LemonChiffon', label="18 - 29")
plt.barh(counties, age30_39, left=x3, color='Thistle', label="30 - 39")
plt.barh(counties, age40_49, left=x4, color='Salmon', label="40 - 49")
plt.barh(counties, age50_59, left=x5, color='CadetBlue', label="50 - 59")
plt.barh(counties, age60_69, left=x6, color='SandyBrown', label="60 - 69")
plt.barh(counties, age70_79, left=x7, color='YellowGreen', label="70 - 79")
plt.barh(counties, age80_plus, left=x8, color='LightPink', label="80 & over")

plt.xlabel("Population")
plt.ylabel("County")
plt.title("County Populations by Age Group", fontsize=18)
plt.legend(loc='upper right', title="Age Groups")

plt.show()
