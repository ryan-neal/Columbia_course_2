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
    import numpy as np
 
 
    x, y = open_data()
    print(x[0])
    print(y[0])
    N, n = len(x), len(x[0])
    print(N, n)
 
    
 
 
 
    # Your code goes here
 
    # You can use either one of the following two approaches
    # Approach 1: construct matrices and vectors, and use the construct_lp_model function
    #m = construct_lp_model(np.zeros(1000), x[:1000], y[:1000])
    #m.optimize()
    m = Model("mae")
    
    w = np.array([None for j in range(n)])
    for k in range(n):
        w[k] = m.addVar(name='w(%d)' %k )
    m.update()
    
    
    #m.setObjective(np.dot(w, x), GRB.MINIMIZE)
    
    
    # Approach 2: create loops to create decision variables and constraints (see sample example in q2.py)
    
    
    
    #for v in m.getVars():
    #    print('%s %g' % (v.varName, v.x))
    #    print('Obj: %g' % m.objVal)
 

 # z = optimal objective value (float)
 # b = intercept (float)
 # w = coefficient for each covariate (list or numpy array)
 #return([z, b, w])
 
print(q1())

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
