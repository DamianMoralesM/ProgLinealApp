
from pulp import *
from testing import * 

#params coeficientes funcion objetivo, restricciones , tipo de problema (max, min) 
obj = [0.013,0.008]
k = [[1,3,30, -1],[6,2,20, -1],[1,5,40, -1]] #restricciones
tipoProblema = LpMaximize

 
problema = resolver(obj,k,tipoProblema)
