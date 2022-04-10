from flask import Flask, make_response, render_template, url_for, request, redirect
from flask import current_app as app
from sqlalchemy import null
from .forms import RestaurantForm
from .__init__ import *
from .models import *
from random import randint

@app.route('/', methods = ['POST', 'GET'])
@app.route('/home')
@app.route('/index')
def index():
    rForm = RestaurantForm()
    if request.method == 'POST':
        cust = Customer(Name = rForm.cName, TableNum = rForm.tableNum, ReceiptNum = randint(0, 200), RestaurantID = rForm.restID)
        db.session.add(cust)
        db.session.commit()
        return make_response(redirect('/order'))
    return render_template('index.html', title="Boishii Mobile Menu | Home", form=rForm)

@app.route('/order')
def order_page():
    return render_template('appetizers.html', title="Boishii Mobile Menu | Order")



# @app.route('/<EID>,<Fname>, <Lname>, <Vcode>')
# def create_manager(EID, Fname, Lname, Vcode):
#         manager = Manager(First_Name = Fname, Last_Name = Lname,EmployeeID = EID,Validation_Code= Vcode  )
#         db.session.add(manager)
#         db.session.commit()
#         Manager.query.all()
#         return "Created User!"


# @app.route('/<EID>&<Fname>&<Lname>&<Vcode>')
# def create_manager(EID, Fname, Lname, Vcode):
#         manager = Manager(First_Name = Fname, Last_Name = Lname,EmployeeID = EID,Validation_Code= Vcode  )
#         print("eid =" + EID + "fname = " + Fname + "lname = "+ Lname + "vcode = " +Vcode)
        
#         db.session.add(manager) 
#         db.session.commit()
#      #   Manager.query.all()
#         return "Created User!"

@app.route('/?cust_name=<Cname>&table_num=<tnum>&restaurant_id=<rID> HTTP/1.1')
def create_customer(Cname, tnum, rID):
        cust = Customer(Name = Cname, TableNum = tnum,ResturantID = rID)
        print("name =" + Cname + "fname = " + tnum + "lname = "+ rID)
        db.session.add(cust)
        db.session.commit()
        #Manager.query.all()
        return "Created User!"

# @app.route('/?cust_name=<name>&table_num=<tnum>&restaurant_id=<rID>')
# def create_customer(name,tnum,rID):
#         # cust = Customer(Name = name, TableNum = tnum,ResturantID = rID)
#         # db.session.add(cust)
#         # db.session.commit()
        
#         return "Created User!"



# @app.route('/<EID>&<Fname>&<Lname>&<Vcode>')
# def create_manager(EID, Fname, Lname, Vcode):
#         manager = Manager(First_Name = Fname, Last_Name = Lname,EmployeeID = EID,Validation_Code= Vcode  )
#         db.session.add(manager)
#         db.session.commit()
#         Manager.query.all()
#         return "Created User!"



# @app.route('/<name>,<age>')
# def create_manager(name,age):
   
#         return f"Created User : name: {name} + age: {age}!"