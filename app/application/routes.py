from flask import Flask, make_response, render_template, url_for, request, redirect
from flask import current_app as app
from sqlalchemy import null
from .forms import RestaurantForm
#from .models import *


@app.route('/', methods = ['POST', 'GET'])
@app.route('/home')
@app.route('/index')
def index():
    rForm = RestaurantForm()
    if request.method == 'POST':
        #cust = Customer(Name = rForm.cName, TableNum = rForm.tableNum, ReceiptNum = None, RestaurantID = rForm.restID)
        #db.session.add(cust)
        #b.session.commit()
        return make_response(redirect('/order'))
    return render_template('index.html', title="Boishii Mobile Menu | Home", form=rForm)

@app.route('/order')
def order_page():
    return render_template('appetizers.html', title="Boishii Mobile Menu | Order")