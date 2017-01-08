#!/usr/bin/env bash

spark-submit \
      --master yarn-client \
      --num-executors 2 \
      --executor-cores 1 \
      --executor-memory 2048m \
      stream_metrics_netcat.py \
      --port 9999 \
      --host hadoop2-00.yandex.ru
