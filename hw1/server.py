#!/shared/anaconda/bin/python
#encoding=utf8

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
import getpass
import hashlib
import random
import struct
import os.path

from flask import Flask, request, abort, jsonify

app = Flask(__name__)
app.secret_key = "wow_wow_key"

METRICS = ({'name': 'total_users',
            'type': int},

            {'name': 'average_session_time',
             'type': float},
            )


def iterate_between_dates(start_date, end_date):
    span = end_date - start_date
    for i in xrange(span.days + 1):
        yield start_date + datetime.timedelta(days=i)


@app.route("/")
def index():
    return "OK!"


@app.route("/api/hw1")
def api_hw1():
    start_date = request.args.get("start_date", None)
    end_date = request.args.get("end_date", None)
    if start_date is None or end_date is None:
        abort(400)
    start_date = datetime.datetime(*map(int, start_date.split("-")))
    end_date = datetime.datetime(*map(int, end_date.split("-")))

    result = {}
    for date in iterate_between_dates(start_date, end_date):
        str_date = date.strftime("%Y-%m-%d")
        result[str_date] = {metric['name']: None for metric in METRICS}
        for metric in METRICS:
            filename = "./metrics/{}/results/{}".format(metric['name'], str_date)
            if os.path.exists(filename):
                with open(filename, 'r') as f:
                    metric_value = metric['type'](f.readline())
                result[str_date][metric['name']] = metric_value

    return jsonify(result)


def login_to_port(login):
    """
    We believe this method works as a perfect hash function
    for all course participants. :)
    """
    hasher = hashlib.new("sha1")
    hasher.update(login)
    values = struct.unpack("IIIII", hasher.digest())
    folder = lambda a, x: a ^ x + 0x9e3779b9 + (a << 6) + (a >> 2)
    return 10000 + reduce(folder, values) % 20000


def main():
    parser = argparse.ArgumentParser(description="HW 1 Alexey Syromyatnikov")
    parser.add_argument("--host", type=str, default="127.0.0.1")
    parser.add_argument("--port", type=int, default=login_to_port(getpass.getuser()))
    parser.add_argument("--debug", action="store_true", dest="debug")
    parser.add_argument("--no-debug", action="store_false", dest="debug")
    parser.set_defaults(debug=False)

    args = parser.parse_args()
    app.run(host=args.host, port=args.port, debug=args.debug)

if __name__ == "__main__":
    # print(login_to_port(getpass.getuser()))
    # >>> 11695
    main()
