"""
Top 10 Views
"""
from mrjob.job import MRJob
import heapq


class MRTop10Views(MRJob):
    def mapper_init(self):
        self.view_lst = []

    def mapper(self, _, line):
        vID = line.split('\t')[0]
        view = line.split('\t')[5]
        context = {'vID': vID, 'view': int(view)}
        self.view_lst.append(context)
        self.view_lst = heapq.nlargest(10, self.view_lst, lambda s: s['view'])

    def mapper_final(self):
        yield (None, self.view_lst)

    def reducer(self, key, values):
        top_10_view = []
        for value in values:
            for context in value:
                top_10_view.append(context)
                top_10_view = heapq.nlargest(10, top_10_view, lambda s: s['view'])

        for value in top_10_view:
            yield (key, value)


if __name__ == '__main__':
    MRTop10Views.run()
