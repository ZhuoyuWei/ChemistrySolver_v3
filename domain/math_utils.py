import numpy as np

'''

def solve_linear_equations(a,b):
    a=np.array(a)
    b=np.array(b)
    #x = np.linalg.solve(a, b)
    x = np.linalg.lstsq(a, b)
    return x.tolist()
'''

def solve_linear_equations_dfs(a,b,x,depth):
    for value in range(1,11):
        x[depth] = value

        if depth == len(x)-1:
            ax=np.matmul(a,x)
            #print(x)
            if (ax==b).all():
                return x
        else:
            res=solve_linear_equations_dfs(a, b, x, depth+1)
            if res is not None:
                return res

def solve_linear_equations(a,b):
    a = np.array(a,dtype=int)
    b = np.array(b,dtype=int)
    x=np.zeros(len(a[0]),dtype=int)
    x=solve_linear_equations_dfs(a,b,x,0)
    if x is None:
        x = np.ones(len(a[0]), dtype=int)
    return x.tolist()


#unit test
if __name__ == '__main__':
    #Na + H2O = NaOH + H2
    a=[[1,0,-1,0,1,2,3],
       [0,2,-1,-2,1,2,3],
       [0,1,-1,0,1,2,3]]
    b=[0,0,0]
    import time
    start=time.time()
    x=solve_linear_equations(a,b)
    end=time.time()
    print(x)
    print(str(end-start))

