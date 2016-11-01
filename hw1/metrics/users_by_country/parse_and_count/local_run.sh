#!/usr/bin/env bash
# local mode
hadoop --config /home/agorokhov/conf.empty jar /opt/hadoop/hadoop-streaming.jar \
	-D mapreduce.job.reduces=1 \
	-D mapreduce.job.maps=1 \
	-D stream.num.map.output.key.fields=1 \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D mapreduce.partition.keypartitioner.options="-k1,1" \
	-D mapreduce.partition.keycomparator.options="-k1,1" \
	-files mapper.py,reducer.py,IP2LOCATION-LITE-DB1.CSV \
	-input /hdfs/user/asyromyatnikov/access.log.dev \
	-output /hdfs/user/asyromyatnikov/out \
	-mapper ./mapper.py \
	-reducer ./reducer.py \

