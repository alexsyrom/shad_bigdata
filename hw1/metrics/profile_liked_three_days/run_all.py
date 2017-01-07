#!/shared/anaconda/bin/python
# encoding=utf8

from __future__ import print_function
from __future__ import division
from __future__ import unicode_literals
from builtins import bytes, chr
from builtins import str
from builtins import dict
from builtins import object
from builtins import range
from builtins import map
from builtins import zip
from builtins import filter 

import sys
import re
import codecs

reload(sys)  
sys.setdefaultencoding('utf8')

sys.stdin = codecs.getreader('utf8')(sys.stdin, errors='ignore')


import argparse
import datetime
import subprocess
import shutil
import os
import os.path


def iterate_between_dates(start_date, end_date):
    span = end_date - start_date
    for i in xrange(span.days + 1):
        yield start_date + datetime.timedelta(days=i)


def run(date):
    real_output_path = '/hdfs/user/asyromyatnikov/hw1/metrics/profile_liked_three_days/results/{}'.format(date)
    if os.path.exists(real_output_path):
        os.remove(real_output_path)
    subprocess.check_call(['spark-submit', 'metric.py', 
                            '--master', 'yarn-client', 
                            '--num-executors', '6', 
                            '--driver-memory', '2g', 
                            '--executor-memory', '8g', 
                            '--executor-cores', '4', 
                            '--conf', "spark.yarn.executor.memoryOverhead=1024", 
                            '--date', date])


def main():
    start_date = datetime.datetime(2016, 10, 10) 
    end_date = datetime.datetime(2017, 01, 06) 
    for date in iterate_between_dates(start_date, end_date):
        run(date.strftime("%Y-%m-%d"))
    

if __name__ == "__main__":
    main()
