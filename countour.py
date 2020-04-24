import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib
import numpy as np
import seaborn as sns
from util import *
import csv

regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu', 'Shanghai']
# regions = ['Guangdong']
head = {'province':0,'doy':1}
birds = [x.strip() for x in read('data/birds.csv')]


cool = []

for region in regions:
    with open('data/cases_weekly2/cases_{}.csv'.format(region)) as inf:
        reader = csv.reader(inf)
        data = trans(list(reader))
    datanew = []
    for i,row in enumerate(data):
        if abs(max([float(x) for x in row[1:]])) > .3:
            datanew.append(row)
    data = datanew
    birdids = [row[0] for row in data]
    cool.append([region] + birdids)
    birdids = [x.split(' ')[0][0]+ '. ' + x.split(' ')[1] for x in birdids]
    data = trans([row[1:] for row in data])
    data = np.array([[float(x) for x in y] for y in data])

    # Make a 9x9 grid...
    ax = sns.heatmap(data, cmap="YlGnBu")

    # put the major ticks at the middle of each cell
    plt.xticks(rotation=90)
    plt.yticks(rotation=0)
    plt.subplots_adjust(bottom=.5, right=1)
    ax.set_xticks(np.arange(data.shape[1]) + .5, minor=False)
    ax.set_yticks(np.arange(data.shape[0]) + .5, minor=False)

    # want a more natural, table-like display
    ax.invert_yaxis()
    # ax.xaxis.tick_top()
    # ax.xaxis.set_ticks_position('both') # THIS IS THE ONLY CHANGE
    plt.title(region)
    ax.set_xticklabels(birdids, minor=False)
    ax.set_yticklabels(range(-10,11), minor=False)
    ax.set_xlabel('Bird Species')
    ax.set_ylabel('Lag (in weeks)')
    # plt.show()
with open('coolbirds.csv','w') as out:
    maxi = max([len(row) for row in cool])
    for i,row in enumerate(cool):
        cool[i] += ([''] * (maxi - len(row)))
    cool = trans(cool)
    writer = csv.writer(out, delimiter=',')
    writer.writerows(cool)