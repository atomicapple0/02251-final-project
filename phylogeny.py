import os
from util import *
from random import randint


regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu']

data = {}
for region in regions:
    data[region] = [x.strip().split(',') for x in read('data/genomes/' + region + '.csv')]


for i in range(10):
    w = ''
    for region in regions:
        rand = randint(0,len(data[region]))
        w += '>' + data[region][rand][0] + '-' + data[region][rand][2] + '\n' + data[region][rand][3] + '\n'
    write('data/phylogeny/random_trees/rand_' + "{:03d}".format(i) + '.fas', w)

    