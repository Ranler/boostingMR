# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect

frontend = Blueprint('frontend', __name__)

@frontend.route('/')
def index():
    return render_template('/frontend.html')

@frontend.route('/dataset')
def dataset():
    return render_template('/dataset.html')

@frontend.route('/dataset', methods=['POST'])
def dataset_next():
    return redirect(url_for('frontend.model'))

@frontend.route('/model')
def model():
    return render_template('/model.html')

@frontend.route('/test')
def test():
    return render_template('/test.html')
