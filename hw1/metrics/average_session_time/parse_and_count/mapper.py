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

for line in sys.stdin:
    words = list(map(''.join, re.findall(r'\"(.*?)\"|\[(.*?)\]|(\S+)', line)))
    if words[5] == "200":
        date, sep, other = words[3].partition(':')
        time, sep, other = other.partition(' ')
        # hours, minutes, seconds = list(map(int, time.split(':')))
        # time_in_seconds = seconds + 60 * (minutes + 60 * hours)
        print(words[0], time, sep='\t')
