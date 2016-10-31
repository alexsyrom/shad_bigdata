#!/usr/bin/env bash
hadoop jar /opt/hadoop/hadoop-streaming.jar \
	-D mapreduce.job.reduces=20 \
	-D mapreduce.job.maps=50 \
	-files mapper.py,reducer.py \
	-input $1 \
	-output $2 \
	-mapper mapper.py \
	-reducer reducer.py \
