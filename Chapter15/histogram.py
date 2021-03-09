import matplotlib.pyplot as plt

#scores showing how many yards students ran in 12 minutes
# 1 mile = 1,760 yards
fitness_test=[2901,1760,3000,2824,3235,2050,2265,2500,2400,2625,3550,1850,1890,3200,2900,2975,3000,2220,2250]
miles = []

for run in fitness_test:
    whole = run / 1760
    dec = run % 1760
    mileage = f"{whole}.{dec}"
    mileage = float("{:.3}".format(mileage))
    
    miles.append(mileage)

plt.hist(miles, bins=9, color='green')
plt.xlabel("Miles")
plt.ylabel("Frequency")

plt.suptitle("Distance Distribution of 12-Minute Runs")

plt.show()

