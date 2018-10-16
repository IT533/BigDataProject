import os
import re


def remove_single_data(filename):
    """
    remove row wih only one column
    """
    newfile = filename + '.new'
    with open(newfile, 'a') as fwrite:
        for line in open(filename, 'r'):
            if len(line.split('\t')) != 1:
                fwrite.write(line)
    fwrite.close()


def iter_and_remove():
    """
    iteratedly remove all data file under input
    """
    files_list = []
    for root, dirs, files in os.walk('./input/'):
        for f in files:
            if re.match('[0-9].txt', f):
                files_list.append(root + '/' + f)
    for filename in files_list:
        remove_single_data(filename)


def merge_file(outputfile):
    """
    merge subfiles into a single file
    """
    files_list = []
    for root, dirs, files in os.walk('./input/'):
        for f in files:
            if re.match('[0-9]+.txt.new', f):
                files_list.append(f)

    for fpath in files_list:
        with open(outputfile, 'a') as fwrite:
            with open('./input/' + fpath, 'r') as fread:
                fwrite.write(fread.read())
            fread.close()
        fwrite.close()


def split_file(num, inputfile, outputfile):
    """
    retrieve first num of rows from inputfile to outputfile
    """
    counter = 0
    with open(outputfile, 'w') as fwrite:
        for line in open(inputfile):
            if counter >= num:
                break
            fwrite.write(line)
            counter += 1
    fwrite.close()


def _helper_category(category):
    return '0' if category == 'Music' else '1'


def _helper_length(length):
    mean = 554788333 / 2256776
    std = 14707.75343270443
    return (length - mean) / std


def _helper_views(views):
    mean = 13673018220 / 2256776
    std = 33173.63572925056
    return (views - mean) / std


def _helper_rate(rate):
    mean = 7789495.799998452 / 2256776
    std = 1.9191814131318685
    return (rate - mean) / std


def _helper_ratings(ratings):
    mean = 36985868 / 2256776
    std = 126.28671864395315
    return (ratings - mean) / std


def _helper_comments(comments):
    mean = 21728872 / 2256776
    std = 45.9752902925119
    return (comments - mean) / std


def data_scrubbing(inputfile, outputfile):
    """
    retrieve certain column data
    Parameters: length, views, rate, ratings, comments
    Result = category
    """
    with open(outputfile, 'w') as fwrite:
        for line in open(inputfile, 'r'):
            columns = line.split('\t')
            if columns[3] not in ('Music', 'Entertainment'):
                continue
            lst = []
            lst.append(str(_helper_category(columns[3])))       # category
            lst.append(str(_helper_length(int(columns[4]))))    # length
            lst.append(str(_helper_views(int(columns[5]))))     # views
            lst.append(str(_helper_rate(float(columns[6]))))    # rate
            lst.append(str(_helper_ratings(int(columns[7]))))   # ratings
            lst.append(str(_helper_comments(int(columns[8]))))  # comments
            fwrite.write('\t'.join(lst) + '\n')
    fwrite.close()
