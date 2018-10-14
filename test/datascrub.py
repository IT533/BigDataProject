import os
import re


def scrub(fname):
    newfile = fname + '.new'
    with open(newfile, 'a') as fwrite:
        for line in open(fname, 'r'):
            if len(line.split('\t')) != 1:
                fwrite.write(line)
    fwrite.close()


if __name__ == '__main__':
    files_list = []
    for root, dirs, files in os.walk('./input/'):
        for f in files:
            if re.match('[0-9].txt', f):
                files_list.append(root + '/' + f)
    for fname in files_list:
        scrub(fname)
