#!/usr/bin/env python

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

# Spark's Python has no builtins :(
"""
from builtins import (
         bytes, dict, int, list, object, range, str,
         ascii, chr, hex, input, next, oct, open,
         pow, round, super,
         filter, map, zip)
"""

from pyspark import SparkContext
from pyspark import SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

import re
import argparse
import os
import sys
import collections


def update_function(new_values, state):
    if state is None:
        state = 0
    return sum(new_values, state)


def print_counts(rdd):
    counts = collections.Counter(rdd.collectAsMap())
    print("15_second_count={n15}; 60_second_count={n60}; total_count={total};".format(**counts))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="HW3StreamMetricsComputer")
    parser.add_argument("--zookeeper", type=str)
    parser.add_argument("--topic", type=str)
    args, unknown = parser.parse_known_args()
 
    sc = SparkContext(appName="HW3StreamMetricsComputer")
    ssc = StreamingContext(sc, 15)
    ssc.checkpoint("checkpointHW3StreamMetricsComputer")

    logger = sc._jvm.org.apache.log4j
    logger.LogManager.getLogger("org"). setLevel(logger.Level.ERROR)
    logger.LogManager.getLogger("akka").setLevel(logger.Level.ERROR)

    kvs = KafkaUtils.createStream(ssc, args.zookeeper, "consumer-HW3StreamMetricsComputer", {args.topic: 4})
    lines = kvs.map(lambda x: x[1])
    parsed_lines = lines.map(lambda line: list(map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))))
    unsuccessful_queries = parsed_lines.filter(lambda words: words[5] != '200')
    n15_second_count = unsuccessful_queries.count()
    n60_second_count = unsuccessful_queries.countByWindow(60, 15)
    total_count = n15_second_count.map(lambda x: ('total', x)).updateStateByKey(update_function)
    counts = ssc.union(n15_second_count.map(lambda x: ('n15', x)),
                       n60_second_count.map(lambda x: ('n60', x)),
                       total_count)
    counts.foreachRDD(print_counts)

    ssc.start()
    ssc.awaitTermination()
