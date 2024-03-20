from matplotlib import pyplot as plt
import csv
import datetime as dt
from datetime import datetime


x1,y1 = [],[]
x2,y2 = [],[]


with open('ch15_data/a.csv', 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    print(header)
    for row in reader:
        x1.append(dt.strptime(row[2], '%Y-%m-%d'))
        y1.append(int(row[4]))
        x2.append(int(row[5]))


plt.plot(x1,y1, label='TMAX', color='red')
plt.plot(x2,y2, label='TMIN', color='blue')
plt.fill_between()
plt.xticks(x1,rotation='vertical')
plt.xlabel('data')

# plt.title('X Square')
# plt.xlabel('X')
# plt.ylabel('X Square')
plt.legend()
plt.show()