import copy
class Func:

    name = "Func"
    description = "Basic Function"
    output_type="None"

    input_sat_maps=[["node_1","mass"],["node_1","molarity"],["node2","mass"],["target","mass"]] #just an example



    def __init__(self):

        self.inputs = None
        self.outputs = None
        self.target_node=None
        self.input_unsat_map=None
        self.parameters=[]

    def sat_running(self):
        '''
        check whether the inputs can satisfy this func running conditions, and update self.parameters by self.inputs
        so you can call unsat_parameters following calling sat_running
        :return: True | False
        '''
        self.target_node=self.outputs[0].in_node
        self.target_property=self.outputs[0].predicate #useless

        self.input_unsat_map = copy.deepcopy(self.__class__.input_sat_maps)
        self.parameters = [None]*len(self.input_unsat_map)

        fill_count=0
        for input_edge in self.inputs:
            for i,parameter in enumerate(self.input_unsat_map):
                if self.parameters[i]:
                    continue
                if input_edge.predicate == parameter[1] and input_edge.out_node is not None:
                    if (input_edge.in_node.id == self.target_node.id and parameter[0] == 'target')\
                            or (input_edge.in_node.id != self.target_node.id):
                        self.parameters[i]=input_edge
                        fill_count+=1
                        break
            if fill_count >= len(self.parameters):
                break

        if fill_count >= len(self.parameters):
            self.input_unsat_map=[]
            return True
        else:
            tmplist=self.input_unsat_map
            self.input_unsat_map=[]
            for i in range(len(tmplist)):
                if self.parameters[i] is None:
                    self.input_unsat_map.append(tmplist[i])
            return False















    def run_func(self):
        '''
        The real functional implement, run immediately
        :return:
        '''
        if not self.sat_running():
            return None

        raise NotImplementedError


    def run_func_by_solving_equation(self):
        '''
        The real functional implement
        :return:
        '''

        raise NotImplementedError
