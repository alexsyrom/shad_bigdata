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


def main():
    prev_country = None
    country_users_counter = 0
    for line in sys.stdin:
        words = line.split('\t')
        cur_country = words[0]
        cur_number = int(words[1])
        if cur_country != prev_country:
            if country_users_counter > 0:
                print(prev_country, country_users_counter, sep='\t')
            country_users_counter = cur_number 
        else:
            country_users_counter += cur_number 
        prev_country = cur_country

    if country_users_counter > 0:
        print(prev_country, country_users_counter, sep='\t')


if __name__ == '__main__':
    main()
