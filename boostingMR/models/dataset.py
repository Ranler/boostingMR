# -*- encoding:utf-8 -*-
from boostingMR.models import db

class Dataset(db.Model) :
    __tablename__ = 'dataset'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    size = db.Column(db.Integer, default=0)
    instanceNum = db.Column(db.Integer)
    attributeNum = db.Column(db.Integer)
    classNum = db.Column(db.Integer)
    classes = db.Column(db.String)
    description = db.Column(db.String)
    extra = db.Column(db.String)

    def __init__(self, name, instanceNum, attributeNum, classNum, classes='', description='', extra=''):
        self.name = name
        self.instanceNum = instanceNum
        self.attributeNum = attributeNum
        self.classNum = classNum
        self.description = description
        self.extra = extra

        if classes == '':
            self.classes = ','.join(['c'+str(i) for i in range(classNum)])
        else:
            self.classes = classes

    def setSize(size):
        self.size = size

    def getReadableSize():
        pass

    def getPathName(self):
        return self.name.replace(' ','_')

    def getClassNum(self):
        return self.classNum

    def getAttributeNum(self):
        return self.attributeNum

    def getInstanceNum(self):
        return self.instanceNum

