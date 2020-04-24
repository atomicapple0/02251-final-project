import csv
from util import *

regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu', 'Shanghai']
head = {'province':0,'doy':1}
birds = [x.strip() for x in read('data/birds.csv')]

for region in regions:
    with open('data/ebd_weekly/ebd_{}.csv'.format(region)) as inf, open('data/cases_weekly/cases_{}.csv'.format(region)) as inf2, open('data/cases_weekly2/cases_{}.csv'.format(region),'w',newline='') as out:
        cases = [int(x) for x in trans(list(csv.reader(inf2)))[0]]
        reader = csv.reader(inf)
        writer = csv.writer(out, delimiter=',')
        next(reader)
        bird_counts = trans(list(reader)) # grab all the rows


        lags = []

        for i,bird_count in enumerate(bird_counts):
            lags.append([birds[i]] + [*ccf([int(x) for x in bird_count],cases,10)])
        
        lags = trans([[str(x) for x in y] for y in lags])
        lags = [[x if x != 'nan' else '0' for x in y] for y in lags]
        print(lags)
        writer.writerows(lags)