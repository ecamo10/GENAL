def CostFunc(pop):
    import numpy as np
    x = np.sum([pop.transpose()**2],axis=1) # sphere
    x = np.sum([pop.transpose() ** 2], axis=1)  # sphere
    return x[0] # output should be array

def DefBounds():
    # Sphere Problem
    lb = [0, 0]
    ub = [1, 1]
    dim = len(ub)  # number of variables
    return lb,ub,dim

def RepBounds(pop,ub,lb,n):
    import numpy as np
    ub = np.matlib.repmat(ub, n, 1)
    lb = np.matlib.repmat(lb, n, 1)
    pop1=np.minimum(pop,ub)
    pop2=np.maximum(pop1,lb)
    return pop2