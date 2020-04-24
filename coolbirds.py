from util import *
regions = ['Guangdong', 'Jiangxi', 'Zhejiang', 'Jiangsu', 'Shanghai']
data = trans(readcsv('coolbirds.csv')[1:])
coolbirds = []
for re in data:
    for bird in re:
        flag = 0
        for i in range(5):
            if bird in data[i]:
                flag +=1 
        if flag >= 5 and bird not in coolbirds:
            coolbirds.append(bird)
coolbirds.sort()
for bird in coolbirds:
    print(bird)