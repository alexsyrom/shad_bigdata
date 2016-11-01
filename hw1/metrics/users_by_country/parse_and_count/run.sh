#!/usr/bin/env bash
hadoop jar /opt/hadoop/hadoop-streaming.jar \
	-D mapreduce.job.reduces=50 \
	-D mapreduce.job.maps=50 \
	-D stream.num.map.output.key.fields=1 \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D mapreduce.partition.keypartitioner.options="-k1,1" \
	-D mapreduce.partition.keycomparator.options="-k1,1" \
	-files mapper.py,reducer.py,IP2LOCATION-LITE-DB1.CSV \
	-input "/user/sandello/logs/access.log.2016-10-20" \
	-output /user/asyromyatnikov/out \
	-mapper mapper.py \
	-reducer reducer.py \
