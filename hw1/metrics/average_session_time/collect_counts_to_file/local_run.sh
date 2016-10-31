#!/usr/bin/env bash
# local mode
hadoop --config /home/agorokhov/conf.empty jar /opt/hadoop/hadoop-streaming.jar \
	-D mapreduce.job.reduces=1 \
	-D mapreduce.job.maps=1 \
	-files mapper.py,reducer.py \
	-input /hdfs/user/asyromyatnikov/out \
	-output /hdfs/user/asyromyatnikov/out1 \
	-mapper ./mapper.py \
	-reducer ./reducer.py \

