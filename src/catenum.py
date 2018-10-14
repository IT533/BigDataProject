"""
Category counting
"""
from mrjob.job import MRJob


class MRCateCount(MRJob):
    def mapper(self, _, line):
        cate = line.split('\t')[3]
        yield (cate, 1)

    def reducer(self, cate, counts):
        yield (cate, sum(counts))


if __name__ == '__main__':
    MRCateCount.run()
