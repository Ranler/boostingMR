# -*- encoding:utf-8 -*-
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from boostingMR.views.frontend import frontend
from boostingMR.views.datasets import datasets
from boostingMR.views.training import training
from boostingMR.views.testing import testing
import settings

app = Flask(__name__)
app.config.from_object(settings)


# register view models
app.register_blueprint(frontend)
app.register_blueprint(datasets)
app.register_blueprint(training)
app.register_blueprint(testing)


# init extensions
db = SQLAlchemy(app)
