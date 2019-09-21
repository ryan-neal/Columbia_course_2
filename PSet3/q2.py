def q2():
 from gurobipy import Model, GRB, quicksum
 import numpy
 from functions import open_data
 
 x, y = open_data()
 N, n = len(x), len(x[0])
 
 # Creation of the model
 m = Model('LR')

 # Your code goes here
 
 # The following example is here to help you build the model (you must adapt it !!!) 
 # Define decision variables
 # z = []
 # for i in range(N):
 #  z.append(m.addVar(lb = -GRB.INFINITY, vtype=GRB.CONTINUOUS, name = 'Z_{}'.format(i), obj = 1))
 # m.update()

 # Define constraints:
 # for i in range(len(x)):
 #  m.addConstr(y[i] - z[i] , "<=" , rhs=0)  
 # m.update()
 
 # Define objective function:
 # m.setObjective(z[0], GRB.MINIMIZE)
 
 # m.update()
 # m.optimize()

 
 # Your code goes here
 
 
 # z = optimal objective value (float)
 # b = intercept (float)
 # w = coefficient for each covariate (list or numpy array)
 return([z, b, w])
