# -*- encoding:utf-8 -*-
from flask import Flask
from boostingMR.lib.hadoop import init_hadoop
from boostingMR.views import init_views
import settings

app = Flask(__name__)
app.config.from_object(settings)

# init views
init_views(app)


init_hadoop(app)
