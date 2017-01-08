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

import stream_metrics


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="HW3StreamMetricsComputer")
    parser.add_argument("--host", type=str)
    parser.add_argument("--port", type=int)
    args, unknown = parser.parse_known_args()
 
    sc = SparkContext(appName="HW3NetCatStreamMetricsComputer")
    sc.addFile('stream_metrics.py')
    ssc = StreamingContext(sc, 15)
    ssc.checkpoint("checkpointNetCatHW3StreamMetricsComputer")

    logger = sc._jvm.org.apache.log4j
    logger.LogManager.getLogger("org"). setLevel(logger.Level.ERROR)
    logger.LogManager.getLogger("akka").setLevel(logger.Level.ERROR)

    lines = ssc.socketTextStream(args.host, args.port)
    stream_metrics.run(ssc, lines)
