import math
import matplotlib.pyplot as plt

dt=0.001
t=0

class planets:
    def __init__(self,m1,m2,x1,y1,x2,y2,vx1,vy1,vx2,vy2):
        self.m1=m1
        self.m2=m2
        self.x1=[x1]
        self.x2=[x2]
        self.y1=[y1]
        self.y2=[y2]
        self.vx1=vx1
        self.vx2=vx2
        self.vy1=vy1
        self.vy2=vy2
        self.r=math.sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2))
    
    def move(self):
        self.vx1=self.vx1+dt*1000*(self.x2[-1]-self.x1[-1])*self.m2/(self.r*self.r*self.r)
        self.vx2=self.vx2+dt*1000*(self.x1[-1]-self.x2[-1])*self.m1/(self.r*self.r*self.r)
        self.vy1=self.vy1+dt*1000*(self.y2[-1]-self.y1[-1])*self.m2/(self.r*self.r*self.r)
        self.vy2=self.vy2+dt*1000*(self.y1[-1]-self.y2[-1])*self.m1/(self.r*self.r*self.r)
        self.x1.append(self.x1[-1]+dt*self.vx1)
        self.x2.append(self.x2[-1]+dt*self.vx2)
        self.y1.append(self.y1[-1]+dt*self.vy1)
        self.y2.append(self.y2[-1]+dt*self.vy2)
        self.r=math.sqrt((self.x1[-1]-self.x2[-1])*(self.x1[-1]-self.x2[-1])+(self.y1[-1]-self.y2[-1])*(self.y1[-1]-self.y2[-1]))

a=planets(1,5,10,10,-10,-5,-10,0,5,-5)        
while t<10:
    a.move()
    t=t+dt
plt.scatter(a.x1,a.y1,2,color='red',label='m='+str(a.m1))
plt.scatter(a.x2,a.y2,2,color='blue',label='m='+str(a.m2))
plt.annotate('',xy=(10-10*2,10),xytext=(10,10),arrowprops=dict(arrowstyle="->"))
plt.annotate('',xy=(-10+5*2,-5-5*2),xytext=(-10,-5),arrowprops=dict(arrowstyle="->"))
plt.legend(loc="upper right", frameon=True,prop={'size':15})
plt.show()