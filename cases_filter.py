import csv
from util import *

regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu', 'Shanghai']
head = {'province':0,'doy':1}
birds = [x.strip() for x in read('data/birds.csv')]


with open('data/cases.csv') as inf, open('data/cases2.csv','w',newline='') as out:
    reader = csv.reader(inf)
    writer = csv.writer(out, delimiter=',')
    rows = list(reader) # grab all the rows

    newrows = []
    for i, row in enumerate(rows):
        if i % 1000 == 0:
            print(i)
        if row[head['province']] in regions:
            newrows.append(row)
    
    writer.writerows(newrows)