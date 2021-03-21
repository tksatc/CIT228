import csv
import matplotlib.pyplot as plt

filename = "trader_joes/data/education.csv"
market = ["grand traverse", "leelanau", "benzie", "wexford", "kalkaska", 
            "missaukee"]
xtra_market = ["charlevoix", "emmet", "crawford", "manistee"]

# Open csv
with open(filename) as edu:
    reader = csv.reader(edu)
    header_row = next(reader)
    state_total = next(reader)

    # Extract counties and education levels
    prime_counties, anc_counties = [], []
    prime_adult_pop, anc_adult_pop = [], []
    prime_high, anc_high = [], []
    prime_someC, anc_someC = [], []
    prime_assoc, anc_assoc = [], []
    prime_bach, anc_bach = [], []
    prime_grad, anc_grad = [], []
        
    for row in reader:
        county = row[0].lower()
        adult_pop = int(row[1])
        hs = int(row[2])
        coll = int(row[3])
        assoc = int(row[4])
        bach = int(row[5])
        grad = int(row[6])
        
        # Separate prime market counties from ancillary market counties
            # Append to appropriate market list
        if county in market:
            prime_counties.append(county)
            prime_adult_pop.append(adult_pop)
            prime_high.append(hs)
            prime_someC.append(coll)
            prime_assoc.append(assoc)
            prime_bach.append(bach)
            prime_grad.append(grad)
        elif county in xtra_market:
            anc_counties.append(county)
            anc_adult_pop.append(adult_pop)
            anc_high.append(hs)
            anc_someC.append(coll)
            anc_assoc.append(assoc)
            anc_bach.append(bach)
            anc_grad.append(grad)

labels = ["High School/Equivalent", "Some College", "Associate's", "Bachelor's",
            "Graduate/Professional"]
prime_totals, anc_totals = [], []

prime_totals.append(sum(prime_high))
prime_totals.append(sum(prime_someC))
prime_totals.append(sum(prime_assoc))
prime_totals.append(sum(prime_bach))
prime_totals.append(sum(prime_grad))

anc_totals.append(sum(anc_high))
anc_totals.append(sum(anc_someC))
anc_totals.append(sum(anc_assoc))
anc_totals.append(sum(anc_bach))
anc_totals.append(sum(anc_grad))


fig1, ax1 = plt.subplots()
ax1.pie(prime_totals, labels=labels, autopct='%3.1f%%')
ax1.axis('equal')
plt.title("Education Levels - Primary Market\n25 Years of Age and Over")

fig2, ax2 = plt.subplots()
ax2.pie(anc_totals, labels=labels, autopct='%3.1f%%')
ax2.axis('equal')
plt.title("Education Levels - Ancillary Market\n25 Years of Age and Over")

plt.show()
