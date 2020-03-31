from .solver_utils import Solver
from model.graph import Graph
from model.edge import Edge
from model.node import Node

class DFSSolver(Solver):
    predicateMap=None

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

    def _dfs(self,target_edge,depth,debug_tree=None):
        target_type=target_edge.predicate
        target_type=self.predicate_alias(target_type)
        if debug_tree is not None:
            debug_tree.append(target_type)
        Func_classes=self.func_indexed_by_return_type.get(target_type,None)
        #print('debug by zhuoyu target_type={}'.format(target_type))
        #print('debug by zhuoyu func_classes={}'.format(Func_classes))
        if Func_classes is None:
            return False
        for Func_cand in Func_classes:
            #input_edges=self._collect_edges_by_neighbors(target_edge.in_node)
            #func=Func_cand(input_edges,[target_edge])
            if debug_tree is not None:
                debug_tree.append('OR')
                debug_tree.append(str(Func_cand))
            func = Func_cand(self.graph.edges, [target_edge])
            res_flag=self.graph.infer_one(func)
            unsat_parameters=self.graph.get_unsat_parameters(func)
            if res_flag==False and unsat_parameters and depth < self.max_depth:
                res_flag=True
                for para in unsat_parameters:
                    if debug_tree is not None:
                        debug_tree.append('AND')
                    sub_predicate=para[1]
                    print('sub_predict={}'.format(sub_predicate))
                    sub_target_edge=Edge(in_node=target_edge.in_node,predicate=sub_predicate,out_node=None)
                    sub_flag=self._dfs(sub_target_edge,depth+1,debug_tree)
                    print('sub_predict={} finished with {}'.format(sub_predicate,sub_flag))
                    #self.graph.print_all_edges()
                    if sub_flag == False:
                        res_flag=False
                        break
                if res_flag:
                    #input_edges = self._collect_edges_by_neighbors(target_edge.in_node)
                    #func = Func_cand(input_edges, [target_edge])
                    res_flag=self.graph.infer_one(func)



            if res_flag and target_edge.out_node is not None:
                self.graph.insert_edges([target_edge])
                break

        if debug_tree is not None:
            if res_flag:
                debug_tree.append('Solve')
            else:
                debug_tree.append('unSolve')

        return res_flag

    def predicate_alias(self, predicate):
        def _read_predicate_alias():
            predicateMap = {}
            with open('domain/resources/predicates.vocabs', 'r', encoding='utf-8') as f:
                for line in f:
                    ss = line.strip()
                    if len(ss) > 0:
                        predicateMap[ss] = ss

            # add mapping by hand
            predicateMap['mole_fraction'] = 'mole_percent'
            predicateMap['molar_ratio'] = 'molarity_percent'
            predicateMap['percent_composition'] = 'mass_percent'
            predicateMap['percent'] = 'mass_percent'
            predicateMap['ratio'] = 'mass_percent'
            predicateMap['partial_pressure'] = 'pressure'
            predicateMap['total_pressure'] = 'pressure'
            predicateMap['vapor_pressure'] = 'pressure'
            predicateMap['oxidation_state'] = 'oxidation_number'
            return predicateMap

        if self.__class__.predicateMap is None:
            self.__class__.predicateMap = _read_predicate_alias()

        if predicate in self.__class__.predicateMap:
            return self.__class__.predicateMap[predicate]
        else:
            return predicate




    def solving(self,target_edge,debug_tree=None):
        '''
        dfs on graph, the input always the edges of the graph, and after produce a new edge, put it into the edges
        :param target_edge:
        :return:
        '''

        solved_flag=self._dfs(target_edge,1,debug_tree)
        return solved_flag

