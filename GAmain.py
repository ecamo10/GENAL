import numpy as np
from GAfuncs import *
from Prob import *

N=5      # number of population
MaxIter=10   # maximum iteration
elit=0.1    # elitism
mut=0.2      # mutation
hyper=[elit,mut]

# currently the problem is Sphere
ub, lb, dim = DefBounds()
bestval, bestsol, vals = GAopti(ub,lb,dim,N,MaxIter,hyper)

print('best value is:', bestval)
print('best solution is:', bestsol)
#print(vals)
#matplotlib.pyplot.plot(range(0,MaxIter),vals)