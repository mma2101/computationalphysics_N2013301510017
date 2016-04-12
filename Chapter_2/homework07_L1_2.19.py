import math
import matplotlib.pyplot as plt

g=9.8
dt=0.01

def B2m(v):
    'Calculate air resistance factor'
    B2m=0.0039+0.0058/(1+math.exp((v-35)/5))
    return B2m
        
class ball:
    def __init__(self,v,theta):
        self.x=0.0
        self.y=1.5
        self.vx=v*math.cos(math.pi*theta/180)
        self.vy=v*math.sin(math.pi*theta/180)
        self.w=2000*2*math.pi/60
        
    def fly(self):
        self.x=self.x+self.vx*dt
        self.y=self.y+self.vy*dt
        self.vx=self.vx+(-B2m(abs(self.vx-vwind))*(self.vx-vwind)*math.sqrt((self.vx-vwind)*(self.vx-vwind)+self.vy+self.vy)-S0m*self.vy*self.w)*dt
        self.vy=self.vy+(-B2m(abs(self.vy))*self.vy*math.sqrt((self.vx-vwind)*(self.vx-vwind)+self.vy+self.vy)+S0m*(self.vx-vwind)*self.w-g)*dt

S0m=4.1e-4 #backspin
vwind=4.4704 #10mph,tailwind
a=ball(50,35)
x1=[]
y1=[]
x1.append(a.x)
y1.append(a.y)
while a.y>0:
    a.fly()
    x1.append(a.x)
    y1.append(a.y)
x1[-1]=(x1[-2]-y1[-2]*x1[-1]/y1[-1])/(1-y1[-2]/y1[-1])
y1[-1]=0   

vwind=-4.4704 #10mph,headwind
b=ball(50,35)
x2=[]
y2=[]
x2.append(b.x)
y2.append(b.y)
while b.y>0:
    b.fly()
    x2.append(b.x)
    y2.append(b.y)
x2[-1]=(x2[-2]-y2[-2]*x2[-1]/y2[-1])/(1-y2[-2]/y2[-1])
y2[-1]=0

S0m=0.0 #nospin
vwind=4.4704 #10mph,tailwind
a=ball(50,35)
x3=[]
y3=[]
x3.append(a.x)
y3.append(a.y)
while a.y>0:
    a.fly()
    x3.append(a.x)
    y3.append(a.y)
x3[-1]=(x3[-2]-y3[-2]*x3[-1]/y3[-1])/(1-y3[-2]/y3[-1])
y3[-1]=0   

vwind=-4.4704 #10mph,headwind
b=ball(50,35)
x4=[]
y4=[]
x4.append(b.x)
y4.append(b.y)
while b.y>0:
    b.fly()
    x4.append(b.x)
    y4.append(b.y)
x4[-1]=(x4[-2]-y4[-2]*x4[-1]/y4[-1])/(1-y4[-2]/y4[-1])
y4[-1]=0

plt.plot(x1,y1,color='blue',label='tailwind,backspin')
plt.plot(x2,y2,color='red',label='headwind,backspin')
plt.plot(x3,y3,color='green',label='tailwind,nospin')
plt.plot(x4,y4,color='orange',label='headwind,nospin')
plt.xlabel('x/m')
plt.ylabel('y/m')
plt.xlim(0,180)
plt.legend(loc="upper right", frameon=True,prop={'size':10})
plt.show()
print 'distance with tailwind and backspin=',x1[-1]
print 'distance with headwind and backspin=',x2[-1]
print 'distance with tailwind and nospin=',x3[-1]
print 'distance with headwind and nospin=',x4[-1]
