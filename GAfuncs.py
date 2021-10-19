def GAopti(ub,lb,nvar,n,MaxIter,hyper):
    import numpy as np
    from Prob import CostFunc,RepBounds
    ## This is a minimization problem
    elit = hyper[0]  # elitism
    mut = hyper[1] # mutation

    # initialize
    pop = InitialGen(n, nvar, ub, lb)  # new population
    # fitness function
    fit = CostFunc(pop)  # fitness
    # sort
    fit, pop = MySort(fit, pop)
    bestval = fit[0]
    bestsol = pop[0]
    vals = [bestval]

    # start of iteration
    for i in range(0, MaxIter):
        offspring = SelCross(fit, pop, n, nvar)  # Random Selection and Crossover
        offspring = Elite(offspring, pop, elit, n)  # Ellitism
        popnew = Mutation(offspring, mut, ub, lb, n,nvar)  # Mutation
        # Evaluate Fitness
        fit = CostFunc(popnew)
        fit, pop = MySort(fit, popnew)

        pop = RepBounds(pop,ub,lb,n)
        if fit[0] < bestval:
            bestval = fit[0]
            bestsol = pop[0]
        vals = np.concatenate((vals, [bestval]))

    return bestval, bestsol, vals

def InitialGen(n,nvar,ub,lb):
    import numpy as np
    import numpy.matlib
    from numpy.random import default_rng
    rng = np.random.default_rng()
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

def SelCross(fit,pop,n,nvar):
    import numpy as np
    from numpy.random import default_rng

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

def Elite(offspring,pop,elit,n):
    import numpy as np
    popnew = offspring
    nelit = int(np.ceil(elit * n))
    rep = np.random.permutation(n)[0:nelit]
    popnew[rep] = pop[range(0, nelit)]
    return popnew

def Mutation(pop,mut,ub,lb,n,nvar):
    import numpy as np
    import numpy.matlib
    from numpy.random import default_rng
    rng = np.random.default_rng()
    nmut = int(np.ceil(mut * n))
    rep = np.random.permutation(n)[0:nmut]
    popnew = pop
    ub = np.matlib.repmat(ub, nmut, 1)
    lb = np.matlib.repmat(lb, nmut, 1)
    s = rng.random((nmut, nvar)) * (ub - lb) + lb
    popnew[rep, :] = s
    return popnew

