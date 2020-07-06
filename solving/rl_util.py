from model.graph import Graph
from model.edge import Edge
from model.node import Node


'''
Action Space
Each Action has a class
The following is old action space class

class RLActionSpaces(object):

    @classmethod
    def exec_function(cls,state):
        pass

    @classmethod
    def merge_nodes(cls):
        pass

    @classmethod
    def split_node(cls):
        pass

    @classmethod
    def remove_a_fact(cls):
        pass

    @classmethod
    def extract_from_text(cls):
        pass

    @classmethod
    def infer_a_fact(cls):
        pass


    action_list=[exec_function,merge_nodes,split_node,remove_a_fact,extract_from_text,infer_a_fact]
'''

class RL_Action(object):

    def __init__(self,state,text=None,graph=None,function_list=None):
        self.state=state
        self.text=text
        self.graph=graph
        self.function_list=function_list

    def sub_actions(self):
        raise NotImplementedError

    def applying(self):
        raise NotImplementedError

class Exec_Function_Action(RL_Action):

    def __init__(self,state,text=None,graph=None,function_list=None):
        super(Exec_Function_Action).__init__(state,text,graph,function_list)
        if function_list is None or len(function_list) < 1:
            print("Invalid: There is no function during run Exec_Function_Action")
            raise NotImplementedError
        if graph is None:
            print("Invalid: There is no graph during run Exec_Function_Action")
            raise NotImplementedError


    def sub_actions(self):
        '''
        Need choose a (valid) function from function list
        :return:
        '''
        return self.function_list

    def applying(self):
        #pick a function
        function=self.function_list[0]
        func = function(self.graph.edges, [None]) #There is no target_edge
        self.graph.infer_one(func)


class Merge_Nodes_Action(RL_Action):

    def __init__(self, state, text=None, graph=None, function_list=None):
        super(Merge_Nodes_Action).__init__(state, text, graph, function_list)
        if graph is None or graph.nodes is None or len(graph.nodes)<2:
            print("Invalid: There is no graph during run Exec_Function_Action")
            raise NotImplementedError

    def sub_actions(self):
        '''
        Need choose two node from graph and merge them
        :return:
        '''
        return self.graph.nodes



    def applying(self):
        # pick two nodes
        node_1=self.graph.nodes[0]
        node_2=self.graph.nodes[1]

        #graph add a function to mereg nodes safely
        self.graph.merge_nodes([node_1,node_2])


class Split_Node_Action(RL_Action):

    def __init__(self, state, text=None, graph=None, function_list=None):
        super(Split_Node_Action).__init__(state, text, graph, function_list)
        if graph is None or graph.nodes is None or len(graph.nodes) < 1:
            print("Invalid: There is no graph during run Exec_Function_Action")
            raise NotImplementedError

    def sub_actions(self):
        '''
        Need choose one node and split it into two nodes
        :return:
        '''
        return self.graph.nodes

    def applying(self):
        # pick one nodes
        node= self.graph.nodes[0]


        # graph add a function to split a node safely
        self.graph.split_node(node)


'''
    @classmethod
    def remove_a_fact(cls):
        pass
'''

class Remove_Fact_Action(RL_Action):

    def __init__(self, state, text=None, graph=None, function_list=None):
        super(Exec_Function_Action).__init__(state, text, graph, function_list)
        if graph is None or graph.edges is None or len(graph.edges) < 1:
            print("Invalid: There is no graph during run Exec_Function_Action")
            raise NotImplementedError

    def sub_actions(self):
        '''
        Need choose one edge to delete
        :return:
        '''
        return self.graph.edges

    def applying(self):
        # pick one nodes
        edge=self.graph.edges[0]
        # graph remove an edge from edges

'''
    @classmethod
    def extract_from_text(cls):
        pass
'''

class Extract_Fact_Action(RL_Action):

    def __init__(self, state, text=None, graph=None, function_list=None):
        super(Extract_Fact_Action).__init__(state, text, graph, function_list)
        if text is None:
            print("Invalid: There is no text during run Extract_Fact_Action")
            raise NotImplementedError


    def sub_actions(self):

        return None

    def applying(self):
        #extractor extracts a fact from text
        fact=None
        edge=None #convert fact to edge
        self.graph.edges.append(edge)
        #update graph

'''  
    @classmethod
    def infer_a_fact(cls):
        pass
'''
class Infer_Fact_Action(RL_Action):

    def __init__(self, state, text=None, graph=None, function_list=None):
        super(Infer_Fact_Action).__init__(state, text, graph, function_list)
        if graph is None:
            print("Invalid: There is no graph during run Infer_Fact_Action")
            raise NotImplementedError


    def sub_actions(self):

        return None

    def applying(self):
        #infer a fact from graph
        fact=None
        edge=None #convert fact to edge
        self.graph.edges.append(edge)
        #update graph


'''
Policy Estimator
'''
class Estimator_Policy_Fix:

    def __init__(self,action_list,function_list):
        self.action_list=action_list
        self.function_list=function_list


    def predicate(self,state):
        if type(state) is Graph:
            probs=[0]*len(self.action_list)
            for i,action in enumerate(self.action_list):
                if action is Exec_Function_Action:
                    probs[i]=1
        else:
            prob=1/len(self.function_list)
            probs=[prob]*len(self.function_list)
        return probs


'''
reward function
'''
def correct_answer_reward(target,answer,check_correct_function):
    if check_correct_function(target,answer):
        return 100
    else:
        return 0