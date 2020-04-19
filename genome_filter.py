from util import *

obs = [x.strip() for x in read('observations.csv')]
# 0:region, 1:DOY, 2:id

global genomes
genomes = [x.strip() for x in read('genomes.csv')]
def findGenome(id):
    global genomes
    for i in range(0,len(genomes),2):
        if genomes[i] == id:
            return genomes[i+1]
    print('aah')
    print(id)
    assert(0)


regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu']

for region in regions:
    w = ''
    for ob in obs:
        ob = ob.split(',')
        if ob[0] == region:
            w += ob[0] + ',' + ob[1] + ',' + ob[2] + '\n' # + ',' + findGenome(ob[2]) + '\n'
    write('observations/' + region + '.csv', w)
    #write('genomes/' + region + '.csv', w)