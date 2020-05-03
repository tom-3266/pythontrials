import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
fig,ax=plt.subplots()
ax.scatter(x,np.sin(x));