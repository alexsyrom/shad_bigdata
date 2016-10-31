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

reload(sys)  
sys.setdefaultencoding('utf8')

MAX_SESSION_TIME = 30 * 60

prev_ip = None
session_count = 0 
session_time = 0
prev_time = 0

for line in sys.stdin:
    words = line.split('\t')
    cur_ip = words[0]
    time = int(words[1])
    if cur_ip != prev_ip:
        session_count += 1
        prev_ip = cur_ip
    elif time > prev_time + MAX_SESSION_TIME:
        session_count += 1
    else:
        old_session_time = session_time
        session_time += time - prev_time
        if session_time < old_session_time:
            print(session_time, old_session_time, time, prev_time)
    prev_time = time

if session_count > 0:
    print(session_count, session_time, sep='\t')


