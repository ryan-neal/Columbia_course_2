################ Open the data ###################################### 
def open_data(file = 'data.txt'):
 import numpy as np
 
 f = open(file, 'r')
 x = np.array([[0 for j in range(10)] for i in range(10000)])
 y = np.array([0 for i in range(10000)])
 
 # Loop over lines and extract variables of interest
 i = 0
 for line in f:
  columns = line.strip().split(',')
  y[i] = float(columns[0])
  for j in range(0,10):
   x[i, j] = float(columns[j+1])
  i += 1
 # x, y are numpy arrays 
 return(x, y)

################ Function to construct an LP Model ##################
def construct_lp_model(c, A, d):	
 from gurobipy import Model, LinExpr, GRB
 
 # A = numpy.array (matrix)
 # c = numpy.array (vector)
 # d = numpy.array (vector)
 
 k, n = A.shape
 
 # Creation of the gurobi model
 m = Model("sp")

 # Variables 
 x = list()
 for i in range(n):
  x.append(m.addVar(lb = -GRB.INFINITY, ub = GRB.INFINITY, name = 'x_%d' % i))
 
 # Objective Function
 objExpr = LinExpr()
 for i in range(n):
  objExpr.add(x[i], c[i])
 m.setObjective(objExpr, GRB.MAXIMIZE)

 # Constraints 
 expr={}
 for j in range(k):
  expr = LinExpr()
  for i in range(n):
   expr.add(x[i], A[j, i])
  m.addConstr(expr, GRB.LESS_EQUAL, d[j])

 # Update the model to add new entries
 m.update()
 return m


def q1():
    from gurobipy import *
    import numpy
    from functions import construct_lp_model, open_data
 
 
    x, y = open_data()
 
    N, n = len(x), len(x[0])
 
 
 
 
    # Your code goes here
 
    # You can use either one of the following two approaches
    # Approach 1: construct matrices and vectors, and use the construct_lp_model function
    m = construct_lp_model(c, A, d)
    m.optimize()
 

    for i in range(10):
        x[i]=m.getVars()[i].x
        print(x[i])
 
 # Approach 2: create loops to create decision variables and constraints (see sample example in q2.py)
 
 

 # z = optimal objective value (float)
 # b = intercept (float)
 # w = coefficient for each covariate (list or numpy array)
 #return([z, b, w])
 
print(q1())