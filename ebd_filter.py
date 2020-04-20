import pandas as pd
import math



for region in ['Guangdong', 'Jiangxi', 'Jiangsu', 'Zhejiang', 'Shanghai']:
    weekly = [0] * 366
    data = pd.read_csv("data/ebd.csv")
    data = data[(data.province == region)]
    for index, row in data.iterrows():
        if math.isnan(row['count']):
            row['count'] = 1
        if row['count'] > weekly[row['doy']-1]:
            weekly[row['doy']-1] = row['count']
