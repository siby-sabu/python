import csv
import matplotlib.pyplot as plt
from datetime import datetime

# filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader =csv.reader(f)
    header_row = next(reader)
    #  for header_col in header_row :
    #     print(header_col)
    high_temp, low_temp, dates = [], [], []
    for value in reader:
        # high_temp.append(int(value[5]))
        # low_temp.append(int(value[6]))

        high_temp.append(int(value[4]))
        low_temp.append(int(value[5]))

        fmt_date = datetime.strptime(value[2], '%Y-%m-%d')
        dates.append(fmt_date)
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, high_temp, c= 'red', alpha=.5)
    ax.plot(dates, low_temp, c= 'blue', alpha = .5)
    ax.fill_between(dates, high_temp, low_temp, facecolor='blue', alpha = .1)
    ax.set_title(label = "Daily Temperature", fontsize = 24 )
    ax.set_xlabel("", fontsize = 16)
    fig.autofmt_xdate()
    ax.set_ylabel("Temperature(F)", fontsize = 16)
    ax.tick_params(axis="both", which = "major", labelsize = 16)
    plt.show()
raw_date = '2022-07-06'
date = datetime.strptime(raw_date, '%Y-%m-%d')
print(raw_date, date)


