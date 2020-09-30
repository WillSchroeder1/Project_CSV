import csv
from datetime import datetime

open_death = open("death_valley_2018_simple.csv", "r")   
open_sitka = open("sitka_weather_2018_simple.csv", "r") 

csv_death = csv.reader(open_death, delimiter=",")
csv_sitka = csv.reader(open_sitka, delimiter=",")

header_row = next (csv_death)
header_row = next (csv_sitka)
'''
print (ehader_row)

for index, column_header in enumerate (header_row):
    print(index,column,header)
'''

highs_death = []
dates_death = []
lows_death = []

highs_sitka = []
dates_sitka = []
lows_sitka = []

'''x = datetime.strptime('2018-07-01','%Y-%m-%d')
'''


for row in csv_death:
    try:
        high_death = int(row[4])
        low_death = int(row[5])
        current_date_death = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing Data for {current_date_death}")
    else:
        dates_death.append(current_date_death)
        highs_death.append(high_death)
        lows_death.append(low_death)

for row in csv_sitka:
    try:
        high_sitka  = int(row[5])
        low_sitka = int(row[6])
        current_date_sitka = datetime.strptime(row[2], '%Y-%m-%d')
    except ValueError:
        print(f"Missing Data for {current_date_sitka}")
    else:
        dates_sitka.append(current_date_sitka)
        highs_sitka.append(high_sitka)
        lows_sitka.append(low_sitka)


import matplotlib.pyplot as plt

fig, ax = plt.subplots(2,1)

ax[0].plot(dates_death, highs_death, c="red", alpha=0.5)
ax[0].plot(dates_death, lows_death, c="blue", alpha=0.5)
ax[1].plot(dates_sitka, highs_sitka, c="red", alpha=0.5)
ax[1].plot(dates_sitka, lows_sitka, c="blue", alpha=0.5)

ax[0].set_title('Temperature comparison between SITKA AIRPORT, AK US and DEATH VALLEY, CA US \n \n SITKA AIRPORT')

plt.title("Death Valley, CA US", fontsize=16)
plt.xlabel("", fontsize=12)


ax[0].fill_between(dates_death, highs_death, lows_death, facecolor='blue', alpha = 0.1)
plt.tick_params(axis="both", labelsize=12)

ax[0].fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor='blue', alpha = 0.1)
plt.tick_params(axis="both", labelsize=12)


fig.autofmt_xdate()


plt.show()