from .solver_utils import Solver
from model.graph import Graph
from model.edge import Edge
from model.node import Node

class DFSSolver(Solver):
    def __init__(self,graph,func_list,max_depth=5):
        '''
        For all functions, build a indexing, the connections are based on return value's semantic type
        '''

        self.graph=graph
        self.func_list=func_list
        self.func_indexed_by_return_type={}
        self.max_depth=max_depth

        self._build_func_index()

    def _build_func_index(self):
        self.func_indexed_by_return_type={}
        if self.func_list:
            for func in self.func_list:
                if not func.output_type in self.func_indexed_by_return_type:
                    self.func_indexed_by_return_type[func.output_type]=[]
                self.func_indexed_by_return_type[func.output_type].append(func)

    def _collect_edges_by_neighbors(self,target_node):
        edge_buffer=target_node.edges
        for edge in target_node.edges:
            if type(edge.in_node) is Node and edge.in_node.id != target_node.id:
                edge_buffer+=edge.in_node.edges
            elif type(edge.out_node) is Node and edge.out_node.id != target_node.id:
                edge_buffer+=edge.out_node.edges
        return edge_buffer

    def _dfs(self,target_edge,depth):
        target_type=target_edge.predicate
        Func_classes=self.func_indexed_by_return_type.get(target_type,None)
        #print('debug by zhuoyu target_type={}'.format(target_type))
        #print('debug by zhuoyu func_classes={}'.format(Func_classes))
        if Func_classes is None:
            return False
        for Func_cand in Func_classes:
            #input_edges=self._collect_edges_by_neighbors(target_edge.in_node)
            #func=Func_cand(input_edges,[target_edge])
            func = Func_cand(self.graph.edges, [target_edge])
            res_flag=self.graph.infer_one(func)
            unsat_parameters=self.graph.get_unsat_parameters(func)
            if res_flag==False and unsat_parameters and depth < self.max_depth:
                res_flag=True
                for para in unsat_parameters:
                    sub_predicate=para[1]
                    print('sub_predict={}'.format(sub_predicate))
                    sub_target_edge=Edge(in_node=target_edge.in_node,predicate=sub_predicate,out_node=None)
                    sub_flag=self._dfs(sub_target_edge,depth+1)
                    print('sub_predict={} finished with {}'.format(sub_predicate,sub_flag))
                    self.graph.print_all_edges()
                    if sub_flag == False:
                        res_flag=False
                        break
                if res_flag:
                    #input_edges = self._collect_edges_by_neighbors(target_edge.in_node)
                    #func = Func_cand(input_edges, [target_edge])
                    res_flag=self.graph.infer_one(func)

            if res_flag and target_edge.out_node is not None:
                self.graph.insert_edges([target_edge])
                return True

        return res_flag








    def solving(self,target_edge):
        '''
        dfs on graph, the input always the edges of the graph, and after produce a new edge, put it into the edges
        :param target_edge:
        :return:
        '''

        solved_flag=self._dfs(target_edge,1)
        return solved_flag

