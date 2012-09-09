# -*- encoding:utf-8 -*-
from boostingMR.models import db

class Dataset(db.Model) :
    __tablename__ = 'dataset'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    size = db.Column(db.Integer)
    instances = db.Column(db.Integer)
    classes = db.Column(db.Integer)
    extra = db.Column(db.String)

    def __init__(self, name, size, instances, classes, extra=""):
        self.name = name
        self.size = size
        self.instances = instances
        self.classes = classes
        self.extra = extra


