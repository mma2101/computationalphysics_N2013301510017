import math
import numpy as np
import matplotlib.pyplot as plt

class pendulum:
    def __init__(self,initTheta):
        self.g=9.8
        self.l=1.0
        self.dt=0.001        
        self.theta=[]
        self.omiga=[]
        self.t=[]
        self.theta.append(initTheta)
        self.omiga.append(0)
        self.t.append(0)
        
    def f(self,theta):
        res=-self.g*math.sin(math.pi*theta/180)/self.l
        return res
    
    def nextState(self):
        theta1=self.theta[-1]
        omiga1=self.omiga[-1]
        omiga2=omiga1+self.f(theta1)*self.dt/2
        theta3=theta1+omiga2*self.dt
        theta2=theta1+omiga1*self.dt/2
        omiga3=omiga1+self.f(theta2)*self.dt
        self.theta.append(theta3)
        self.omiga.append(omiga3)
        self.t.append(self.t[-1]+self.dt)

theta=[]
period=[]

for i in np.linspace(10,170,161):
    theta.append(i)
    p=pendulum(i)
    times=0
    deltat=[0,0,0]
    while p.t[-1]<100:
        p.nextState()
        if times<2.5:
            if p.theta[-1]*p.theta[-2]<=0:
                deltat[times]=(p.t[-1]+p.t[-2])/2
                times=times+1
    period.append(deltat[2]-deltat[0])
    #plt.plot(p.t,p.theta,label='theta='+str(i))
#plt.legend(loc="upper right", frameon=True,prop={'size':8})
#plt.xlabel('t/s')
#plt.ylabel('theta/degree')
#print theta,period
plt.plot(theta,period)
plt.xlabel('theta/degree')
plt.ylabel('period/s')
plt.show()
