import csv

with open('data/ebd.csv') as inf, open('ebd2.csv','w',newline='') as out:
    reader = csv.reader(inf)
    writer = csv.writer(out, delimiter=',')
    writer.writerow(next(reader)) # read the first line and write it
                                  # to the output file
    rows = list(reader) # grab all the rows
    for i, row in enumerate(rows):
        if i % 100 == 0:
            print(i)
        row[6] = int(row[6])-1 # reduce the first number for all
                              # rows
    # Set the last row to a random number
    writer.writerows(rows)