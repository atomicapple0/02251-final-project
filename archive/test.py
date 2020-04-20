from util import *

obs = [x.strip() for x in read('tree.fas')]
global genomes
genomes = [x.strip() for x in read('data/genomes.fas')]
def findGenome(id):
    global genomes
    id = '>' + id
    for i in range(0,len(genomes),2):
        if genomes[i] == id:
            return genomes[i+1]
    print('aah')
    print(id)
    assert(0)


w = ''
for ob in obs:
    w += '>' + ob + '\n' + findGenome(ob) + '\n'
write('tree2.csv', w)