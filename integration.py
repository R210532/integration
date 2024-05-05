import numpy as np
from matplotlib import pyplot as plt
x=np.array([1,1,1,1,-1,-1,-1,-1])
l=len(x)
y=[]
for i in range(0,l):
    integral=np.sum(x[:i])
    y.append(integral)
plt.plot(x)
plt.plot(y)
plt.show()
