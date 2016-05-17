import math
import matplotlib.pyplot as plt

class Jupiter:
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.r=math.sqrt(x*x+y*y)
    def nextState(self):
        self.vx=self.vx-dt*4*math.pi*math.pi*self.x/(self.r*self.r*self.r)
        self.vy=self.vy-dt*4*math.pi*math.pi*self.y/(self.r*self.r*self.r)
        self.x=self.x+dt*self.vx
        self.y=self.y+dt*self.vy
        self.r=math.sqrt(self.x*self.x+self.y*self.y)

class asteroid:
    def __init__(self,x,y,vx,vy):
        self.x=x
        self.y=y
        self.vx=vx
        self.vy=vy
        self.rj=math.sqrt((x-xj)*(x-xj)+(y-yj)*(y-yj))
        self.rs=math.sqrt(x*x+y*y)
    def nextState(self):
        self.vx=self.vx+dt*(-4*math.pi*math.pi*self.x/(self.rs*self.rs*self.rs)+4*math.pi*math.pi*(xj-self.x)*0.001/(self.rj*self.rj*self.rj))
        self.vy=self.vy+dt*(-4*math.pi*math.pi*self.y/(self.rs*self.rs*self.rs)+4*math.pi*math.pi*(yj-self.y)*0.001/(self.rj*self.rj*self.rj))
        self.x=self.x+dt*self.vx
        self.y=self.y+dt*self.vy
        self.rs=math.sqrt(self.x*self.x+self.y*self.y)
        self.rj=math.sqrt((self.x-xj)*(self.x-xj)+(self.y-yj)*(self.y-yj))

def v(r):
    v=2*math.pi/math.sqrt(r)
    return v

dt=0.01
t=0
j=Jupiter(5.2,0,0,v(5.2))
xj=j.x
yj=j.y
a=asteroid(3.7,0,0,2*math.pi/math.sqrt(3.7))
b=asteroid(3.276,0,0,2*math.pi/math.sqrt(3.276))
c=asteroid(3.0,0,0,2*math.pi/math.sqrt(3))
x=[]
y=[]
xa=[]
ya=[]
xb=[]
yb=[]
xc=[]
yc=[]

while t<4282:
    j.nextState()
    xj=j.x
    yj=j.y     
    a.nextState()    
    b.nextState()        
    c.nextState()    
    t=t+dt
    if t>=4250:
        x.append(j.x)
        y.append(j.y)
        xa.append(a.x)
        ya.append(a.y)
        xb.append(b.x)
        yb.append(b.y)
        xc.append(c.x)
        yc.append(c.y)
        

plt.plot(x,y,label='Jupiter')
plt.plot(xa,ya,label='r=3.700AU')
plt.plot(xb,yb,label='r=3.276AU')
plt.plot(xc,yc,label='r=3.000AU')
plt.legend(loc="upper right", frameon=True,prop={'size':10})
plt.xlabel('x/AU')
plt.ylabel('y/AU')
plt.show()