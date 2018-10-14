"""
Top 10 Views
"""
from mrjob.job import MRJob
import heapq

class MRTop10Views(MRJob):
    # def mapper_init(self):
    #     # MRJob.__init__(args = None)
    #     self.view_lst = []
    #     self.top_10_view = []

    def mapper(self, _, line):
        view_lst = []
        vID = line.split('\t')[0]
        view = line.split('\t')[5]
        context = {'vID': vID, 'view': view}
        view_lst.append(context)
        top_10_lst = heapq.nlargest(10,view_lst,lambda s:s['view'])
        yield ('', top_10_lst)

    def reducer(self, key, top_10_lst):
        top_10_view = []        
        top_10_view = top_10_view + list(top_10_lst)
        top_10_view = heapq.nlargest(10,top_10_view,lambda s:s['view'])
        yield ('', top_10_view)


if __name__ == '__main__':
    MRTop10Views.run()
