#!/usr/bin/env bash
# local mode
hadoop --config /home/agorokhov/conf.empty jar /opt/hadoop/hadoop-streaming.jar \
	-D mapreduce.job.reduces=10 \
	-D mapreduce.job.maps=10 \
	-D stream.num.map.output.key.fields=2 \
	-D mapreduce.job.output.key.comparator.class=org.apache.hadoop.mapreduce.lib.partition.KeyFieldBasedComparator \
	-D mapreduce.partition.keypartitioner.options=-k1,1 \
	-D mapreduce.partition.keycomparator.options="-k1,2" \
	-files mapper.py,reducer.py \
	-input /hdfs/user/asyromyatnikov/access.log.dev3 \
	-output /hdfs/user/asyromyatnikov/out \
	-mapper ./mapper.py \
	-reducer ./reducer.py \
	-partitioner org.apache.hadoop.mapred.lib.KeyFieldBasedPartitioner

