# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect

testing = Blueprint('testing', __name__)

@testing.route('/testing')
def index():
    return render_template('testing/index.html')
