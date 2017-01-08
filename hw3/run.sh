#!/usr/bin/env bash

spark-submit 
      --master yarn-client \
      --num-executors 2 \
      --executor-cores 1 \
      --executor-memory 2048m \
      stream_metric.py \
      --topic bigdatashad-2016 \
      --zookeeper hadoop2-10:2181
