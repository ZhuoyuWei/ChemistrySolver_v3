class Graph:

    def __init__(self):
        '''
        Description/Definition of Graph Structure and Properties
        '''
        self.nodes=[]
        self.edges=[]
        self.situated=True


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
        graph=Graph()
        #################
        ##Non Implement##
        #################
        return graph
