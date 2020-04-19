from util import *

r = read('influenza_genome.txt')

w1 = ''
w2 = ''
skip = False
for s in r:
    if s[0] == '>':
        if 'unknown' in s:
            skip = True
        else:
            skip = False
            w1 += s.strip() + '\n'
            w2 += '\n' + s.strip() + '\n'
    elif not skip:
        w2 += s.strip()

write('gisaid.csv', w1)
write('influenza_genome_filtered.txt', w2)

