import os
import re

files_list = []
for root, dirs, files in os.walk('./input/'):
    for f in files:
        if re.match('[0-9]+.txt.new', f):
            files_list.append(f)


for fpath in files_list:
    with open('./input/allfile.txt.new', 'a') as fwrite:
        with open('./input/' + fpath, 'r') as fread:
            fwrite.write(fread.read())
        fread.close()
    fwrite.close()

print('done')
