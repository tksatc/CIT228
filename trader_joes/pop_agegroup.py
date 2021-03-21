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
    under18, age18, age25, age30, age35 = [], [], [], [], []
    age40, age45, age50, age55, age60 = [], [], [], [], []
    age65, age70, age75, age80, age85 = [], [], [], [], []

    # Extract data, append to lists if county in market list
    for row in reader:
        county = row[6].lower()

        if county in market:        
            counties.append(row[6])
            counties_titles.append(row[6])
            under18.append(int(row[15]))
            age18.append(int(row[16]))
            age25.append(int(row[17]))
            age30.append(int(row[18]))
            age35.append(int(row[19]))
            age40.append(int(row[20]))
            age45.append(int(row[21]))
            age50.append(int(row[22]))
            age55.append(int(row[23]))
            age60.append(int(row[24]))
            age65.append(int(row[25]))
            age70.append(int(row[26]))
            age75.append(int(row[27]))
            age80.append(int(row[28]))
            age85.append(int(row[29]))

# Calculate left margin for bar subsets
x2 = under18
x3 = list(map(lambda a,b: a+b, under18, age18))
x4 = list(map(lambda a,b,c: a+b+c, under18, age18, age25))
x5 = list(map(lambda a,b,c,d: a+b+c+d, under18, age18, age25, age30))
x6 = list(map(lambda a,b,c,d,e: a+b+c+d+e, under18, age18, age25, age30, 
                age35))
x7 = list(map(lambda a,b,c,d,e,f: a+b+c+d+e+f, under18, age18, age25, 
                age30, age35, age40))
x8 = list(map(lambda a,b,c,d,e,f,g: a+b+c+d+e+f+g, under18, age18, age25, 
                age30, age35, age40, age45))
x9 = list(map(lambda a,b,c,d,e,f,g,h: a+b+c+d+e+f+g+h, under18, age18, age25, 
                age30, age35, age40, age45, age50))
x10 = list(map(lambda a,b,c,d,e,f,g,h,i: a+b+c+d+e+f+g+h+i, under18, age18, 
                age25, age30, age35, age40, age45, age50, age55))
x11 = list(map(lambda a,b,c,d,e,f,g,h,i,j: a+b+c+d+e+f+g+h+i+j, under18, age18,
                age25, age30, age35, age40, age45, age50, age55, age60))
x12 = list(map(lambda a,b,c,d,e,f,g,h,i,j,k: a+b+c+d+e+f+g+h+i+j+k, under18, 
                age18, age25, age30, age35, age40, age45, age50, age55, age60, 
                age65))
x13 = list(map(lambda a,b,c,d,e,f,g,h,i,j,k,l: a+b+c+d+e+f+g+h+i+j+k+l, 
                under18, age18, age25, age30, age35, age40, age45, age50, age55, 
                age60, age65, age70))
x14 = list(map(lambda a,b,c,d,e,f,g,h,i,j,k,l,m: a+b+c+d+e+f+g+h+i+j+k+l+m, 
                under18, age18, age25, age30, age35, age40, age45, age50, age55, 
                age60, age65, age70, age75))
x15 = list(map(lambda a,b,c,d,e,f,g,h,i,j,k,l,m,n: a+b+c+d+e+f+g+h+i+j+k+l+m+n,
                under18, age18, age25, age30, age35, age40, age45, age50, age55, 
                age60, age65, age70, age75, age80))


# Design bars
plt.barh(counties, under18, color='MediumAquamarine', label="Under 18")
plt.barh(counties, age18, left=x2, color='LemonChiffon', label="18 - 24")
plt.barh(counties, age25, left=x3, color='Thistle', label="25 - 29")
plt.barh(counties, age30, left=x4, color='Salmon', label="30 - 34")
plt.barh(counties, age35, left=x5, color='CadetBlue', label="35 - 39")
plt.barh(counties, age40, left=x6, color='SandyBrown', label="40 - 44")
plt.barh(counties, age45, left=x7, color='YellowGreen', label="45 - 49")
plt.barh(counties, age50, left=x8, color='LightPink', label="50 - 54")
plt.barh(counties, age55, left=x9, color='LightGray', label="55 - 59")
plt.barh(counties, age60, left=x10, color='Plum', label="60 - 64")
plt.barh(counties, age65, left=x11, color='PowderBlue', label="65 - 69")
plt.barh(counties, age70, left=x12, color='Khaki', label="70 - 74")
plt.barh(counties, age75, left=x13, color='Coral', label="75 - 79")
plt.barh(counties, age80, left=x14, color='Silver', label="80 - 84")
plt.barh(counties, age85, left=x15, color='LightSkyBlue', label="85 and Over")

plt.xlabel("Population")
plt.ylabel("County")
plt.title("County Populations by Age Group")
plt.legend(loc='upper right')

plt.show()
