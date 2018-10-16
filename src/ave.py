"""
Average
"""
from mrjob.job import MRJob
from mrjob.step import MRStep


class MRAverage(MRJob):
    def steps(self):
        return [
            MRStep(mapper=self.mapper_mean,
                   reducer_init=self.reducer_mean_init,
                   reducer=self.reducer_mean,
                   reducer_final=self.reducer_mean_final)
        ]

    def mapper_mean(self, _, line):
        columns = line.split('\t')
        dic = dict()
        dic['length'] = int(columns[4])    # length
        dic['views'] = int(columns[5])     # views
        dic['rate'] = float(columns[6])    # rate
        dic['ratings'] = int(columns[7])   # ratings
        dic['comments'] = int(columns[8])  # comments
        for key, value in dic.items():
            yield (key, value)

    def reducer_mean_init(self):
        self.count = 0
        self.total = 0
        self.key = ''

    def reducer_mean(self, key, values):
        self.key = key
        for value in values:
            self.count += 1
            self.total += value

    def reducer_mean_final(self):
        yield (self.key, self.total / self.count)


if __name__ == '__main__':
    MRAverage.run()
