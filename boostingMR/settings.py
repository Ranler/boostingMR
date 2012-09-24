# -*- encoding:utf-8 -*-

SECRET_KEY = 'uEQT&O+PX$TgvM6-g$t^\\"UqY\\P,0_s$'


# Flask-SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'sqlite:///boostingMR.db3'
SQLALCHEMY_ECHO = False

# Workspace
SERVER_WORKSPACE_DIR = 'boostingMR'
LOCAL_WORKSPACE_DIR = '/tmp/boostingMR'

# Hadoop
HADOOP_DIR = '/usr/lib/hadoop'
HADOOP_NAMENODE = 'hdfs://211.87.100.189:9160/'
HADOOP_CLASSPATH = '/usr/lib/hadoop/client/asm-3.2.jar:/usr/lib/hadoop/client/avro-1.5.4.jar:/usr/lib/hadoop/client/commons-beanutils-1.7.0.jar:/usr/lib/hadoop/client/commons-beanutils-core-1.8.0.jar:/usr/lib/hadoop/client/commons-codec-1.4.jar:/usr/lib/hadoop/client/commons-collections-3.2.1.jar:/usr/lib/hadoop/client/commons-configuration-1.6.jar:/usr/lib/hadoop/client/commons-digester-1.8.jar:/usr/lib/hadoop/client/commons-el-1.0.jar:/usr/lib/hadoop/client/commons-io-2.1.jar:/usr/lib/hadoop/client/commons-lang-2.5.jar:/usr/lib/hadoop/client/commons-logging-1.1.1.jar:/usr/lib/hadoop/client/commons-math-2.1.jar:/usr/lib/hadoop/client/commons-net-3.1.jar:/usr/lib/hadoop/client/guava-11.0.2.jar:/usr/lib/hadoop/client/hadoop-auth-2.0.0-cdh4.0.1.jar:/usr/lib/hadoop/client/hadoop-common-2.0.0-cdh4.0.1.jar:/usr/lib/hadoop/client/hadoop-hdfs-2.0.0-cdh4.0.1.jar:/usr/lib/hadoop/client/hadoop-mapreduce-client-app-2.0.0-cdh4.0.1.jar:/usr/lib/hadoop/client/hadoop-mapreduce-client-common-2.0.0-cdh4.0.1.jar:/usr/lib/hadoop/client/hadoop-mapreduce-client-core-2.0.0-cdh4.0.1.jar:/usr/lib/hadoop/client/hadoop-mapreduce-client-jobclient-2.0.0-cdh4.0.1.jar:/usr/lib/hadoop/client/hadoop-mapreduce-client-shuffle-2.0.0-cdh4.0.1.jar:/usr/lib/hadoop/client/hadoop-yarn-api-2.0.0-cdh4.0.1.jar:/usr/lib/hadoop/client/hadoop-yarn-common-2.0.0-cdh4.0.1.jar:/usr/lib/hadoop/client/hadoop-yarn-server-common-2.0.0-cdh4.0.1.jar:/usr/lib/hadoop/client/jackson-core-asl-1.8.8.jar:/usr/lib/hadoop/client/jackson-mapper-asl-1.8.8.jar:/usr/lib/hadoop/client/jline-0.9.94.jar:/usr/lib/hadoop/client/jsch-0.1.42.jar:/usr/lib/hadoop/client/json-simple-1.1.jar:/usr/lib/hadoop/client/jsr305-1.3.9.jar:/usr/lib/hadoop/client/log4j-1.2.15.jar:/usr/lib/hadoop/client/netty-3.2.3.Final.jar:/usr/lib/hadoop/client/oro-2.0.8.jar:/usr/lib/hadoop/client/paranamer-2.3.jar:/usr/lib/hadoop/client/protobuf-java-2.4.0a.jar:/usr/lib/hadoop/client/slf4j-api-1.6.1.jar:/usr/lib/hadoop/client/slf4j-log4j12-1.6.1.jar:/usr/lib/hadoop/client/snappy-java-1.0.3.2.jar:/usr/lib/hadoop/client/xmlenc-0.52.jar:/usr/lib/hadoop/client/zookeeper-3.4.3-cdh4.0.1.jar:boostingMR/pig/piglib/pig-0.9.2-cdh4.0.1.jar:/etc/hadoop/conf.jsjcloud/'

