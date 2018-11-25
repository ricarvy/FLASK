from app import app
from flask import render_template, url_for, request, jsonify, make_response
import pymysql
import pandas as pd

dbcon = pymysql.connect(
  host="10.118.41.65",
  user="01380531",
  password="01380531Li",
  db = "class",
  port=3306
)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/shortcodes')
def shortcodes():
    return render_template('shortcodes.html')