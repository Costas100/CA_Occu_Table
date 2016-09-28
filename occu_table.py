##Constantine Athanitis
##Work 3 Main App 
from flask import Flask, render_template
import utils.occupation

app = Flask(__name__) 


<<<<<<< HEAD
=======
heading = ["Job Class", "Percentage"]
            tot = ["Total", "99.8"]
	
>>>>>>> 3e51e0da85fe0d6226a2c1d10791a7033dd59c43

heading = ["Job Class", "Percentage"]
tot = ["Total", "99.8"]
	


@app.route("/occupations")
def printRandOcc():
    dicti = utils.occupation.dict()
    randOcc = ""
    randOcc = utils.occupation.randOccupation(dicti)
    return render_template('work3.html', d=dicti, head = heading,tot = tot, rand = randOcc)


if (__name__) == "__main__":
    app.debug = True
    app.run()

