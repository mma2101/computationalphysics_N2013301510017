import matplotlib.pyplot as plt
import numpy as np
# numerical solution
Nn=[]
tn=[]
dt=0.01
Nn.append(input('Initial N='))
tn.append(0)
time=input('Time=')
a=input('a=')
while tn[-1]<time:
    Nn.append(Nn[-1]*(a*dt+1))
    tn.append(tn[-1]+dt)
# analytical solution
ta=np.linspace(0,time,100)
Na=Nn[0]*np.exp(a*ta)
plt.plot(tn,Nn,color='red',linewidth=2.0,linestyle="-",label="Numerical")
plt.plot(ta,Na,color='blue',linewidth=2.0,linestyle="-",label="Analytical")
plt.legend(loc="upper left", frameon=True)
plt.xlabel('t')
plt.ylabel('N')
plt.show()