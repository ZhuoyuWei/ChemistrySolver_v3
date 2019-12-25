'''
Related to math, including:
1. very basic math operators, +,-,*,/,rate,compare
'''

from .func_utils import Func

class Func_compare_greater_or_less(Func):

    def __init__(self,inputs,outputs=None):
        super.__init__(inputs,outputs)

    def run_func(self):
        pass

class Func_rate(Func):
    pass

class Func_sum(Func):
    pass