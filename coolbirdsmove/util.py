def read(filename):
    with open(filename, 'r') as f:
        return f.readlines()

def write(path, contents):
	with open(path, 'w') as f:
		f.write(contents)

import numpy as np
import scipy.signal as ss

def ccf(x, y, lag_max = 100):

    result = ss.correlate(y - np.mean(y), x - np.mean(x), method='direct') / (np.std(y) * np.std(x) * len(y))
    length = (len(result) - 1) // 2
    lo = length - lag_max
    hi = length + (lag_max + 1)

    return result[lo:hi]

def trans(l):
    return list(map(list, zip(*l)))

import csv
def readcsv(file):
    with open(file) as inf:
        reader = csv.reader(inf)
        data = list(reader)
        return data