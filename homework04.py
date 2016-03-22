import matplotlib.pyplot as plt
na=[]
nb=[]
t=[]
tao=1.0
dt=0.1
na.append(input("Initial Na:"))
nb.append(input("Initial Nb:"))
time=input("time:")
t.append(0)
while t[-1]<time:
    dna=(nb[-1]-na[-1])*dt/tao
    dnb=(na[-1]-nb[-1])*dt/tao
    na.append(na[-1]+dna)
    nb.append(nb[-1]+dnb)
    t.append(t[-1]+dt)
plt.plot(t,na,color="red",linewidth=2.0,linestyle="-",label="Na")
plt.plot(t,nb,color="yellow",linewidth=2.0,linestyle="-",label="Nb")
plt.plot([0,time],[na[-1]]*2,color="blue",linewidth=1.5,linestyle="-.")
plt.legend(loc="upper right", frameon=True)
plt.show()