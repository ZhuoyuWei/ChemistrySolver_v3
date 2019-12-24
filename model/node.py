import uuid

class Node:
    def __init__(self,id=None,name=None):
        if id is not None:
            self.id=id #a uid
        else:
            self.id=str(uuid.uuid1())

        self.is_cvt = False

        self.in_edges=[]
        self.out_edges=[]
        self.edges=self.in_edges+self.out_edges
        #need other indexing for graph algorithms?

        #buildin property
        self.concept='Substance' #the type of Node
        self.name=name
        self.default_value=None #?

    def update_edges(self):
        #add name and concept to edges
        #name_flag=False
        #concept_flag=False
        #for edge in self.out_edges:
            #if edge.predicate == 'name':
                #name_flag=True
            #if edge.predicate == 'concept':
                #concept_flag=True
        self.edges = self.in_edges + self.out_edges
