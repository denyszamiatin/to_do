#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from datetime import datetime
from main import add_task, fail_if_invalid_date, read_tasks, delete_task,\
    read_all_tasks, get_all_tasks
from setting import nickname

web_app = Flask(__name__)
read_tasks()

@web_app.route('/')
@web_app.route('/index')
def index():
    date = _convert_htm5_date(request.args['date']) \
        if request.args else datetime.today().strftime('%d.%m.%Y')
    return render_template(
        'index.html',
        name=nickname,
        date=date,
        tasks=get_all_tasks(date)
    )


@web_app.route('/addtask', methods=['GET', 'POST'])
def add_task_web():
    error_message = ''
    form = {
        'date': request.form['date'] if request.form else '',
        'description': request.form['description'] if request.form else ''
    }

    if request.method == 'POST':
        try:
            add_task(
                fail_if_invalid_date(_convert_htm5_date(form['date'])),
                form['description']
            )
            return redirect('/')
        except Exception as e:
            error_message = e.message
    return render_template('addtask.html', error_message=error_message, form=form)


@web_app.route('/deltask', methods=['GET', 'POST'])
def delete_task_web():
    error_message = ''
    if request.method == 'POST':
        try:
            delete_task(
                request.form['task'],
                int(request.form['index'])
            )
        except Exception as e:
            error_message = e.message
    return render_template('deltask.html', error_message=error_message, tasks=read_all_tasks())


def _convert_htm5_date(date):
    year, month, day = date.split('-')
    return '{0}.{1}.{2}'.format(day, month, year)


web_app.run(debug=True)