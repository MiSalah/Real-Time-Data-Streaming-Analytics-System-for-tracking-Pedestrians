#!/bin/bash

# generate ssh key
echo "Y" | ssh-keygen -t rsa -P "" -f configs/id_rsa

# Building Hadoop Docker Image
docker build -f ./docker_hadoop/Dockerfile . -t hadoop_spark_cluster:hadoop

# Building Spark Docker Image
docker build -f ./docker_spark/Dockerfile . -t hadoop_spark_cluster:spark

# Building PostgreSQL Docker Image for Hive Metastore Server
docker build -f ./docker_postgresql/Dockerfile . -t hadoop_spark_cluster:postgresql

# Building Hive Docker Image
docker build -f ./docker_hive/Dockerfile . -t hadoop_spark_cluster:hive

