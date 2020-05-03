# 0. import matplot lib
import matplotlib.pyplot as plt

# 1.import data
x=[1,2,3,4]
y=[11,22,33,44]

#2.setup plot
fig,ax=plt.subplots(figsize=(10,10)) #dimention of figsize

#3.plot data
ax.plot(x,y);

#4.customize plot
ax.set(title="Simple plot",xlabel="x-axis",ylabel="y-axis")

#5.save and show
fig.savefig("sampleplot.png")