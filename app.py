import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'IraqDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')

# FOR HOME PAGE
@app.route('/home')
def home():
    return render_template("home.html", login=mongo.db.IQ2019.find())
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
             port=int(os.environ.get('PORT')),
             debug=True)
