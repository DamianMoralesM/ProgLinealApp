import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(4,2)
columns = ('Frequency','Hz')
rows = ['# %d' % p for p in (1,2,3,4)] 

fig, (ax, tabax) = plt.subplots(nrows=2)

ax.plot(data[:,0], data[:,1], '-') #plot x-y
ax.axis([0, 1, 0, 1.2]) #range for x-y plot
ax.set_xlabel('Hz')

tabax.axis("off")
the_table = tabax.table(cellText=data,rowLabels=rows, colLabels=columns,
                      loc='center')
plt.subplots_adjust(bottom=0.05)
plt.show()