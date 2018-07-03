from matplotlib import pyplot                                               
import numpy as np
# x = (c-b*y)/a
def f(x, c1, c2, b):
    return (b - c1*x)/c2

def graficar(k):
    x = np.arange(0.0, 2.0, 0.01)
    y1 = f(x, k[0][0], k[0][1], k[0][2])
    y2 = f(x, k[1][0], k[1][1], k[1][2])
    y3 = f(x, k[2][0], k[2][1], k[2][2])
    pyplot.plot(x, y1)
    pyplot.plot(x, y2)
    pyplot.plot(x, y3)
    pyplot.show()
