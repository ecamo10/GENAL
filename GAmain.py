import numpy as np
from GAfuncs import InitialGen, CostFunc, MySort, SelCross, Mutation,Elite

lb=[0, 0]
ub=[1, 1]
nvar=len(ub) # number of variables
n=50      # number of population
MaxIter=10   # maximum iteration
elit=0.05    # elitism
mut=0.1      # mutation

#### This is a minimization problem
# initialize
pop = InitialGen(n,ub,lb)# new population
# fitness function
fit = CostFunc(pop)# fitness
# sort
fit, pop = MySort(fit,pop)
bestval=fit[0]
bestsol=pop[0]
vals=[bestval]
print(bestval)
print(bestsol)

# start of iteration
for i in range(0,MaxIter):
    offspring = SelCross(fit,pop) # Random Selection and Crossover
    offspring=Elite(offspring,pop,elit)# Ellitism
    popnew = Mutation (offspring, mut, ub, lb)# Mutation
    # Evaluate Fitness
    fit = CostFunc(popnew)
    fit, pop = MySort(fit,popnew)
    if fit[0]<bestval:
        bestval=fit[0]
        bestsol=pop[0]
    vals = np.concatenate((vals, [bestval]))

print('best value is:', bestval)
print('best solution is:', bestsol)
print(vals)
#matplotlib.pyplot.plot(range(0,MaxIter),vals)