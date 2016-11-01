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

HDFS_SOURCE_PATH = "/user/sandello/logs/access.log."
HDFS_DEST_PATH = "/user/asyromyatnikov/hw1/metrics/users_by_country/"
LOCAL_DEST_PATH = os.path.expanduser("~/src/shad_bigdata/hw1/metrics/users_by_country/")
CWD = os.path.dirname(os.path.realpath(__file__)) 


def run(date):
    input_path = HDFS_SOURCE_PATH + date
    output_path = os.path.join(HDFS_DEST_PATH, "parse_and_count")
    real_output_path = '/hdfs' + output_path
    if os.path.exists(real_output_path):
        shutil.rmtree(real_output_path)
    subprocess.check_call([os.path.join(CWD, "parse_and_count/prod_run.sh"),
            input_path, output_path], cwd=os.path.join(CWD, "parse_and_count"))

    input_path = output_path 
    output_path = os.path.join(HDFS_DEST_PATH, "collect_counts_to_file")
    real_output_path = '/hdfs' + output_path
    if os.path.exists(real_output_path):
        shutil.rmtree(real_output_path)
    subprocess.check_call([os.path.join(CWD, "collect_counts_to_file/prod_run.sh"),
            input_path, output_path], cwd=os.path.join(CWD, "collect_counts_to_file"))
    shutil.rmtree('/hdfs' +  input_path)

    input_dir = real_output_path
    input_path = os.path.join(input_dir, "part-00000")
    output_dir = '/hdfs' + os.path.join(HDFS_DEST_PATH, "results")
    output_path = os.path.join(output_dir, date)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    shutil.copyfile(input_path, output_path)
    shutil.rmtree(input_dir)

    input_path = output_path
    output_dir = os.path.join(LOCAL_DEST_PATH, "results")
    output_path = os.path.join(output_dir, date)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    shutil.copyfile(input_path, output_path)


def main():
    previous_day = datetime.datetime.now() - datetime.timedelta(days=1)

    parser = argparse.ArgumentParser(description="A metric run script")
    parser.add_argument("--date", type=str, default=previous_day.strftime("%Y-%m-%d"))

    args = parser.parse_args()
    run(date=args.date)


if __name__ == "__main__":
    main()
