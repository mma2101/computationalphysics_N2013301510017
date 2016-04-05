import math
import numpy as np
import matplotlib.pyplot as plt
def acce(vx,vy,y):
    'Calculate acceleration concerning attitude'
    accelerration=[0,0]
    accelerration[0]=-math.pow((1-0.0065*y/293),2.5)*0.00004*math.sqrt(vx*vx+vy*vy)*vx
    accelerration[1]=-math.pow((1-0.0065*y/293),2.5)*0.00004*math.sqrt(vx*vx+vy*vy)*vy-9.8
    return accelerration
def traj(angle,velocity):
    'Calculate the trajectory'
    dt=0.01
    speed=[[],[]]
    trajectory=[[],[]]
    speed[0].append(velocity*math.cos(math.pi*angle/180))
    speed[1].append(velocity*math.sin(math.pi*angle/180))
    trajectory[0].append(0)
    trajectory[1].append(0)    
    while trajectory[1][-1]>=0:
        trajectory[0].append(trajectory[0][-1]+speed[0][-1]*dt)
        trajectory[1].append(trajectory[1][-1]+speed[1][-1]*dt)
        speed[0].append(speed[0][-1]+acce(speed[0][-1],speed[1][-1],trajectory[1][-1])[0]*dt)
        speed[1].append(speed[1][-1]+acce(speed[0][-1],speed[1][-1],trajectory[1][-1])[1]*dt)
    trajectory[0][-1]=(trajectory[0][-2]-trajectory[1][-2]*trajectory[0][-1]/trajectory[1][-1])/(1-trajectory[1][-2]/trajectory[1][-1])
    trajectory[1][-1]=0
    return trajectory
maxangle=0
maxdis=0
for angle in np.linspace(0,90,901):
    x=traj(angle,700)
    if x[0][-1]>maxdis:
        maxdis=x[0][-1]
        maxangle=angle
print 'Maxangle=',maxangle
y=traj(maxangle,700)
plt.plot(y[0],y[1])
plt.xlabel('x/m')
plt.ylabel('y/m')
plt.xlim(0,30000)
text='angle='+str(maxangle)
plt.annotate(text,xy=(21200,4300),xytext=(23000,5000),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))
plt.show()
