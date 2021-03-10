import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = "Chapter16/data/seattle_temps_2020.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, and high and low temperatures from this file
    dates, highs, lows  = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m")
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

    # Plot the high and low temperatures
    plt.style.use("seaborn-dark-palette")
    fig, ax = plt.subplots()
    ax.plot(dates, highs, marker='^', c="red", alpha=0.5)
    ax.plot(dates, lows, marker='v', c="blue", alpha=0.5)
    #ax.fill_between(dates, highs, lows, facecolor="blue", alpha=0.1)

    # Format plot
    title = "Monthly high and low temperatures - 2020\nSeattle, WA"
    ax.set_title(title, fontsize=16)
    ax.set_xlabel("", fontsize=14)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature (F)", fontsize=14)
    ax.tick_params(axis="both", which="major", labelsize=14)

    plt.show()

"""
#print(highs)
        
for index, column_header in enumerate(header_row):
    print(index, column_header)
"""