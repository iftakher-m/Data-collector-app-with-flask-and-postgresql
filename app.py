from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]= "postgresql://postgres:iftakher@localhost/Height_collector" 

db= SQLAlchemy(app) 

class Data(db.Model): 
    __tablename__= "user_data"
    id= db.Column(db.Integer, primary_key= True)
    email_received= db.Column(db.String(120), unique= True)
    height_received= db.Column(db.Integer)

    def __init__(self, email_received, height_received):
        self.email_received= email_received
        self.height_received= height_received

# in cmd run -->
# from app import db
# db.create_all() # the reason to run this in cmd is to not run the whole py file and create the web app, we will only create a data table and fields on the database. This will crate our column blueprints that are inside the 'Data' class to the database.

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST'])  # default is 'get' , for 'post' method we have to mention it
def success():
    if request.method== 'POST':
        email= request.form["email_id"] #'request.form' is an element of request method that returns a dictionary and here it captures the email id by dictionary key and stores in a variable and 'email_id' can be found in index.html --> input --> 1st one.
        height= request.form["height_name"]
        print(email, height)
        return render_template("success.html")

if __name__== "__main__": # it means if the scripts is being executed, not imported then following codes will run.
    app.debug= True
    app.run() # the default port is here 5000, we can change it by --> app.run(port= 6000)
