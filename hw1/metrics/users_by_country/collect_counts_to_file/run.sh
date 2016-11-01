#!/usr/bin/env bash
hadoop jar /opt/hadoop/hadoop-streaming.jar \
	-D mapreduce.job.reduces=1 \
	-D mapreduce.job.maps=20 \
	-files mapper.py,reducer.py \
	-input /user/asyromyatnikov/out \
	-output /user/asyromyatnikov/out1 \
	-mapper mapper.py \
	-reducer reducer.py \
