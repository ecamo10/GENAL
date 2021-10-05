def CostFunc(pop):
    import numpy as np
    x=np.sum([pop.transpose()**2],axis=1) # sphere
    x = np.sum([pop.transpose() ** 2], axis=1)  # sphere
    return x[0] # output should be array

def InitialGen(n,ub,lb):
    import numpy as np
    import numpy.matlib
    from numpy.random import default_rng
    rng = np.random.default_rng()
    nvar = len(ub)  # number of variables
    ub = np.matlib.repmat(ub, n, 1)
    lb = np.matlib.repmat(lb, n, 1)
    pop = rng.random((n, nvar)) * (ub - lb) + lb
    return pop

def MySort(fit,pop):
    import numpy as np
    yin = np.argsort(fit)  # know the index of the minimum value
    ynew = fit[yin]
    popnew = pop[yin]  # arrange new population
    return ynew, popnew

def SelCross(fit,pop):
    import numpy as np
    from numpy.random import default_rng

    # random selection
    n=pop.shape[0]
    nvar=pop.shape[1]

    S = np.absolute(np.cumsum(1 / fit))
    rng = np.random.default_rng()
    s = rng.random(n) * S[-1]
    snew = s[np.argsort(s)]

    # strong parent
    XX = np.where(S >= snew[0])[0]
    parent1 = [pop[XX[0]]]
    for ii in range(1, n):
        XX = np.where(S >= snew[ii])[0]
        parent1 = np.concatenate((parent1, [pop[XX[0]]]),axis=0)  # parent1
    parent1 = parent1[np.random.permutation(n), :]
    # match parent 2
    rng = np.random.default_rng()
    s = rng.random(n) * S[-1]
    snew = s[np.argsort(s)]
    # strong parent
    XX = np.where(S >= snew[0])[0]
    parent2 = [pop[XX[0]]]
    for ii in range(1, n):
        XX = np.where(S >= snew[ii])[0]
        parent2 = np.concatenate((parent2, [pop[XX[0]]]), axis=0)  # parent1
    parent2 = parent2[np.random.permutation(n), :]
    rng = np.random.default_rng()
    a = rng.random((n, nvar))
    offspring = a * parent1 + (1 - a) * parent2

    return offspring

def Elite(offspring,pop,elit):
    import numpy as np
    n = pop.shape[0]
    popnew = offspring
    nelit = int(np.ceil(elit * n))
    rep = np.random.permutation(n)[0:nelit]
    popnew[rep] = pop[range(0, nelit)]
    return popnew

def Mutation(pop,mut,ub,lb):
    import numpy as np
    import numpy.matlib
    from numpy.random import default_rng
    rng = np.random.default_rng()
    n = pop.shape[0]
    nvar = pop.shape[1]
    nmut = int(np.ceil(mut * n))
    rep = np.random.permutation(n)[0:nmut]
    popnew = pop
    ub = np.matlib.repmat(ub, nmut, 1)
    lb = np.matlib.repmat(lb, nmut, 1)
    s = rng.random((nmut, nvar)) * (ub - lb) + lb
    popnew[rep, :] = s
    return popnew

