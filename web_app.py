#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect
from main import tasks, add_task, fail_if_invalid_date, return_today_tasks
from setting import nickname

web_app = Flask(__name__)

@web_app.route('/')
@web_app.route('/index')
def index():
    return render_template('index.html', name=nickname, tasks=return_today_tasks())


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


def _convert_htm5_date(date):
    year, month, day = date.split('-')
    return '{0}.{1}.{2}'.format(day, month, year)


web_app.run(debug = True)