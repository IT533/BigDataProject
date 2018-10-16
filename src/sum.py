"""
Sum
"""
from mrjob.job import MRJob


class MRSum(MRJob):
    def mapper(self, _, line):
        columns = line.split('\t')
        dic = dict()
        dic['length'] = int(columns[4])    # length
        dic['views'] = int(columns[5])     # views
        dic['rate'] = float(columns[6])    # rate
        dic['ratings'] = int(columns[7])   # ratings
        dic['comments'] = int(columns[8])  # comments
        dic['count'] = 1
        for key, value in dic.items():
            yield (key, value)

    def reducer(self, key, values):
        yield (key, sum(values))


if __name__ == '__main__':
    MRSum.run()
