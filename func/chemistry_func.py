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
DICT_MolarMassElement={"K":39.0983,"Cl":35.453,"P":30.9738,"O":15.999,"C":12.010,"H":1.007,"N":14.0067,"He":4.002,"F":18.998,"Al":26.981,"Na":22.989,"Mg":24.304,"S":32.059,"Br":79.901}

class Func_Name2CE(Func):
    '''
    just as an example, CE is a text
    '''

    name = "Name2CE"
    description = "Convert a substance name to its chemical equation (CE)"
    output_type="Chemistry_Substance"
    input_sat_maps = [["target", "name"]]


    def __init__(self,inputs,outputs=None):
        super().__init__(inputs,outputs)


    def run_func(self):
        if not self.sat_running():
            return False
        ce_str=NAME2CE.get(self.parameters[0].out_node,None)
        print('in ce parser, ce_str={},name={}'.format(ce_str,self.parameters[0].out_node))
        if ce_str == None:
            ce_str=self.parameters[0].out_node
        chemistry_substance=ParseSubstance(ce_str)
        print('chemistry_substance = {}'.format(chemistry_substance))
        self.outputs[0].out_node=chemistry_substance
        return (chemistry_substance is not None)

class Func_Mole2Atom(Func):

    name = "Mole2Atom"
    description = "Calculate the number of Atom from the Mole"
    output_type="Atom"

    def __init__(self,inputs,outputs=None):
        super().__init__()
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

class Func_CE2MolarMass(Func):
    '''
    just as an example, CE is a text
    '''

    name = "Name2MolarMass"
    description = "from the CE of a substance to its MolarMass"
    output_type="MolarMass"
    input_sat_maps = [["target", "Chemistry_Substance"]]


    def __init__(self,inputs,outputs=None):
        super().__init__(inputs,outputs)


    def run_func(self):
        if not self.sat_running():
            return False
        chemistry_substance=self.parameters[0].out_node
        print('cs in molarmass')
        sum=0
        for element_pair in chemistry_substance.elements:
            element=element_pair['element']
            element_count=element_pair['count']
            print(element_pair)
            sum+=DICT_MolarMassElement.get(element,0)*element_count

        self.outputs[0].out_node=PU(value=sum,unit='g/mole')
        return True

class Func_Mass2Mole(Func):
    '''
    just as an example, CE is a text
    '''

    name = "Mass2Mole"
    description = "mole=mass/molar_mass"
    output_type="Mole"
    input_sat_maps = [["target", "MolarMass"],["target","Mass"]]


    def __init__(self,inputs,outputs=None):
        super().__init__(inputs,outputs)


    def run_func(self):
        if not self.sat_running():
            return False
        molarMass=self.parameters[0].out_node
        mass=self.parameters[1].out_node
        mole_value=mass.value/molarMass.value
        self.outputs[0].out_node=PU(value=mole_value,unit='mole')
        return True


