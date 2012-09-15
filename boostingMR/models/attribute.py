# -*- encoding:utf-8 -*-
from boostingMR.models import db

class Attribute(db.Model) :
    __tablename__ = 'attribute'

    id = db.Column(db.Integer, primary_key=True)
    did = db.Column(db.Integer)
    name = db.Column(db.String)
    type = db.Column(db.Integer)
    isClass = db.Column(db.Integer, default=0)
    extra = db.Column(db.String)


    def __init__(self, did, name, type=0, isClass=0, extra=''):
        self.did = did
        self.name = name
        self.type = type
        self.isClass = isClass
        self.extra = extra
