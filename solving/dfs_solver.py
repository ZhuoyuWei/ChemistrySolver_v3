from .solver_utils import Solver

class DFSSolver(Solver):
    def __init__(self,graph,func_list):
        '''
        For all functions, build a indexing, the connections are based on return value's semantic type
        '''

        self.graph=graph
        self.func_list=func_list
        self.func_indexed_by_return_type={}

    def _build_func_index(self):
        self.func_indexed_by_return_type={}
        if self.func_list:
            for func in self.func_list:
                if not func.output_type in self.func_indexed_by_return_type:
                    self.func_indexed_by_return_type[func.output_type]=[]
                self.func_indexed_by_return_type[func.func.output_type]=func


    def solving(self,target_edge):
        '''
        dfs on graph
        :param target_edge:
        :return:
        '''
        pass