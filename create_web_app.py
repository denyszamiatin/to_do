__author__ = 'illes'
from flask import Flask, render_template

web_app = Flask(__name__)

@web_app.route('/')
@web_app.route('/index')
def index():
    return render_template()


web_app.run(debug = True)