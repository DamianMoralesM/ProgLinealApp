
 #Import PuLP modeler functions
from pulp import *

# Resolucion= Problema(coeficienteObjetivo,restricciones,tipoRestricciones,tipoDeProblema)
coeficienteObjetivo = [3,5]
restricciones = [[2,3,5],[4,5,9],[2,4,6]]

tipoDeProblema = LpMaximize;
#coeficienteObjetivo = c1, c2, c3... Ci
#restricciones = r1, r2, r3.... Ri .. 
#R= a1, a2, a3.... ai.. bi

#Tipo problema = LPminimize, LPmaximaze

#

# Create the 'prob' variable to contain the problem data
prob = LpProblem("el nombre de tu problema",LpMaximize)


x1=LpVariable("var1",0,None,LpInteger)
x2=LpVariable("var2",0,None,LpInteger)

# Definimos funcion objetivo
prob += coeficienteObjetivo[0]*x1 + coeficienteObjetivo[1]*x2, "obj"


# Definimos restricciones
prob += restricciones[0][0]*x1 + restricciones[0][1]*x2 <= restricciones[0][2], "Res1"
prob += restricciones[1][0]*x1 + restricciones[1][1]*x2 <= restricciones[1][2], "Res2"
prob += restricciones[2][0]*x1 + restricciones[2][1]*x2 <= restricciones[2][2], "Res3"

# The problem data is written to an .lp file
prob.writeLP("test.lp")

# The problem is solved using PuLP's choice of Solver
prob.solve()


# The status of the solution is printed to the screen
print("Status:", LpStatus[prob.status])

# Each of the variables is printed with it's resolved optimum value
for v in prob.variables():
    print(v.name, "=", v.varValue)
    
# The optimised objective function value is printed to the screen
print("El optimo es = ", value(prob.objective))
print(restricciones)