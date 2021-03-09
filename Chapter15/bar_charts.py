import matplotlib.pyplot as plt  
import numpy as np 

# percentage of fast food consumption per day by different sexes and age groups    
#https://www.cdc.gov/nchs/data/databriefs/db322_table.pdf#page=1

men = [37.9,46.5,37.6,25.6]
women = [35.4,43.3,37.8,22.7]
total=[36.6,44.9,37.7,24.1]
age_range=["Over 20","20-39","40-59","Over 60"]
barWidth = 0.25

bar1 = np.arange(len(age_range))
bar2 = [x + barWidth for x in bar1]
bar3 = [x + barWidth for x in bar2]

plt.xticks([r + barWidth for r in range(len(age_range))], age_range)

plt.bar(bar1, men, color='blue', width=barWidth, label="Men")
plt.bar(bar2, women, color='pink', width=barWidth, label="Women")
plt.bar(bar3, total, color='purple', width=barWidth, label="Average")

plt.ylabel("Percentages")
plt.xlabel("Age Range")
plt.title("Daily Fast Food Consumption", fontsize=18)
plt.legend(loc='best')

plt.show() 