# 第九次作业  
　　　　2013301510017　　　　马汉臻  
　　　　
## 摘要  
> 本次作业研究物理摆中的混沌现象，根据外力周期，选取等时间间隔，在相空间中画出这些时刻相应的点。当选取的点足够多时，可以看到相空间中出现吸引子的图像。这说明混沌现象也有一定的规律。除了画出外作用力为零的点以外，还画出了外作用力最大的点，此外还可以取任意相位画点。  

## 背景介绍  
> 在考虑阻力和外驱动力后，真实的物理摆的运动方程为  
　　　　　![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B2%7D%5Ctheta%20%7D%7B%5Cmathrm%7Bd%7D%20t%5E%7B2%7D%7D%3D-%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta%20-q%5Cfrac%7Bd%5Ctheta%20%7D%7Bdt%7D&plus;F_%7BD%7Dsin%28%5COmega%20_%7BD%7Dt%29)  
> 当外驱动力周期恒定，且幅度足够大后，物理摆的运动将出现混沌现象。在混沌现象中，即使物理规律是决定性的，但只要初始状态相差一点，系统后续的演化将会差异巨大。混沌现象同时存在决定性与不确定性。  
> 为了研究混沌现象中的规律，我们可以画出相空间中的庞加莱截面，即根据外力周期，选取等时间间隔，在相空间中画出这些时刻相应的点。这样画出的图像中将出现吸引子，根据我们选取的相位不同，吸引子的形状也会不同。  

## 正文  

### 问题提出  
> 3.12：画出类似图3.9的Poincare section，但是每点相应的相位不一定取0，可以取0-2π间的任意值。  

### 解决方法  
> 该问题实质上仍为利用Euler-Cromer方法数值求解二阶常微分方程，但这次画出数值解在相空间中的图像，即角速度-角度图像，并且按照外驱动力的频率取点。  
> Euler-Cromer方法的计算式为书上式(3.19)  

### 计算结果  
> [代码链接](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_3/homework09_3.12.py)  
> 选取外驱动力为零，即相位为0的点，画出庞加莱图如下，和课本图3.9一致  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_3/1.png)  
> 现在选取相位为π/2的点，此时外驱动力达到正值极大，画图如下  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_3/2.png)  
> 此外，还可以选取相位π/4的点，画图如下  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_3/3.png)  
> 可以看到在相位依次从0变化至π/4时，画出来的图应该有一个连续变化的过程。  

## 致谢  
> 无
