from flask import Flask, render_template, url_for
from flask import current_app as app


@app.route('/')
@app.route('/home')
@app.route('/index')
def index():
    return render_template('index.html', title="Boishii Mobile Menu | Home")

@app.route('/order')
def order_page():
    return render_template('appetizers.html', title="Boishii Mobile Menu | Order")