class Graph:

    '''
    Description/Definition of Graph Structure and Properties
    '''
    def __init__(self):
        self.nodes=[]
        self.edges=[]
        self.situated=True

    '''
    pick one function, and provide this function's input and output
    '''
    def infer_one(self,func, in_edges,out_edges):
        pass


    '''
    maintain the graph structure, including nodes, edges and the relations among them
    '''
    def _update_graph(self):
        pass

    '''
    Split one, maybe generate a cvt node
    '''
    def _split_node(self,node):
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
