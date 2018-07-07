from matplotlib import pyplot                                               
import numpy as np
# x = (c-b*y)/a
def f(x, c1, c2, b):
    if c2 == 0:
        return b / c1
    return (b - c1*x)/c2

def puntosTabla(obj, k, n):
    # Primero se obtienen los puntos factibles: A * X = B
    rest = k
    rest.append([1, 0, 0, 1])
    rest.append([0, 1, 0, 1])
    data = []
    i = 0
    while i < (len(rest) - 1):
        c11 = rest[i][0]
        c12 = rest[i][1]
        b1 = rest[i][2]
        j = i + 1
        while j < len(rest):
            c21 = rest[j][0]
            c22 = rest[j][1]
            b2 = rest[j][2]
            A = np.array([[c11, c12], [c21, c22]])
            B = np.array([[b1], [b2]])
            print('Matriz A')
            print(A)
            print('Matriz B')
            print(B)
            # X = [[x1], [x2]]
            try:
                X = np.linalg.inv(A).dot(B)
                print('Resultado')
                arr = [X[0][0], X[1][0]]
                print(arr)
                if not (arr in data):
                    data.append(arr)
            except:
                print("Restricciones {0} y {1} incompatibles".format(i, j))
            j += 1
        i += 1
    print('Los puntos son')
    print(data)
    # Luego se tienen que obtener los valores de slacks por cada punto
    i = 0
    rest.pop()
    rest.pop()
    while i < len(data):
        x1 = data[i][0]
        x2 = data[i][1]
        # Para x1 y x2 se deben recorrer todas las restricciones
        j = 0
        while j < len(rest):
            c1 = rest[j][0]
            c2 = rest[j][1]
            b = rest[j][2]
            signo = rest[j][3] * (-1)
            s = (b - c1 * x1 - c2 * x2) * signo
            data[i].append(s)
            j += 1
        i += 1
    print('Agregando slacks')
    print(data)
    # Ahora agregamos el valor de Z en cada punto
    i = 0
    while i < len(data):
        x1 = data[i][0]
        x2 = data[i][1]
        c1 = obj[0]
        c2 = obj[1]
        z = (c1 * x1) + (c2 * x2)
        data[i].append(z)
        i += 1
    print('La tabla final')
    print(data)
    return data

def graficar(obj, k, solucion, n):
    fig, (ax, tabax) = pyplot.subplots(nrows=2)

    # Definiciones para la tabla
    data = puntosTabla(obj, k, n)
    columns = ("x1", "x2", "x3", "x4", "x5", "z")
    rows = []
    char = ord('A')
    i = 0
    while i < len(data):
        rows.append(chr(char))
        char += 1
        i += 1
    tabax.axis("off")
    tabax.table(cellText=data, rowLabels=rows, colLabels=columns, loc="center") #, bbox=[0.0,-0.5,1,0.3])

    # Definiciones para la gráfica
    # Obtenemos el punto optimo con valor mayor de X
    i = 0
    arr = []
    while i < len(data):
        arr.append(data[i][0])
        i += 1
    xmax = max(arr)
    xmax = xmax + 0.4 * xmax
    x = np.arange(0, xmax, 0.01)
    # ax.set_ylim(0)
    # ax.axis('equal')
    ax.autoscale(enable = True, axis = 'y', tight = True)
    i = 0
    while i < n:
        y = f(x, k[i][0], k[i][1], k[i][2])
        if k[i][1] == 0:
            ax.axvline(x = y)
        else:
            ax.plot(x, y)
        i += 1 
    # Dibujamos los ejes
    ax.axvline(x = 0, color = 'k')
    ax.axhline(y = 0, color = 'k')
    # Marcamos el optimo
    ax.plot([solucion[1]], [solucion[2]], marker='o', markersize=3, color="red")
    # Titulo de la gráfica
    s = "{0} | Z = {1} | x1 = {2} | x2 = {3}".format(solucion[3], solucion[0], solucion[1], solucion[2])
    ax.set_title(s)
    pyplot.tight_layout()
    pyplot.show()
