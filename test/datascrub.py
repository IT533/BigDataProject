def scrub(fname):
    newfile = fname + '.new'
    with open(newfile, 'a') as fwrite:
        for line in open(fname, 'r'):
            if len(line.split('\t')) != 1:
                fwrite.write(line)
    fwrite.close()


if __name__ == '__main__':
    fname = './input/0301/0.txt'
    scrub(fname)
