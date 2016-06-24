import math
import matplotlib.pyplot as plt

FD=1.2
OD=2.0/3.0
q=0.5
dt=2*math.pi/(OD*1000)

t=0.25*math.pi/(OD)
om=0.0
th=0.0
theta=[]
omiga=[]

while t<10000:
    for i in range(1000):
        om=om+dt*(-math.sin(th)-q*om+FD*math.sin(OD*t))
        th=th+om*dt
        if th>math.pi:
            th=th-2*math.pi
        elif th<-math.pi:
            th=th+2*math.pi
        t=t+dt
    theta.append(th)
    omiga.append(om)

plt.scatter(theta,omiga,3)
plt.xlabel('theta')
plt.ylabel('omiga')
plt.show()