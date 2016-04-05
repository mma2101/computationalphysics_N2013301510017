#第六次作业
##摘要
>本文为计算物理课程第六次作业报告，我完成了作业的Level 1及Level 2（[*作业要求*](https://github.com/caihao/computational_physics_whu/blob/master/Exercises.md)），分别对应教材习题2.9和2.10。正文主要包括解决问题的思路以及实现的代码；结论部分将给出程序运行结果及图片。  

##背景介绍
>计算物理课程第二章旨在计算真实抛体的运动轨迹，本质上是数值求解二阶线性常微分方程组，使用方法仍为欧拉法。考虑炮弹的飞行轨迹，忽略空气阻力的话，运动方程由牛顿第二定律给出，如下式  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2x%7D%7Bdt%5E2%7D%3D0)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2y%7D%7Bdt%5E2%7D%3D-g)  
其中x和y分别为水平和垂直坐标，g为重力加速度。这是一个二阶常微分方程组，我们可以把它化为四个一阶常微分方程，如下式  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7Dx%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_%7Bx%7D)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7Dv_%7Bx%7D%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D0)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7Dy%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_%7By%7D)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7Dv_%7By%7D%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-g)  
式中vx和vy分别为速度的水平和垂直分量。使用欧拉法，将每个方程写为有限小量形式，以计算每隔dt炮弹位置和速度的变化，给定位置和速度的初始值，我们就能计算此后的运动状态。当dt足够小时，用欧拉法数值计算的结果趋近于真实（解析）解。此外，我们还应该考虑空气阻力的影响，假定空气阻力总是沿着速度的反方向，大小与速度的平方成正比，空气阻力由下式给出  
![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%7D%3D-B_%7B2%7Dv%5E2)  
空气阻力与空气密度成正比，而空气密度又与海拔高度有关，我采用大气层的绝热近似，最终欧拉法的计算式如下  
![](http://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D%3Dx_%7Bi%7D&plus;v_%7Bx%2Ci%7D%7D%5CDelta%20t)  
![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D&plus;%5Cleft%20%28%201-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%20%5Cright%20%29%5E%7B%5Calpha%20%7D%5Cfrac%7BF_%7Bdrag%7D%7D%7Bm%7D%5CDelta%20t)  
![](http://latex.codecogs.com/gif.latex?y_%7Bi&plus;1%7D%3Dy_%7Bi%7D&plus;v_%7By%2Ci%7D%7D%5CDelta%20t)  
![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%3Dv_%7Bx%2Ci%7D&plus;%5Cleft%20%28%201-%5Cfrac%7Bay%7D%7BT_%7B0%7D%7D%20%5Cright%20%29%5E%7B%5Calpha%20%7D%5Cfrac%7BF_%7Bdrag%7D%7D%7Bm%7D%5CDelta%20t-g%5CDelta%20t)  
最后，考虑抛体轨迹的终点截断，当某次计算后y坐标小于0时，即为抛体落下地面，计算结束。根据“落到地面以下”前后两次的位置，用内插法（取直线）寻找恰好落到地面时的x坐标。  

##正文
###Level 1（习题2.9）
>[*代码homework06_L1_2.9.py*](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_2/homework06_L1_2.9.py)  
- 题目要求  
考虑空气阻力和海拔影响，计算不同抛射角度下的运动轨迹，寻找使得落点最远的抛射角。  
- 解决方法  
抛体的轨迹用一个形如[[  ],[  ]]的列表储存，第一个子列表用来储存x坐标，第二个储存y坐标。定义函数traj用以给出抛体轨迹，其参数为抛射角度angle和初始速率velocity。代码如下
```python
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
```
Traj函数中需要用到计算某刻加速度的函数acce，其参数为速度水平和垂直分量vx、vy，海拔高度y，其中重力加速度使用9.8m/s^2。返回的加速度由二元列表[  ,  ]给出，分别储存两个方向的分量。
```python
def acce(vx,vy,y):
    'Calculate acceleration concerning attitude'
    accelerration=[0,0]
    accelerration[0]=-math.pow((1-0.0065*y/293),2.5)*0.00004*math.sqrt(vx*vx+vy*vy)*vx
    accelerration[1]=-math.pow((1-0.0065*y/293),2.5)*0.00004*math.sqrt(vx*vx+vy*vy)*vy-9.8
    return accelerration
```
程序的主体非常简单，在0到90度之间等间距选取若干角度值（这里每0.1度计算一次，因此选取901个角度值），计算在该角度下的抛射轨迹，从中选取最远抛射距离及其对应抛射角。  
```python
maxangle=0
maxdis=0
for angle in np.linspace(0,90,901):
    x=traj(angle,700)
    #plt.plot(x[0],x[1],label=str(angle))
    if x[0][-1]>maxdis:
        maxdis=x[0][-1]
        maxangle=angle
print 'Maxangle=',maxangle
print 'Maxdistance=',maxdis
y=traj(maxangle,700)
plt.plot(y[0],y[1])
#plt.legend(loc="upper right", frameon=True)
plt.xlabel('x/m')
plt.ylabel('y/m')
plt.xlim(0,32000)
text='angle='+str(maxangle)
plt.annotate(text,xy=(21200,4300),xytext=(23000,5000),arrowprops=dict(arrowstyle="->",connectionstyle="arc3"))
plt.show()
```
作图时可选择画出最远的轨迹，抑或将所有角度的轨迹都画出来，后者可得到漂亮的图形。计算得到的最优角度及各种图片将在“结论”部分给出。  

###Level 2（习题2.10）
(施工中)

##结论  
###Level 1  
> - 程序运行结果  
```
Maxangle= 43.7  
Maxdistance= 24592.6051944
```
因此在初始速率700m/s时，使得抛射距离最远的角度为43.7度，最远距离为24592.6051944m。轨迹如下图  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_2/homework06_L1_2.9.png)  
此外，将所有轨迹每隔10度或1度都画出来，可得下图  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_2/homework06_L1_2.9_2.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_2/homework06_L1_2.9_3.png)  
非常漂酿  

