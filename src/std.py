"""
Standard Deviation
"""
from mrjob.job import MRJob
from math import sqrt


class MRSTD(MRJob):
    def mapper(self, _, line):
        mean_lt = 554788333 / 2256776
        mean_vw = 13673018220 / 2256776
        mean_rt = 7789495.799998452 / 2256776
        mean_rg = 36985868 / 2256776
        columns = line.split('\t')
        mean_co = 21728872 / 2256776
        dic = dict()
        dic['length'] = pow(int(columns[4]) - mean_lt, 2)
        dic['views'] = pow(int(columns[5]) - mean_vw, 2)
        dic['rate'] = pow(float(columns[6]) - mean_rt, 2)
        dic['ratings'] = pow(int(columns[7]) - mean_rg, 2)
        dic['comments'] = pow(int(columns[8]) - mean_co, 2)
        for key, value in dic.items():
            yield (key, value)

    def reducer(self, key, values):
        N = 2256776 - 1
        yield (key, sqrt(sum(values) / N))


if __name__ == '__main__':
    MRSTD.run()
