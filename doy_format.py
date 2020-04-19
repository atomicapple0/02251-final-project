from util import *
from datetime import datetime

cases = read('cases.csv')
out = ''
for s in cases:
    ss = s.split(',')
    ss_date = datetime.strptime(ss[1].strip(), '%Y-%m-%d')
    ss[1] = ss_date.timetuple().tm_yday
    out += ss[0] + ',' + str(ss[1]) + '\n'

write('cases_1.csv', out)
