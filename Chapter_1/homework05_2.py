import matplotlib.pyplot as plt
N=[]
t=[]
dt=0.001
N.append(input('Initial N='))
t.append(0)
time=input('Time=')
a=input('a=')
b=input('b=')
while t[-1]<time:
    N.append(N[-1]+a*N[-1]*dt-b*N[-1]*N[-1]*dt)
    t.append(t[-1]+dt)
plt.plot(t,N,color='red',linewidth=2.0,linestyle="-",label="Numerical")
plt.legend(loc="upper right", frameon=True)
plt.xlabel('t')
plt.ylabel('N')
plt.ylim(0,1.5*N[-1])
plt.show()