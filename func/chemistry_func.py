'''

Molarity(x,y) ^ Mole(x,z) => Volume(x,a)
a=f_volume(Molarity(x,y),Mole(x,z))


If we know the following ideal gas equation:
    PV=nRT
How to solve different

'''

from .func_utils import Func
from domain.chemistry_utils import PU,CE,ChemicalSubstance
from parse.chemistry_parse import ParseSubstance

NAME2CE={"sodium carbonate":"Na2CO3"}

class Func_Name2CE(Func):
    '''
    just as an example, CE is a text
    '''

    name = "Name2CE"
    description = "Convert a substance name to its chemical equation (CE)"
    output_type="Chemistry_Substance"
    input_sat_maps = [["target", "name"]]


    def __init__(self,inputs,outputs=None):
        super.__init__()
        self.inputs = inputs
        self.outputs = outputs









    def run_func(self):
        if not self.sat_running():
            return None
        ce_str=NAME2CE.get(self.parameters[0].out_node,None)
        if ce_str == None:
            ce_str=self.parameters[0].out_node
        chemistry_substance=ParseSubstance(ce_str)
        self.outputs[0].out_node=chemistry_substance
        return (chemistry_substance is not None)

class Func_Mole2Atom(Func):

    name = "Mole2Atom"
    description = "Calculate the number of Atom from the Mole"
    output_type="Atom"

    def __init__(self,inputs,outputs=None):
        super.__init__()
        self.inputs = inputs
        self.outputs = outputs

    '''
    def _sat_running(self):
        if len(self.outputs)<1 or self.outputs[0] is None:
            return False
        return True
    '''

    def run_func(self):
        '''
        The real functional implement
        :return:
        '''
        if not self._sat_running():
            return None

        raise NotImplementedError


