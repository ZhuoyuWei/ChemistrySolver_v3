class Node:
    def __init__(self):
        self.id='0000-0000-0000-0000' #a uid
        self.is_cvt = False

        self.in_edges=[]
        self.out_edges=[]
        self.edges=self.in_edges+self.out_edges
        #need other indexing for graph algorithms?

        #buildin property
        self.concept='Substance' #the type of Node
        self.name='\ce{C2O}'
        self.default_value=None #?
