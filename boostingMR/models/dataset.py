# -*- encoding:utf-8 -*-
from boostingMR.models import db

class Dataset(db.Model) :
    __tablename__ = 'dataset'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    size = db.Column(db.Integer)
    instanceNum = db.Column(db.Integer)
    classNum = db.Column(db.Integer)
    classes = db.Column(db.String)
    description = db.Column(db.String)
    extra = db.Column(db.String)

    def __init__(self, name, size, instanceNum, classNum, classes, description='', extra=''):
        self.name = name
        self.size = size
        self.instanceNum = instanceNum
        self.classNum = classNum
        self.classes = classes
        self.description = description
        self.extra = extra
