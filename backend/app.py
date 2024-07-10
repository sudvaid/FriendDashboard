#ok, so before we installed flask or anything, we created a virtual environment using python -m venv venv, where the second venv is the name of our virtual environment 
# this allowed us to install flask without having to do it on our machine-- instead it is only on the venv 


from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_cors import CORS 


app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///friends.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

import routes

#the below creates the tables needed, creates context for optimization 

with app.app_context(): 
    db.create_all()


#what this if statement below does is only if app.py is ran directly using python app.py, the entire thing will run on its own
# if app.py is imported into a a diff file like it is in models.py. using 'from app import db'
# we dont want the entirety of app.py to run multiple times -- only once
# so th if statement prevents infinite loops 

#snce running on a venv, of u go to localhost5000/api/friends and it says no tbale friends, make sure to 
# set FLASK_APP=app.py and set FLASK_ENV=development and flask run
#do all 3 commands in terminal
# ACTUALLY instead of flask run, do flask run --reload to avoid having to reload 



if __name__ == "__main__":
    app.run(debug=True)
