import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

import csv
from util import *
import math

regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu', 'Shanghai']
head = {'species':0,'province':1,'count':2,'lat':3,'lon':4,'date':5,'doy':6}
birds = [s.strip() for s in read('coolbirds.csv')]

with open('coolbirds.csv') as inf, open('coolbirdscoords.csv','w',newline='') as out:
    reader = csv.reader(inf)
    writer = csv.writer(out, delimiter=',')
    writer.writerow(next(reader)) # read the first line and write it
                                  # to the output file
    rows = list(reader) # grab all the rows
    newrows = []
    for i, row in enumerate(rows):
        if i % 1000 == 0:
            print(i)
        if row[head['species']] in birds:
            if row[head['count']] == '':
                row[head['count']] == '1'
            newrows.append(row)

    writer.writerows(newrows)

cities = pd.read_csv('data/california_cities.csv')

# Extract the data we're interested in
lat = cities['latd'].values
lon = cities['longd'].values
population = cities['population_total'].values
area = cities['area_total_km2'].values

# 1. Draw the map background
fig = plt.figure(figsize=(8, 8))
m = Basemap(projection='lcc', resolution='h', 
            lat_0=37.5, lon_0=-119,
            width=1E6, height=1.2E6)
m.shadedrelief()
m.drawcoastlines(color='gray')
m.drawcountries(color='gray')
m.drawstates(color='gray')

# 2. scatter city data, with color reflecting population
# and size reflecting area
m.scatter(lon, lat, latlon=True,
          c=np.log10(population), s=area,
          cmap='Reds', alpha=0.5)

# 3. create colorbar and legend
plt.colorbar(label=r'$\log_{10}({\rm population})$')
plt.clim(3, 7)

# make legend with dummy points
for a in [100, 300, 500]:
    plt.scatter([], [], c='k', alpha=0.5, s=a,
                label=str(a) + ' km$^2$')
plt.legend(scatterpoints=1, frameon=False,
           labelspacing=1, loc='lower left');