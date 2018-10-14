import os
import re

files_list = []
for root, dirs, files in os.walk('./input/'):
    for f in files:
        if re.match('[0-9].txt.new', f):
            files_list.append(root + '/' + f)

for fpath in files_list:
    foo = fpath.split('/')
    newpath = './input/' + foo[2] + foo[3]
    os.rename(fpath, newpath)
