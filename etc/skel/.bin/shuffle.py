#!/usr/bin/python3
# Shuffler for ascii art
# made by ybenel
import random
import sys
import os
path = os.environ.get('HOME')+'/.bin'
listdir = os.listdir(path) 
random.shuffle(listdir)
for i in listdir:
    name = i 
if i.endswith(".ans") :
    os.system('iconv -f 437 %s/%s | pv --quiet --rate-limit 7000'%(path,i))
    os.system('stty echo')
else:
    os.system('%s/%s'%(path,i))
    os.system('stty echo')
