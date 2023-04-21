from random import *
from functions import *

n = 5     # Population size 
dim = 2   # Problem dimension
Tmax = 10 # Maximun number od iterations

# ------ PROBLEM INITALIZATION ------
pop = [[1, 0, 0, 0], # Initial population
       [1 ,0 ,1 ,0],
       [1, 1, 1 ,1]]

r = random() # Valor random entre 0 y 1
q = random() # Valor random entre 0 y 1

bestMatr =[]  # Memory matrix
fit = fitness(pop)

for i in range(Tmax):
    print (i)