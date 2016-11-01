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
import time

CWD = os.path.dirname(os.path.realpath(__file__)) 
METRICS = ("total_users", "average_session_time")
SLEEPING_TIME = 3 * 60 # 3 minutes
SLEEPING_COUNT = 20 * 5 # 5 hours of waiting


def run(date):
    processes = {}
    for metric in METRICS:
        processes[metric] = subprocess.Popen([os.path.join(CWD, metric, "run.py"),
                                              "--date={}".format(date)])
    run_metrics = METRICS
    for index in range(SLEEPING_COUNT): 
        new_run_metrics = []
        for metric in run_metrics:
            if processes[metric].poll() is not None:
                print(metric, processes[metric].poll())
            else:
                new_run_metrics.append(metric)
        if new_run_metrics:
            run_metrics = new_run_metrics
            time.sleep(SLEEPING_TIME)
        else:
            break


def main():
    previous_day = datetime.datetime.now() - datetime.timedelta(days=1)

    parser = argparse.ArgumentParser(description="All metric run script")
    parser.add_argument("--date", type=str, default=previous_day.strftime("%Y-%m-%d"))

    args = parser.parse_args()
    run(date=args.date)


if __name__ == "__main__":
    main()
