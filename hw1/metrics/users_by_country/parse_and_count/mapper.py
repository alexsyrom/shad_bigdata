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
import pandas as pd

reload(sys)  
sys.setdefaultencoding('utf8')

sys.stdin = codecs.getreader('utf8')(sys.stdin, errors='ignore')

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
    for line in sys.stdin:
        words = list(map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line)))
        if words[5] == "200":
            country = get_country_by_ip(words[0])
            print(country, words[0], sep='\t')


if __name__ == "__main__":
    main()
