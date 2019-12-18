'''

Molarity(x,y) ^ Mole(x,z) => Volume(x,a)
a=f_volume(Molarity(x,y),Mole(x,z))


If we know the following ideal gas equation:
    PV=nRT
How to solve different

'''

from .func_utils import Func
from domain.chemistry_utils import PU,CE

NAME2CE={"sodium carbonate":"Na2CO3"}

class Func_Name2CE(Func):
    '''
    just as an example
    '''


    def __init__(self,inputs,outputs=None):
        super.__init__()
        self.inputs = inputs
        self.outputs = outputs

        ###for func calc
        self.substance_name=None



    def _sat_running(self):
        '''
        check whether the inputs can satisfy this func running conditions
        :return: True | False
        '''
        flag=False
        target_node=self.outputs[0].in_node
        for input in self.inputs:
            if input.in_node.id == target_node.id and input.property == 'substance_name':
                flag=True
                self.substance_name=input.out_node
                break

        return flag

    def func(self):
        if not self._sat_running():
            return None
        ce_str=NAME2CE.get(self.substance_name)
        return CE(ce_str)



class Func_Mole2Atom(Func):

    def __init__(self,inputs,outputs=None):
        super.__init__()
        self.inputs = inputs
        self.outputs = outputs

    def _sat_running(self):
        '''
        check whether the inputs can satisfy this func running conditions
        :return: True | False
        '''
        if len(self.outputs)<1 or self.outputs[0] is None:
            return False
        return True
        

    def func(self):
        '''
        The real functional implement
        :return:
        '''
        if not self._sat_running():
            return None

        raise NotImplementedError


