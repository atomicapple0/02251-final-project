from util import *

r = read('gisaid.csv')

num = 0
curr = r[0].split(',')[0]
for s in r:
    if s.split(',')[0].upper() == curr.upper():
        num += 1
    else:
        print(curr, ' ', num)
        curr = s.split(',')[0]
        num = 1
