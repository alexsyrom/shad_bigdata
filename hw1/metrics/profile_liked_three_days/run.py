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
    previous_day = datetime.datetime.now() - datetime.timedelta(days=1)

    parser = argparse.ArgumentParser(description="A metric run script")
    parser.add_argument("--date", type=str, default=previous_day.strftime("%Y-%m-%d"))

    args = parser.parse_args()
    run(date=args.date)


if __name__ == "__main__":
    main()
