from .node import Node
class Edge:
    def __init__(self,predicate=None,in_node=None,out_node=None):
        self.predicate=predicate
        self.in_node=in_node
        self.out_node=out_node #can be a node or a <value,unit> pair

    def __str__(self):
        return '{}({},{})'.format(self.predicate,self.in_node,self.out_node)
    def __repr__(self):
        return '{}({},{})'.format(self.predicate,self.in_node,self.out_node)

    @classmethod
    def generate_edge_from_triplet(cls,triplet):
        in_node=Node(name=triplet[0])
        predicate=triplet[1]
        value=triplet[2]
        edge=Edge(predicate=predicate,in_node=in_node,out_node=value)
        in_node.out_edges.append(edge)
        in_node.update_edges()
        return edge

