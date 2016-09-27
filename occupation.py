##Constantine Athanitis
##Work 1

import csv
import random

def dict():
    with open('occupations.csv','rb') as f:
        reader = csv.reader(f)
        d = {}
        for row in reader: 
            d[row[0]] = row[1]
            del d["Job Class"]
            del d["Total"]
            ##Read CSV file and deleted non-numerical data


def randOccupation():
    randomInt =  random.randrange(0,100)
    vals = d.values()
    percentage = 0
    i = 0
    while(randomInt > percentage):
        percentage += float(vals[i]) 
        i+=1
    print d.keys()[i]

randOccupation()
