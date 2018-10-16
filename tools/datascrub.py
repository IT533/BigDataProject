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


def helper_category(category):
    return category


def helper_length(length):
    return length


def helper_views(views):
    return views


def helper_rate(rate):
    return rate


def helper_ratings(ratings):
    return ratings


def helper_comments(comments):
    return comments


def data_scrubbing(inputfile, output_parameters, output_result, lst):
    """
    retrieve certain column data
    Parameters: category, length, views, rate, ratings, comments
    Result = Age
    """
    with open(output_parameters) as fwrite_para:
        with open(output_result) as fwrite_result:
            for line in open(inputfile):
                columns = line.split('\t')
                # output parameters flush out
                fwrite_result.write(columns[2])

                # output result flush out
                lst = []
                lst.append(helper_category(columns[3]))  # category
                lst.append(helper_length(columns[4]))  # length
                lst.append(helper_views(columns[5]))  # views
                lst.append(helper_rate(columns[6]))  # rate
                lst.append(helper_ratings(columns[7]))  # ratings
                lst.append(helper_comments(columns[8]))  # comments
                fwrite_para.write('\t'.join(lst))
        fwrite_result.close()
    fwrite_para.close()
