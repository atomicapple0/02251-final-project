import os
from util import *
from random import randint


regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu', 'Shanghai']

data = {}
for region in regions:
    data[region] = [x.strip().split(',') for x in read('data/genomes/' + region + '.csv')]


for i in range(100):
    w = ''
    for region in regions:
        rand = randint(0,len(data[region])-1)
        w += '>' + data[region][rand][0] + ' (' + data[region][rand][2] + ')\n' + data[region][rand][3] + '\n'
    write('phylogeny/trash/randseq-{:03d}.fas'.format(i), w)
    os.system('megacc -a phylogeny/mao/clustal_align_nucleotide.mao -d phylogeny/trash/randseq-{:03d}.fas -o phylogeny/trash/randalign-{:03d}.meg'.format(i,i))
    os.system('megacc -a phylogeny/mao/infer_NJ_nucleotide.mao -d phylogeny/trash/randalign-{:03d}.meg -o phylogeny/random_trees/randtree-{:03d}.align'.format(i,i))