import csv
from util import *

regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu', 'Shanghai']
head = {'province':0,'doy':1}
birds = [x.strip() for x in read('data/birds.csv')]

for region in regions:
    with open('data/cases.csv'.format(region)) as inf, open('data/cases_weekly/cases_{}.csv'.format(region),'w',newline='') as out:
        reader = csv.reader(inf)
        writer = csv.writer(out, delimiter=',')
        rows = list(reader) # grab all the rows


        weekly = [0] * 53

        for i, row in enumerate(rows):
            if i % 1000 == 0:
                print(i)
            if row[head['province']] == region:
                weekly[int(row[head['doy']]) // 7] += 1
        
        weekly = [[str(x)] for x in weekly]
        writer.writerows(weekly)