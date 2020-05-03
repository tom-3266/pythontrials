import numpy as np
import matplotlib.pyplot as plt
prices = {"Almond":10,"peanut":8,"cashew":12}
x=np.random.randn(1000)
fig,((ax1,ax2),(ax3,ax4)) = plt.subplots(nrows=2,ncols=2,figsize=(10,5))
ax1.plot(x,x/2);
ax2.scatter(np.random.random(10),np.random.random(10));
ax3.bar(prices.keys(),prices.values());
ax4.hist(np.random.randn(1000));