from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy.sql import func

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

@app.route("/success", methods=['POST'])  # default is 'GET' , for 'POST' method we have to mention it
def success():
    if request.method== 'POST':
        email= request.form["email_id"] #'request.form' is an element of request method that returns a dictionary and here it captures the email id by dictionary key and stores in a variable and 'email_id' can be found in index.html --> input --> 1st one. and we are using 'if' conditionals as 'GET' request can come also.
        height= request.form["height_name"]
        
        if db.session.query(Data).filter(Data.email_received== email).count()== 0: # db.session.query(Data) --> inside the bracket will be the class name. Then it will check the database if user have typed an existing email or not, if existing then reload the same page, otherwise return the rendered html , 'success' in this case. 'count()==0' means no matching email.
            data=Data(email, height) # instance of the class 'Data' and passing the variable values as argument.
            db.session.add(data) # adding the instance to the 'db' object.
            db.session.commit()
            average_height= db.session.query(func.avg(Data.height_received)).scalar() # here the class 'func' will apply the 'avg' method on 'height_received' column and scalar method will receive it as a number not as an object
            average_height= round(average_height, 2)
            count= db.session.query(Data.height_received).count()
            send_email(email, height, average_height, count) # passing arguments to the function that have been imported.
            return render_template("success.html")
        return render_template("index.html", text="Email already exits, try a different one!")

if __name__== "__main__": # it means if the scripts is being executed, not imported then following codes will run.
    app.debug= True
    app.run() # the default port is here 5000, we can change it by --> app.run(port= 6000)
