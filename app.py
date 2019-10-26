import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'IraqDB'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)

@app.route('/')

# for home page
@app.route('/home')
def home():
    return render_template("home.html", login=mongo.db.IQ2019.find())
    
# for register form to To save data in mongodb
@app.route('/register', methods=['POST']) 
def register():
    print(request.form)
    data = dict(request.form)
    user_name = data['user_name']
    password = data['password']
    mongo.db.users.insert_one({"user_name": user_name, "password": password})
    return render_template("home.html")
    
# for login form 
@app.route('/login', methods=['POST'])
def login():
    data = dict(request.form)
    print(data)
    user_name = data['user_name']
    password = data['password']
    mongo_data = mongo.db.users.find_one({"user_name": user_name})
    print(mongo_data)
    return render_template("home.html")
    
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
             port=int(os.environ.get('PORT')),
             debug=True)
