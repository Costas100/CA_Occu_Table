##Constantine Athanitis
##Work 3
import csv, random
from flask import Flask, render_template

app = Flask(__name__) 


heading = ["Job Class", "Percentage"]
            tot = ["Total", "99.8"]
	


randOcc = ""

@app.route("/occupations")
def printRandOcc():
    randOccupation()
    print randOcc
    return render_template('work3.html', d=d, head = heading,tot = tot, rand = randOccupation())

                           
def randOccupation():
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

