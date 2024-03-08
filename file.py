# with open('name.txt', encoding = 'utf-8') as file:
#     for line in file:
#         print(line, end = '')

# def add (a,b):
#     return a+b
# print(add(1,2))
# print('A', 'B', 'C', sep = ', ')

import csv

with open('grade.csv') as file:
    reader = csv.reader(file)
    # header = next.haeder:
    for line in reader:
        print(line)
