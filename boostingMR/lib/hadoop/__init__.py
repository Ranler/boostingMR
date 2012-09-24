# -*- encoding:utf-8 -*-
from pigpy.hadoop import Hadoop

hadoop = None

def init_hadoop(app):
    local_home = app.config['HADOOP_DIR']
    name_node = app.config['HADOOP_NAMENODE']
    classpaths = app.config['HADOOP_CLASSPATH']

    global hadoop
    hadoop = Hadoop(local_home, name_node, classpaths)

def get_hadoop():
    return hadoop
