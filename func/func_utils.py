class Func:

    name = "Func"
    description = "Basic Function"

    def __init__(self):

        self.inputs = None
        self.outputs = None

    def _sat_running(self):
        '''
        check whether the inputs can satisfy this func running conditions
        :return: True | False
        '''
        raise NotImplementedError

    def func(self):
        '''
        The real functional implement
        :return:
        '''
        if not self._sat_running():
            return None

        raise NotImplementedError

