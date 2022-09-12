import csv
import matplotlib.pyplot as plt
from datetime import datetime

death_valley_dates, death_valley_high, sitka_dates, sitka_high = [],[],[],[]


file1 = 'data/death_valley_2018_simple.csv'
file2 = 'data/sitka_weather_2018_simple.csv'

with open(file1) as f1:
    reader =  csv.reader(f1)
    next(reader)

    for header_val in reader:
        fmt_date = datetime.strptime(header_val[2],'%Y-%m-%d')
        try:
            high_temp = int(header_val[4])
        except ValueError:
            print(f"Error while processing data for {fmt_date}")
        else:
            death_valley_dates.append(fmt_date)
            death_valley_high.append(high_temp)

with open(file2) as f2:
    reader =  csv.reader(f2)
    next(reader)

    for header_val in reader:
        fmt_date = datetime.strptime(header_val[2],'%Y-%m-%d')
        try:
            high_temp = int(header_val[5])
        except ValueError:
            print(f"Error while processing data for {fmt_date}")
        else:
            sitka_dates.append(fmt_date)
            sitka_high.append(high_temp)    

plt.style.use('seaborn')
fig, ax = plt.subplots()

ax.set_title("Temperature comparison betweem Death Valley and Sitka", fontsize = 20)
ax.set_xlabel('', fontsize = 16)
ax.set_ylabel('Temperature (F)', fontsize = 16)
ax.plot(death_valley_dates, death_valley_high, c = 'red', alpha = .5)
ax.plot(sitka_dates, sitka_high, c='blue', alpha = .5)
fig.autofmt_xdate()
ax.tick_params(axis='both', which = 'major', labelsize = 20)
plt.show()