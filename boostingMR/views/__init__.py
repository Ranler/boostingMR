# -*- encoding:utf-8 -*-
from .frontend import frontend
from .datasets import datasets
from .training import training
from .testing import testing

def init_views(app):
    # register view models
    app.register_blueprint(frontend)
    app.register_blueprint(datasets)
    app.register_blueprint(training)
    app.register_blueprint(testing)
