"""
Gaussian Distribution
"""
from mrjob.job import MRJob


class MRSTD(MRJob):
    def mapper(self, _, line):
        columns = line.split('\t')
        value = float(columns[6])
        yield (int(round(value/0.125, 0)), 1)

    def reducer(self, key, values):
        yield (key, sum(values))


if __name__ == '__main__':
    MRSTD.run()
