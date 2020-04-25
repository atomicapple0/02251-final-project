import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import pandas as pd
import csv
from util import *
import math

regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu', 'Shanghai']
head = {'species':0,'province':1,'count':2,'lat':3,'lon':4,'date':5,'doy':6}
coolbirds = [s.strip() for s in read('coolbirds.csv')]
cooldata = [[] for i in range(13)] 

data = readcsv('coolbirdsdat.csv')


for row in data[1:]:
    cooldata[int(row[head['doy']])//30].append(row)

for i in range(12):

    # 1. Draw the map background
    fig = plt.figure(figsize=(8, 8))
    print('ok')
    map = Basemap(projection='lcc', resolution='l', 
                lat_0=29.6, lon_0=114.0,
                width=2.5E6, height=2.5E6)

    map.shadedrelief()
    # map.drawcoastlines(color='gray')
    # map.drawcountries(color='gray')
    # map.drawstates(color='gray')


    # print('ok')

    # # 2. scatter city data, with color reflecting population
    # # and size reflecting area
    # for bird in coolbirds:  
    #     # Extract the data we're interested in
    #     lat = [float(row[head['lat']]) for row in test]
    #     lon = [float(row[head['lon']]) for row in test]
    #     population = [int(row[head['count']]) for row in test]

    #     print('ok')
    #     map.scatter(lon, lat, latlon=True,
    #             s=(population) * 10, alpha=.5)

    # Create plot

    lat = [float(row[head['lat']]) for row in cooldata[i]]
    lon = [float(row[head['lon']]) for row in cooldata[i]]
    spe = [row[head['species']] for row in cooldata[i]]
    count = [int(row[head['count']]) for row in cooldata[i]]
    df = pd.DataFrame(dict(lat=lat, lon=lon, spe=spe,count=count))
    colors = {'Aix galericulata': '#ecd6cb', 'Anas acuta': '#257a83', 'Anas crecca': '#3562e5', 'Aythya ferina': '#9c600d', 'Gallinula chloropus': '#45f4d9', 'Recurvirostra avosetta': '#58b303', 'Spatula clypeata': '#c9456c', 'Tringa glareola': '#31277f'}
    map.scatter(list(df['lon']), list(df['lat']), latlon=True,
                c=list(df['spe'].apply(lambda x: colors[x])), 
                s=count, alpha=0.5)

    plt.title('Matplot scatter plot')
    # plt.legend(loc=2)

    # 3. create colorbar and legend
    # plt.colorbar(label=r'$\log_{10}({\rm population})$')
    # plt.clim(3, 7)

    # make legend with dummy points
    # for a in [100, 300, 500]:
    #     plt.scatter([], [], c='k', alpha=0.5, s=a,
    #                 label=str(a) + ' km$^2$')
    # plt.legend(scatterpoints=1, frameon=False,
    #            labelspacing=1, loc='lower left');
    plt.savefig('ah/{}.png'.format(i))
    plt.show()