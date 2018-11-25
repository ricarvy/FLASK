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

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/login_validation', methods=['GET','POST'])
def login_validation():
    username = request.form.get('username')
    password = request.form.get('password')
    sql = f'select * from login_info where username={username} and password={password}'
    data = pd.read_sql(sql, dbcon)
    if data.shape[0] == 0:
        return 'f'
    else:
        return 's'

@app.route('/index')
def index():
    sql = "select * from test"
    data = pd.read_sql(sql, dbcon)
    return render_template('fixed_sidebar.html',name='ricarvy')

@app.route('/dm')
def dm():
    sql = "select * from dm"
    data = pd.read_sql(sql, dbcon).values
    lesson_sql = "select * from lessons"
    lessons_data = pd.read_sql(lesson_sql, dbcon).values
    return render_template('dm.html', data=data, lessons_data = lessons_data)

@app.route('/change_lesson', methods=['GET','POST'])
def change_lesson():
    lesson_id = request.form.get('lesson_id')
    sql = f'select * from dm where lessonid={lesson_id}'
    data = pd.read_sql(sql, dbcon).to_dict()
    print(data)
    return make_response(jsonify({'data':data}))

@app.route('/mp')
def mp():
    return render_template('modify_password.html')

@app.route('/cm')
def cm():
    return render_template('class_manage.html')

@app.route('/bj')
def bj():
    return render_template('bj_manage.html')