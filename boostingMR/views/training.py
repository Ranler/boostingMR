# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect

training = Blueprint('training', __name__)

@training.route('/training')
def index():
    return render_template('training/index.html')
