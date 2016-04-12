# **第七次作业**  
## **摘要**  
> 本次作业依旧研究抛体运动，不过是运动情况更为复杂的棒球，分别计算它在顺风和逆风情况下的下旋球飞行轨迹。计算轨迹时，不仅要考虑空气阻力以及风的影响，还要考虑棒球自转引起的轨迹偏移。此外，空气阻力的系数不再是常数，而是与球相对于空气的速度有关。由于风的存在，所有与球速有关的参数都应使用球与风的相对速度计算。  

## **背景介绍**
> 棒球作为一种（在美国）非常受欢迎的运动，针对它的研究（在美国）可谓如火如荼，数不清的物理学家在研究它。我们的目的是模拟真实的棒球飞行轨迹，在这个模拟中最重要的考虑因素是空气的影响，包括阻力、风力和侧压力等。  
> 棒球运动的基本方程和之前考虑过的炮弹类似，不同之处在于，棒球的空气阻力系数与其飞行速度有关，同时棒球的自转也会对轨迹造成显著影响。话虽如此，研究棒球和研究炮弹的方法大同小异，不过是在其运动方程中添加修正项。  

## **正文**  
### 问题提出  
> 本次作业解决书本第二章2.19题。模拟下旋球的飞行轨迹，取球的自转角速度为2000rpm。  

### 解决思路  
> 先考虑棒球的运动方程。由于是下旋球，自转不会造成棒球“拐弯”，因此建立二维坐标系足矣。棒球除了受空气阻力（与速度方向相反）和重力（竖直向下）外，还受自转引起的Magnus力（与速度方向垂直）。最终，欧拉法的有限小微元计算式为  
　　　　　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?dx%3Dv_%7Bx%7Ddt)  
　　　　　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?dy%3Dv_%7By%7Ddt)  
　　　　　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?dv_%7Bx%7D%3D%28-%5Cfrac%7BB_%7B2%7D%7D%7Bm%7Dvv_%7Bx%7D-%5Cfrac%7BS_%7B0%7D%7D%7Bm%7Dv_%7Bx%7D%5Comega%20%29dt)  
　　　　　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?dv_%7By%7D%3D%28-%5Cfrac%7BB_%7B2%7D%7D%7Bm%7Dvv_%7By%7D&plus;%5Cfrac%7BS_%7B0%7D%7D%7Bm%7Dv_%7By%7D%5Comega%20-g%29dt)  
> 以此为基础即可计算飞行轨迹。注意式中S0/m=0.00041为常量，B2/m与棒球速度有关，由下式给出  
　　　　　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BB_%7B2%7D%7D%7Bm%7D%3D0.0039&plus;%5Cfrac%7B0.0058%7D%7B1&plus;e%5E%7B%28v-v_%7Bd%7D%29/D%7D%7D)  
> 其中vd=35m/s，D=5m/s。  
> 在该问题中，初始高度设为1.5米，与棒球被投出时的水平高度相仿。  

### 实现代码  
代码链接[**homework07_L1_2.19.py**](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_2/homework07_L1_2.19.py)  
> 定义计算阻力系数的函数B2m，方便调用。  
```python
def B2m(v):
    'Calculate air resistance factor'
    B2m=0.0039+0.0058/(1+math.exp((v-35)/5))
    return B2m
```
> 定义一个新的类——ball，其属性是球的运动状态，包括位置、速度、角速度，唯一方法fly为“计算下一刻的状态”，只需不断使用该方法，并记录下每次的状态，即可得到轨迹，面向对象编程真是厉害。  
```python
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
```
> 接下来的语句就是循环执行fly方法，记录下每次的位置，即可用plot作图。注意在球落地前后两点之间依然需要截断，避免地面被砸穿，赔不起。如考虑有下旋，顺风，风速10mph，则用如下代码实现  
```python
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
```

## **结论**  
> 取初速度为50m/s，投射角35度，分别考虑有无自旋、顺逆风四种情况下的飞行轨迹，并输出落地距离。  
> 输出距离如下  
```
distance with tailwind and backspin= 140.297901124
distance with headwind and backspin= 116.572172822
distance with tailwind and nospin= 127.371397529
distance with headwind and nospin= 108.617475213
```
> 轨迹如下  
![]()  
> 易见下旋会使球飞得更高更远，顺风也当然有利于球的飞行。  

## **致谢**
> 校园网
