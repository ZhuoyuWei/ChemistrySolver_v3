import copy
from domain.chemistry_utils import PU, UnitConvertor

class Func:

    name = "Func"
    description = "Basic Function"
    output_type="None" #should be a predicate

    input_sat_maps=[["node_1","mass","g"],["node_1","molarity","g"],["node2","mass","g"],["target","mass","g"]] #just an example


    def __init__(self,inputs,outputs=None):

        self.inputs = inputs
        self.outputs = outputs
        self.target_node=None
        self.input_unsat_map=None
        self.parameters=[]

    def sat_running(self):
        return self._sat_running(self.__class__.input_sat_maps)

    def _sat_running(self,current_input_sat_maps):
        '''
        check whether the inputs can satisfy this func running conditions, and update self.parameters by self.inputs
        so you can call unsat_parameters following calling sat_running
        :return: True | False
        '''
        self.target_node=self.outputs[0].in_node
        self.target_property=self.outputs[0].predicate #useless

        self.input_unsat_map = copy.deepcopy(current_input_sat_maps)
        self.parameters = [None]*len(self.input_unsat_map)

        fill_count=0
        for input_edge in self.inputs:
            #print('DEBUG in sat_running {} flag = {} and type = {}'.format(input_edge.out_node,
            #        (type(input_edge.out_node) is PU and input_edge.out_node.value is None),
            #         type(input_edge.out_node)))
            if type(input_edge.out_node) is PU and input_edge.out_node.value is None:
                continue
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

        print('DEBUG in sat_running: parameters={}'.format(self.parameters))

        if fill_count >= len(self.parameters):
            self.input_unsat_map=[]
            self.all_unit_converting(current_input_sat_maps)
            return True
        else:
            tmplist=self.input_unsat_map
            self.input_unsat_map=[]
            for i in range(len(tmplist)):
                if self.parameters[i] is None:
                    self.input_unsat_map.append(tmplist[i])
            return False

    def unit_converting(self,old_pu,target_unit):
        if isinstance(old_pu,PU) and old_pu.value is not None and \
            old_pu.unit is not None and old_pu.unit != target_unit:
            target=UnitConvertor.converting(old_pu,target_unit)
        else:
            target=old_pu
        return target

    def all_unit_converting(self,current_input_sat_maps):

        for i,parameter in enumerate(self.parameters):
            print(current_input_sat_maps[i])
            self.parameters[i].out_node=self.unit_converting(self.parameters[i].out_node,
                                                             current_input_sat_maps[i][2])


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


    def __str__(self):
        return self.__class__.name


