class Func:

    name = "Func"
    description = "Basic Function"
    output_type="None"

    def __init__(self):

        self.inputs = None
        self.outputs = None

    def _sat_running(self):
        '''
        check whether the inputs can satisfy this func running conditions
        :return: True | False
        '''
        raise NotImplementedError

    def run_func(self):
        '''
        The real functional implement, run immediately
        :return:
        '''
        if not self._sat_running():
            return None

        raise NotImplementedError


    def run_func_by_solving_equation(self):
        '''
        The real functional implement
        :return:
        '''
        if not self._sat_running():
            return None

        raise NotImplementedError
