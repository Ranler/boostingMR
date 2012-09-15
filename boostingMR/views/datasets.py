# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect, request

datasets = Blueprint('datasets', __name__)

@datasets.route('/datasets')
def index():

    d = {}
    return render_template('datasets/index.html', **d)


@datasets.route('/datasets/random', methods=['POST', 'GET'])
def random():
    if request.method == 'GET':
        d = {}
        return render_template('datasets/random.html', **d)
    else:
        name = request.form['rdname']
        generator = request.form['rdgen']
        attributeNum = request.form['rdnAttr']
        classNum = request.form['rdnClass']
        instanceNum = request.form['rdnInst']

        d = {}
        d['msg'] = 'test'
        return render_template('datasets/random.html', **d)
