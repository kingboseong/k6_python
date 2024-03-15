
# with open('a.csv') as f:
#     for line in f:
#         print(line.rstrip().split(sep=','))

import csv
import matplotlib.pyplot as plt
from pathlib import Path

COL_DATA = 2
COL_TMAX = 4

x1,y1 = [],[]
x2,y2 = [],[]

with open(Path('data','a.csv')) as f:
    reader = csv.reader(f)
    header = next(reader)
    for line in reader:
        
        x1.append(line[COL_DATA])
        y1.append(line[COL_TMAX])
        x2.append(line[2])
        y2.append(line[5])


plt.plot(x1,y1,label = 'TMAX')
plt.plot(x2,y2,label = 'TMIN')
plt.legend()
plt.show()

