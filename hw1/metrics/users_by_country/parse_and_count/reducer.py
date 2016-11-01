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
import pandas as pd

reload(sys)  
sys.setdefaultencoding('utf8')

country_ip_limits = pd.read_csv("IP2LOCATION-LITE-DB1.CSV", header=None, names=['lower', 'upper', 'code', 'name'])


def get_numeric_ip(ip):
    byte_0, byte_1, byte_2, byte_3 = list(map(int, ip.split(".")))
    dec = byte_0 << 24 | byte_1 << 16 | byte_2 << 8 | byte_3 << 0
    return dec


def get_country_by_ip(ip):
    numeric_ip = get_numeric_ip(ip)
    country = country_ip_limits[
                (country_ip_limits.lower <= numeric_ip) &
                (numeric_ip <= country_ip_limits.upper)].name.item()
    return country


def main():
    prev_ip = None
    for line in sys.stdin:
        words = line.split('\t')
        cur_ip = words[0]
        if prev_ip != cur_ip:
            country = get_country_by_ip(cur_ip)
            print(country, sep='\t')
        prev_ip = cur_ip


if __name__ == "__main__":
    main()
