import math
import matplotlib.pyplot as plt

dx=1.0
dt=0.1
v=10.0
k=0.1
t=0.0
r=v*dt/dx
y3=range(101)
y2=range(101)
y1=range(101)
for i in range(101):
    y3[i]=math.exp(-k*(30.0-i)*(30.0-i))+2*math.sin(i)*math.exp(-k*(70.0-i)*(70.0-i))
    #y3[i]=math.exp(-k*(30.0-i)*(30.0-i))+2*math.exp(-k*(70.0-i)*(70.0-i))
    y1[i]=y3[i]
    y2[i]=y3[i]

plt.figure(figsize=(10,5))
#plt.plot(y3)

while t<3:
    for i in range(101):
        y1[i]=y2[i]
        y2[i]=y3[i]
    for j in range(101):
        if j>0 and j<100:
            y3[j]=(y2[j+1]+y2[j-1])-y1[j]
    #y3[0]=0.0
    #y3[100]=0.0
    t=t+dt

plt.plot(y3,label='t='+str(t-dt))
plt.ylabel('y')
plt.xlabel('x')
plt.legend(loc="upper right", frameon=True,prop={'size':20})
#plt.xlim([90,95])
plt.ylim([-2.5,2.5])
plt.show()
