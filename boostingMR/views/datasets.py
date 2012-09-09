# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect

datasets = Blueprint('datasets', __name__)

@datasets.route('/datasets')
def index():
    return render_template('datasets/index.html')

