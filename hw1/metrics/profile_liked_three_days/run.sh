#!/bin/bash
spark-submit metric.py \
    --master yarn-client \
    --num-executors 6 \
    --driver-memory 2g \
    --executor-memory 8g \
    --executor-cores 4 \
    --conf "spark.yarn.executor.memoryOverhead=1024" \
    --date "2016-12-12"
