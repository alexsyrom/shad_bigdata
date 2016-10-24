#!/usr/bin/env bash
hadoop jar /opt/hadoop/hadoop-streaming.jar \
	-D mapreduce.job.reduces=20 \
	-D mapreduce.job.maps=20 \
	-files mapper.py,reducer.py \
	-input "/user/sandello/logs/access.log.2016-10-20" \
	-output /user/asyromyatnikov/out \
	-mapper mapper.py \
	-reducer reducer.py \
