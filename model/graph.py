from .node import Node
from .edge import Edge

class Graph:

    def __init__(self,nodes=[],edges=[],situated=True):
        '''
        Description/Definition of Graph Structure and Properties
        '''
        self.nodes=nodes
        self.edges=edges
        self.situated=situated

        self.id2node={}


    def infer_one(self,func):
        '''
        pick one function, and provide this function's input and output
        :param func:
        :return:
        '''
        run_res_flag=func.run_func()
        return run_res_flag

    def get_unsat_parameters(self,func):
        return func.input_unsat_map

    def insert_edges(self,edges):
        self.edges+=edges
        self._update_graph_by_edges()

    def _update_graph(self):
        '''
        maintain the graph structure, including nodes, edges and the relations among them
        :return:
        '''
        pass

    def _update_graph_by_nodes(self):
        '''
        if the node list is updated out of the graph, you need call this function to update the corresponding edges
        :return:
        '''
        self.edges=[]
        for node in self.nodes:
            node.update_edges()
            self.edges+=node.edges

    def _update_graph_by_edges(self):
        '''
        if the edge list is updated out of the graph, you need call this function to update the corresponding nodes
        :return:
        '''
        self.nodes=[]
        self.id2node={}
        for edge in self.edges:
            self.nodes.append(edge.in_node)
            self.id2node[edge.in_node.id]=edge.in_node
            if edge.out_node is Node:
                self.nodes.append(edge.out_node)
                self.id2node[edge.out_node.id] = edge.out_node

    def split_node(self,node):
        '''
        Split one, maybe generate a cvt node
        :param node:
        :return:
        '''
        pass

    def merge_nodes(self,nodes):
        pass

    #debug
    def print_all_edges(self):
        for i,edge in enumerate(self.edges):
            print('{}\t{}\t{}\t{}'.format(i,edge.in_node.id,edge.predicate,edge.out_node))

    def add_name_into_edges_for_all_node(self):
        for node in self.nodes:
            name_edge=Edge(in_node=node,predicate='name',out_node=node.name)
            node.out_edges.append(name_edge)
        self._update_graph_by_nodes()



    @classmethod
    def build_graph_from_edges(cls,edges):
        '''
        Build a graph instance from edges.
        The edges can contains both question_varibles and conditions
        :param edges:
        :return:
        '''
        graph=Graph(edges=edges)

        for edge in edges:
            graph.nodes.append(edge.in_node)
            graph.id2node[edge.in_node.id]=edge.in_node
            if type(edge.out_node) is Node:
                graph.nodes.append(edge.out_node)
                graph.id2node[edge.out_node.id] = edge.out_node

        return graph
