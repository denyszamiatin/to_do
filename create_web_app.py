#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from main import tasks, add_task, fail_if_invalid_date, return_today_tasks

web_app = Flask(__name__)

@web_app.route('/')
@web_app.route('/index')
def index():
    name = {'nickname' : 'Dimon'}
    return render_template('index.html', name = name, list = return_today_tasks())


@web_app.route('/')
@web_app.route('/serch_by_date')
def serch_by_date():
    return '<form action="/serch_by_date" method="GET"><input name="date"><input type="submit" value="Enter date"></form>'


@web_app.route('/addtask', methods=['GET','POST'])
def addtask():
    successful_text = ''
    error_text = ''
    try:
        if request.method == 'POST':
            year, month, day = request.form['date'].split('-')
            add_task(fail_if_invalid_date('{0}.{1}.{2}'.format(day, month, year)), request.form['description'])
            successful_text = u'Данные сохранены'
    except Exception as e:
        error_text = e.message

    return render_template('addtask.html', message = successful_text, error_message = error_text)


web_app.run(debug = True)