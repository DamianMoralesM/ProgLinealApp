#!/usr/bin/env python
# @(#) $Jeannot: test1.py,v 1.11 2005/01/06 21:22:39 js Exp $
# Copywrite 2007 Stuart Mitchell
# Columnwise modelling

# Import PuLP modeler functions
from pulp import *

# A new LP problem
prob = LpProblem("test6", LpMaximize)

# objective

x1=LpVariable("x1",0,None,LpInteger)
x2=LpVariable("x2",0)
# constraints

constrain1 = LpAffineExpression([ (x1,1), (x2,3)])
constrain2 = LpAffineExpression([ (x1,6), (x2,2)])

a = LpConstraint(e=constrain1, sense=-1, name="test1", rhs=30), "PercentagesSum"
b = LpConstraint(e=constrain2, sense=-1, name="test2", rhs=20), "PercentagesSum2"




prob += 0.013*x1 + 0.008*x2, "Total Cost of Ingredients per can"
prob += a
prob += b





# Write the problem as an LP file
prob.writeLP("test6.lp")

# Solve the problem using the default solver
prob.solve()
# Use prob.solve(GLPK()) instead to choose GLPK as the solver
# Use GLPK(msg = 0) to suppress GLPK messages
# If GLPK is not in your path and you lack the pulpGLPK module,
# replace GLPK() with GLPK("/path/")
# Where /path/ is the path to glpsol (excluding glpsol itself).
# If you want to use CPLEX, use CPLEX() instead of GLPK().
# If you want to use XPRESS, use XPRESS() instead of GLPK().
# If you want to use COIN, use COIN() instead of GLPK(). In this last case,
# two paths may be provided (one to clp, one to cbc).

# Print the status of the solved LP
print("Status:", LpStatus[prob.status])
print(prob.constraints)
print(prob.objective)
# Print the value of the variables at the optimum
for v in prob.variables():
    print(v.name, "=", v.varValue)

# Print the value of the objective
print("objective=", value(prob.objective))