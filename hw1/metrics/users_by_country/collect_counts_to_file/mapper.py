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


session_time = 0
session_count = 0

for line in sys.stdin:
    count, time = list(map(int, line.split('\t')))
    session_count += count
    session_time += time

print(session_count, session_time, sep='\t')
