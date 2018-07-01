
from pulp import *
from testing import * 
#SE SUPONE QUE ME PASAN LOS DATOS DE LA UI
#params coeficientes funcion objetivo, restricciones , tipo de problema (max, min) 
obj = [3,2]
restricciones = [[2,1,18, -1],[2,3,42, -1],[3,1,24, -1]] #restricciones
tipoProblema = LpMaximize 

 
problema = resolver(obj,restricciones,tipoProblema)
print(problema.solve())

# Print the status of the solved LP
print("Status:", LpStatus[problema.status])
print(problema.constraints)
print(problema.objective)
# Print the value of the variables at the optimum
for v in problema.variables():
    print(v.name, "=", v.varValue)
    print( problema.variables())

# Print the value of the objective
print("objective=", value(problema.objective))


