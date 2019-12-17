'''

Molarity(x,y) ^ Mole(x,z) => Volume(x,a)
a=f_volume(Molarity(x,y),Mole(x,z))


If we know the following ideal gas equation:
    PV=nRT
How to solve different

'''

from .func_utils import Func

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
        

    def func(self):
        '''
        The real functional implement
        :return:
        '''
        if not self._sat_running():
            return None

        raise NotImplementedError


