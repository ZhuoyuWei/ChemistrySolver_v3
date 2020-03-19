class A:
    def __init__(self):
        self.t=0
    @classmethod
    def create_A(cls):
        a=A()
        a.t+=1
        return a


for i in range(100):
    b=A.create_A()
    print(b.t)