
# Import PuLP modeler functions
from pulp import *
 
def resolver(obj,k,tipoProblema):

    # A new LP problem
    prob = LpProblem("yourProblem", tipoProblema)

    # variables

    x1=LpVariable("x1",0,None,LpInteger)
    x2=LpVariable("x2",0)


    #objetive
    prob += obj[0]*x1 + obj[1]*x2, "Funcion Objetivo"

    # constraints
    constrain1 = LpAffineExpression([ (x1,k[0][0]), (x2,k[0][1])])
    constrain2 = LpAffineExpression([ (x1,k[1][0]), (x2,k[1][1])])
    constrain3 = LpAffineExpression([ (x1,k[2][0]), (x2,k[2][1])])

    a = LpConstraint(e=constrain1, sense= k[0][3], name="c1", rhs= k[0][2]) 
    b = LpConstraint(e=constrain2, sense= k[1][3], name="c2", rhs= k[1][2])
    c = LpConstraint(e=constrain3, sense= k[2][3], name="c3", rhs= k[2][2])

    #adding constrains to the problem
    prob += a
    prob += b
    prob += c


    # Write the problem as an LP file
    prob.writeLP("Calculus.lp")
    prob.solve()
    # Print the status of the solved LP
    print("Status:", LpStatus[prob.status])
    print(prob.constraints)
    print(prob.objective)
    # Print the value of the variables at the optimum

    for v in prob.variables():
        print(v.name, "=", v.varValue)
         

    # Print the value of the objective
    print("objective=", value(prob.objective))
    
    # Solve the problem using the default solver


  