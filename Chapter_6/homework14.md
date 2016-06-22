# 第十四次作业  
　　2013301510017　　马汉臻  

## 摘要  
> 本报告完成完成课本习题6.6，模拟两个波包的运动，验证波的叠加原理。本问题考虑一维运动的横波。由于波动方程满足叠加原理，两列波相遇时，振幅叠加，不发生相互作用，分离后保持原有的形状、速度。本程序先模拟两个振幅不同的高斯波包，研究各时刻各点的振幅；再将其中一个波包换成正弦波和高斯波包的叠加，更加直观地看到叠加原理的作用。  

## 背景介绍  
> 在忽略介质损耗的情况下，一维弹性波满足如下波动方程  
　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20y%7D%7B%5Cpartial%20t%5E2%7D%3Dc%5E%7B2%7D%5Cfrac%7B%5Cpartial%5E2%20y%7D%7B%5Cpartial%20x%5E2%7D)  
> 该方程适用于横波或纵波。式中c为波速，x为沿波传播方向的坐标，y为该点的位移。  
> 许多问题满足波动方程，因此许多物理现象具有波动的性质，例如弹性介质中的弹性波、电磁波、声波等。波动方程是线性方程，因此若方程存在某两个解，那么他们的和也是波动方程的解，这就是叠加原理。叠加原理使得两束波相遇时，振幅叠加，但单看每一个波的行为都不受影响。叠加原理不受各波初始条件的影响，因此我们可以改变波的形状，更加形象地表现两束波的叠加和分离。  

## 正文  
[代码](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/homework14_6.6.py)  
### 问题提出  
> 习题6.6：叠加原理的一个重要结果就是两个波包的运动相互独立，当我们在初始时建立两个高斯波包后，它们会相对运动并结合，最终分离。模拟它们的行为，证明它们在碰撞中不会互相影响，即碰撞后速度、形状不变。  

### 解决方法   
> 使用有限元差分法对偏微分方程进行数值计算。每步计算的时间间隔和空间距离满足dx/dt=v，其中v为波速，这样可以使结果尽可能地接近实际结果。每点每刻的位移y由下式计算，其中i标志位置，n标志时刻  
　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?y%28i%2Cn&plus;1%29%3Dy%28i&plus;1%2Cn%29&plus;y%28i-1%2Cn%29-y%28i%2Cn-1%29)  
> 初始时刻的高斯波包由下式描述，其中x0为波包中心位置  
　　　　　　　　　　![](http://latex.codecogs.com/gif.latex?y%28x%29%3Dexp%5B-k%28x-x_%7B0%7D%29%5E%7B2%7D%5D)  
> 在本问题中，应该设置两个波包。  

### 问题解决  
> 先考虑两个初始静止的高斯波包，他们的最大振幅比为1:2。由于波包初始静止，在开始模拟后他们分别将分裂成两个波包，向两边运动。我们主要观察相互靠近的两个子波包。在本问题中，我使用了固定边界条件，因此波到达边界时会反弹。下图画出了各点位移随时间的变化。  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/1.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/2.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/3.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/4.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/5.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/6.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/7.png)  
> 可见，两个波包相遇后分离，前后速度、形状均不改变，叠加原理得到验证。  
> 右边的波包乘以一个正弦波，观察差异巨大的两个波包的行为。  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/8.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/9.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/10.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/11.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/12.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/13.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_6/14.png)  

## 致谢  
> 无
