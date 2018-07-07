from matplotlib import pyplot                                               
import numpy as np

x = np.arange(0, 10, 0.01)
arrx = [3, 0, 1, 0]
arry = [3, 0, 1 ,2]

pyplot.fill_between(arrx, arry)
pyplot.show()