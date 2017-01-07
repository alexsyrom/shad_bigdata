#!/shared/anaconda/bin/python
# encoding=utf8

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
"""from builtins import (
         bytes, dict, int, list, object, range, str,
         ascii, chr, hex, input, next, oct, open,
         pow, round, super,
         filter, map, zip)
"""
from pyspark import SparkContext
from pyspark import SparkConf
import re
import argparse
import datetime
import os
import sys
import subprocess


if __name__ == '__main__':
    conf = SparkConf().setAppName("ProfileLikedThreeDays").set("spark.ui.port", "11695")
    sc = SparkContext(conf=conf)
    # print('''*******************\n\n WOW \n\n************************''')

    previous_day = datetime.datetime.now() - datetime.timedelta(days=1)
    parser = argparse.ArgumentParser(description="Profile Liked Three Days script")
    parser.add_argument("--date", type=str, default=previous_day.strftime("%Y-%m-%d"))
    args, unknown = parser.parse_known_args()
    date = datetime.datetime.strptime(args.date, "%Y-%m-%d")
    unique_liked_users = None
    
    for shift in range(3):
        one_day_log = sc.textFile("/user/sandello/logs/access.log." + date.strftime("%Y-%m-%d"))
        parsed_log = one_day_log.map(lambda line: list(map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line))))
        successful_queries = parsed_log.filter(lambda words: words[5] == '200')
        resources = successful_queries.map(lambda words: words[4].split()[1])
        liked = resources.filter(lambda resource: resource.find('?like=1') != -1)
        liked_users = liked.map(lambda resource: resource.split('?', 1)[0][1:])
        # we don't need next line, because intersection method removes duplicates
        # unique_liked_users = liked_users.distinct()
        if unique_liked_users is None:
            unique_liked_users = liked_users
        else:
            unique_liked_users = unique_liked_users.intersection(liked_users)
        unique_liked_users.persist()
        date -= datetime.timedelta(days=1)
    unique_liked_users_count = unique_liked_users.count()

    with open(args.date, 'w') as output:
        print(unique_liked_users_count, file=output)
    subprocess.check_call(['hdfs', 'dfs', '-put',
        args.date, '/user/asyromyatnikov/hw1/metrics/profile_liked_three_days/results/{}'.format(args.date)])

    sc.stop()

