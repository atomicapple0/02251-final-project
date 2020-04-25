from util import *
import csv
import math

regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu', 'Shanghai']
head = {'species':0,'province':1,'count':2,'lat':3,'lon':4,'date':5,'doy':6}
birds = [x.strip() for x in read('data/birds.csv')]
coolbirds = [x.strip() for x in read('coolbirds.csv')]
coolbird_count = [0] * len(coolbirds)
data = readcsv('data/ebd.csv')
tot = 0
for i,bird in enumerate(coolbirds):
    for row in data:
        if row[head['species']] == bird:
            coolbird_count[i] += int(row[head['count']])

# tot = 0
# for row in data:
#     if row[head['species']] in birds:
#         try:
#             count = int(row[head['count']])
#         except:
#             count = 1
#         tot += count 

for i in range(len(coolbird_count)):
    print(coolbird_count[i])

# print(tot)
