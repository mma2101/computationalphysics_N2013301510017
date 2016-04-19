#**第八次作业**  
2013301510017　　马汉臻  

##**摘要**  
> 本次作业使用二阶Runge-Kutta法解决课本习题3.8。在没有小角度近似的情况下，研究真实摆的运动规律，同时假设摆臂为一无质量的刚性棒，这将允许我们考虑摆幅大于90的情况。不采取小角度近似时，在一定的摆长和重力加速度下，摆的周期将与摆幅有关，且摆幅越大，周期越长。本次作业将数值计算不同摆幅下摆的运动轨迹，并作出周期-摆幅关系图。  

##**背景介绍**  
> 振动现象在生活中随处可见，在物理中更是有数不清的现象应以振动描述。物理中，振动的最简单例子就是摆（pendulum）。在理想情况下，忽略各种摩擦，并假设摆幅非常小，摆的运动可看做简谐运动（harmonic motion）。但在本次作业讨论的范围内，我们不假设摆幅很小，同时允许摆幅超过90度（即假定摆臂为不可伸缩的轻棒），摆的运动方程可表示为  
　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B2%7D%5Ctheta%20%7D%7Bdt%5E%7B2%7D%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta)  
> 式中θ为摆幅，g为重力加速度，l为摆长。  
> 在没有摩擦的体系中，能量守恒，摆依然作周期性运动，但不是简谐运动。在这种模型下，摆的周期将与摆幅有关。我们假定摆无初始速度，那么初始位置即为摆幅。  

##**正文**  

###问题提出  
- 3.8  考虑非线性摆，利用二阶Runge-Kutta法计算摆的运动轨迹，研究周期和摆幅的关系  

###解决思路  
> 摆的运动方程可化为两个一阶微分方程，如下  
　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5Ctheta%20%7D%7Bdt%7D%3D%5Comega)  
　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5Comega%20%7D%7Bdt%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta)  
> 使用二阶Runge-Kutta法进行逐步计算，方法如下：  
- 1.使用起点的θ和ω计算中点的ω；
- 2.使用中点的ω和起点的θ计算终点的θ；
- 3.使用起点的θ和ω计算中点的θ；
- 4.使用中点的θ和起点的ω计算终点的ω，至此完成一步计算。  

> 至于研究周期和摆幅的关系，采用扫描的方法，在10度至170度之间每隔1度计算一条轨迹，在每条轨迹中，记录前三次穿过平衡位置的时间，第一和第三次的时间之差即为摆动周期，由此的到摆幅和周期的组合。  

###实现代码  
- 代码链接[*homework08_3.8.py*](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_3/homework08_3.8.py)  

> 定义pendulum类，用三个列表分别记录θ、ω和时间。方法nextState用于计算在下一时刻摆的运动状态，包含了二阶Runge-Kutta法；方法f用于计算角速度的变化率。  
```python
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
```
> 在10至170度间取若干角度计算轨迹并作图，计算每个角度对应的周期。  
```python
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
```
##**结论**  
> 设摆幅分别为10度、90度和170度，作出摆末端的运动图像  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_3/homework08_3.8_pic1.png)  
> 可见，摆幅越大，周期越长，三个周期分别为：  
```python
print period[0]
print period[1]
print period[2]
```
> 15.221  
17.932  
37.06  

> 摆幅在10到170之间，每隔1度计算一次，记录每个角度对应的周期，作出周期-摆幅曲线  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_3/homework08_3.8_pic2.png)  
> 可见周期随着摆幅上升，且上升速率不断增加。  

##**致谢**  
- 无
