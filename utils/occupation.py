##Constantine Athanitis
##Work 3 BackEnd

import csv, random
from flask import Flask

app = Flask(__name__) 



def dict():
    with open('data/occupations.csv','rb') as f:
        reader = csv.reader(f)
        d = {}
        for row in reader: 
            d[row[0]] = row[1]
        del d["Job Class"]
        del d["Total"]
        dicti = d
        return d

                           
def randOccupation(d):
    randomInt =  random.randrange(0,100)
    vals = d.values()
    percentage = 0
    i = 0
    while(randomInt > percentage):
        percentage += float(vals[i]) 
        i+=1    
    if i >= len(d.keys()):
        i= i-1
    return d.keys()[i]



if (__name__) == "__main__":
    app.debug = True
    app.run()


