from app import app
from flask import render_template, request, redirect, url_for
import os
import requests
import json
from bs4 import BeutifulSuop
from app.utils import extract_tag, selectors 

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/autor')
def autor():
    return render_template('autor.html')

@app.route('/extract', methods=['POST','GET'])
def extract():
    if request.method == "POST":
        product_code = request.form.get('product_code')
        return redirect(url_for('product', product_code))

    return render_template('extract.html')

@app.route('/productsTable')
def productTable():
    return render_template('productsTable.html')

@app.route('/product/<product_code>')
def product(product_code):
    return render_template('product.html', product_code=product_code.
    to_html(headers=True, classes='table table-striped table-success',
            table_id='opinions'))

@app.route('/wykresy')
def wykresy():
    return render_template('wykresy.html')