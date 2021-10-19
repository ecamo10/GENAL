# GENAL
Starting to adapt to python from matlab. This is my first code.

## Genetic Algorithm
GA is a heuristic search algorithm based on the Darwin's Theory of evolution. It uses the "natural processes" of selection to identify better solutions to a function (fitness function or objective function)

### Fitness Function
For this example, the function solves the minimum point of the sphere function
y = sum( x^2 )
For the Python files, the fitness function (CostFunc) is found in the Prob 
For the Jupyter notebook, the fitness function (CostFunc) is found in the GAmain

### Process of Selection
In this process, a chromosome, which correspond to a set of solution, undergoes the differnt process of selection. Each chromosome is composed of nvar number of genes. A collection of chromosomes is called a population, where n is the number of population. This process repeats MaxIter times.  

#### Random Selection
Chromosomes are randomly selected from the population with higher probability for fitter chromosomes to be selected for the next generation.

#### Crossover
The selected chromoses are paired (parents) and crossovered to produce a pair offspring (new generation)

#### Elitism
At times, stronger genes appear in the new generation. (elit variable)

#### Mutation
And, at times, a completely different combination. (mut variable)
