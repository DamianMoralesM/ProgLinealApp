
from pulp import *
from testing import * 

#params coeficientes funcion objetivo, restricciones , tipo de problema (max, min) 
obj = [0.013,0.008]
k = [[1,3,30, -1],[6,2,20, -1],[1,5,40, -1]] #restricciones
tipoProblema = LpMaximize

 
problema = resolver(obj,k,tipoProblema)
problema.solve()
# Print the status of the solved LP
print("Status:", LpStatus[problema.status])
print(problema.constraints)
print(problema.objective)
# Print the value of the variables at the optimum
for v in problema.variables():
    print(v.name, "=", v.varValue)

# Print the value of the objective
print("objective=", value(problema.objective))