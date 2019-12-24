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


    def infer_one(self,func, in_edges,out_edges):
        '''
        pick one function, and provide this function's input and output
        :param func:
        :param in_edges:
        :param out_edges:
        :return:
        '''
        pass



    def _update_graph(self):
        '''
        maintain the graph structure, including nodes, edges and the relations among them
        :return:
        '''
        pass

    def split_node(self,node):
        '''
        Split one, maybe generate a cvt node
        :param node:
        :return:
        '''
        pass

    def merge_nodes(self,nodes):
        pass


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
            if edge.out_node is Node:
                graph.nodes.append(edge.out_node)
                graph.id2node[edge.out_node.id] = edge.out_node

        return graph
