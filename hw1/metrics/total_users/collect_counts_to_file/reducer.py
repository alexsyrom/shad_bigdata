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

prev_ip = None
counter = 0

for line in sys.stdin:
    words = line.split('\t')
    cur_ip = words[0]
    if cur_ip != prev_ip:
        prev_ip = cur_ip
        counter += 1
if counter > 0:
    print(counter)


