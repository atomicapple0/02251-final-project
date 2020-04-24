import csv
from util import *

regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu', 'Shanghai']
head = {'species':0,'province':1,'count':2,'lat':3,'lon':4,'date':5,'doy':6}
birds = [x.strip() for x in read('data/birds.csv')]
birdid = {x:i for i,x in enumerate(birds)}

for region in regions:
    with open('data/ebd.csv') as inf, open('data/ebd_weekly/ebd_{}.csv'.format(region),'w',newline='') as out:
        reader = csv.reader(inf)
        writer = csv.writer(out, delimiter=',')
        next(reader)
        rows = list(reader) # grab all the rows
        writer.writerow(birds)
        weekly = [[0] * len(birds) for i in range(53)]
        
        for i, row in enumerate(rows):
            if i % 1000 == 0:
                print(i)
            if row[head['province']] == region:
                weekly[int(row[head['doy']]) // 7][birdid[row[head['species']]]] += int(row[head['count']])
            
        weekly = [[str(y) for y in x] for x in weekly]
        writer.writerows(weekly)