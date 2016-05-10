#第十一次作业  
2013301510017　　马汉臻  
##摘要  
> 本次作业用Euler-Cromer方法解决课本习题4.7，模拟质量相近的双星系统的运动。改变两个天体的质量、初始位置和初始速度，可得到不同的运动轨迹。我使用了绝对坐标系，而非质心系，因此一般难以得到闭合轨迹，但是可以观察双星系统的绝对运动。先通过合理设定初始条件，尝试令系统稳定运动；再大胆尝试各种初值，观察系统的运动情况。  

##背景介绍  
> 在低速、小质量近似下，天体运动服从牛顿万有引力定律，二体之间的引力由下式给出  
　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?F%3D%5Cfrac%7BGm_%7B1%7Dm_%7B2%7D%7D%7Br%5E%7B2%7D%7D)  
> 考虑多体系统时，某天体的受力应为其它所有天体对其的合力，其运动方程由下式给出  
　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?m%5Cfrac%7B%5Cmathrm%7Bd%7D%20v%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3DF)  
> 在二体问题中，若两个天体的质量相差甚大，则大质量的天体可视为静止，只需考虑小质量天体的运动，其受力与两天体距离有关，服从平方反比定律，运动轨迹为圆锥曲线，根据初始条件的不同，可能为抛物线、椭圆或双曲线。当两天体质量相近时，需要同时考虑二者的运动，并且运动轨迹往往不闭合。  

##正文  
###问题提出  
> 习题4.7 考虑一个假想的太阳系，但太阳质量并不远大于行星。现在同时考虑二者的运动，模拟它们的运动轨迹。尝试找出使轨迹稳定的条件。  
###解决方法  
> [代码链接](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_4/homework11_4.7.py)  
> 数值求解涉及二体的二阶微分方程组，化为八个一阶方程，使用Euler-Cromer方法，由初始点位置计算下一点速度，由下一点速度计算下一点位置，用四个list保存二体共四个坐标，再用scatter方法作图即可。  
> 直接将“二体”当作一个对象，建立相应类planets，包含方法move()，用于计算下一步状态。代码如下  
```python
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
```  

###模拟结果  
> 选取了一组比较合适的初始条件，得到双星系统运动轨迹如下
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_4/figure_1.png)  
> 减小蓝色线代表的天体的质量，轨迹产生如下变化，可见轨迹变得更加“紧凑”了，这与初速度减小，总能量减小有关。  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_4/figure_2.png)  
> 继续减小蓝色天体的初速度  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_4/figure_3.png)  
> 可见能量继续减小  
> 接下来尝试“制作”闭合轨迹  
