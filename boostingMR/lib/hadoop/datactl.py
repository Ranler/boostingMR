# -*- encoding:utf-8 -*-
import os
import subprocess
from boostingMR.lib.hadoop import get_hadoop

LOCAL_WORKSPACE_DIR = '/tmp/boostingMR/'

SERVER_WORKSPACE_DIR = 'boostingMR/'
DATASET_DIR = SERVER_WORKSPACE_DIR + 'datasets/'

RANDOM_FILE_NAME = 'random.mdata'

def gen_random_data(dataset):
    server_mdata = SERVER_WORKSPACE_DIR + DATASET_DIR + RANDOM_FILE_NAME
    server_data = SERVER_WORKSPACE_DIR + DATASET_DIR + dataset.getPathName()

    create_random_mdata(dataset.getInstanceNum())

    '''
    hadoop = get_hadoop()
    params = ['-param wekaparams=\'weka.datagenerators.classifiers.classification.RDG1 \
    -r weka.datagenerators.classifiers.classification.RDG1-S_1_-n_1000_-a_'+dataset.getAttributeNum()
    +'_-c_'+dataset.getClassNum()
    +'_-N_100_-I_0_-M_1_-R_10 -S 1 -n 1000 -a '+dataset.getAttributeNum()
    +' -c '+dataset.getClassNum()
    +' -N 1000 -I 0 -M 1 -R 10\'',
    '-param input=' + server_mdata,
    '-param output=' + server_data]
    hadoop.run_pig_job('scrpits/gen_random.pig', params)
    hadoop.rm(server_mdata)

    # get file size
    size = hadoop.filesize(server_data)
    dataset.setSize(size)
    '''

def create_random_mdata(instanceNum):
    local_mdata = os.path.join(LOCAL_WORKSPACE_DIR, RANDOM_FILE_NAME)
    hadoop = get_hadoop()

    result = subprocess.Popen(['mkdir', '-p', LOCAL_WORKSPACE_DIR])
    result = subprocess.Popen(['seq', '1', str(instanceNum)], stdout=open(local_mdata, 'w'))
    print result
    hadoop.copyFromLocal(local_mdata, DATASET_DIR + RANDOM_FILE_NAME)
    result = subprocess.Popen(['rm', '-r', local_mdata])




