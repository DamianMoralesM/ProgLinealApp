from matplotlib import pyplot                                               
import numpy as np
# x = (c-b*y)/a
def f(x, c1, c2, b):
    if c2 == 0:
        return b / c1
    return (b - c1*x)/c2

def graficar(k, solucion, n):
    fig, (ax, tabax) = pyplot.subplots(nrows=2)
    # Definiciones para la gráfica
    x = np.arange(0.0, 2.0, 0.01)
    
    i = 0
    while i < n:
        y = f(x, k[i][0], k[i][1], k[i][2])
        if k[i][1] == 0:
            ax.axvline(x = y)
        else:
            ax.plot(x, y)
        i += 1 

    #y1 = f(x, k[0][0], k[0][1], k[0][2])
    #ax.plot(x, y1)
    #y2 = f(x, k[1][0], k[1][1], k[1][2])
    #ax.plot(x, y2)
    #y3 = f(x, k[2][0], k[2][1], k[2][2])
    #ax.plot(x, y3)
    
    # Marcamos el optimo
    ax.plot([solucion[1]], [solucion[2]], marker='o', markersize=3, color="red")
    # Titulo de la gráfica
    s = "{0} | Z = {1} | x1 = {2} | x2 = {3}".format(solucion[3], solucion[0], solucion[1], solucion[2])
    ax.set_title(s)

    # Definiciones para la tabla
    columns = ("x1", "x2", "x3", "x4", "x5", "z")
    rows = ["A", "B", "C"]
    data = [
        [11, 12, 13, 14, 15, "z1"],
        [21, 22, 23, 24, 25, "z2"],
        [31, 32, 33, 34, 35, "z3"]
    ]
    tabax.axis("off")
    tabax.table(cellText=data, rowLabels=rows, colLabels=columns, loc="center") #, bbox=[0.0,-0.5,1,0.3])
    pyplot.tight_layout()
    pyplot.show()
