import csv
from util import *
import math

regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu', 'Shanghai']
head = {'species':0,'province':1,'count':2,'lat':3,'lon':4,'date':5,'doy':6}
birds = [s.strip() for s in read('coolbirds.csv')]

with open('D:/Files/Projects/02251-final-project/data/archive/ebd_full.csv') as inf, open('coolbirdscoords.csv','w',newline='') as out:
    reader = csv.reader(inf)
    writer = csv.writer(out, delimiter=',')
    writer.writerow(next(reader)) # read the first line and write it
                                  # to the output file
    rows = list(reader) # grab all the rows
    newrows = []
    for i, row in enumerate(rows):
        if i % 1000 == 0:
            print(i)
        if row[head['species']] in birds:
            if row[head['count']] == '':
                row[head['count']] == '1'
            newrows.append(row)

    writer.writerows(newrows)