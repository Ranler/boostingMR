# -*- encoding:utf-8 -*-
from flask import Blueprint, render_template, url_for, redirect, request
from boostingMR.lib.hadoop.datactl import gen_random_data
from boostingMR.models.dataset import Dataset

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
        attributeNum = int(request.form['rdnAttr'])
        classNum = int(request.form['rdnClass'])
        instanceNum = int(request.form['rdnInst'])

        d = {}
        d['msg'] = 'test'

        dataset = Dataset(name, instanceNum, attributeNum, classNum)
        gen_random_data(dataset)
        
        return render_template('datasets/random.html', **d)

@datasets.route('/datasets/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'GET':
        d = {}
        return render_template('datasets/upload.html', **d)
    else:
        name = request.form['rdname']
        generator = request.form['rdgen']
        attributeNum = request.form['rdnAttr']
        classNum = request.form['rdnClass']
        instanceNum = request.form['rdnInst']

        d = {}
        d['msg'] = 'test'
        return render_template('datasets/random.html', **d)
