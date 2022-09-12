import csv
from email.policy import default
from shutil import which
import matplotlib.pyplot as plt
from datetime import datetime

filename = "data/death_valley_2018_simple.csv"

with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    dates, max, min = [], [], []
    for values in reader:
       
      
        try:
            date_formatted = datetime.strptime(values[2], '%Y-%m-%d')
            max_value = int(values[4])
            
            min_value = int(values[5])
           
        except ValueError:
            print('Error while processing a row')
        else:
            dates.append(date_formatted)
            max.append(max_value)
            min.append(int(values[5]))
    
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, max, c= 'red', alpha = .5)
    ax.plot(dates, min, c = 'blue' , alpha = .5)
    ax.fill_between(dates, max, min, facecolor = 'blue', alpha =.1)
    ax.set_title(label="Death Valley Temperature", fontsize = 24)
    ax.set_xlabel('', fontsize = 16)
    fig.autofmt_xdate()
    ax.set_ylabel('Temperature(F)', fontsize = 16)
    ax.tick_params(axis='both', which='major', labelsize = 16 )
    plt.show()