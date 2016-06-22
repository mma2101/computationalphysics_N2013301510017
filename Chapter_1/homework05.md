# 第五次作业  
马汉臻　　　2013301510017  

## 摘要
> 本报告系计算物理第五次作业，完成课本习题1.6。用欧拉法数值模拟了人口增长模型。首先模拟无限增长的模型，在该模型下死亡率为0，研究人口总数随时间的变化。然后加入与人口死亡有关的项，比较前后两种模型的区别。在第二个模型中，调整与出生率和死亡率有关的参数，比较人口变化的趋势。  

## 背景介绍  
> 多项式型的人口增长模型是最简单、最直观的人口模型。在该模型下，认为人口的出生率正比于人口基数，而死亡率正比于人口基数的平方，因为在人口数量过大时，由于资源匮乏，死亡率将显著上升。描述出生率和死亡率的两个参数与实际的环境有关，在这里，我只作数学上的考虑，因此可尝试各种参数组合，研究人口的变化趋势。  

## 正文  
[代码1](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_1/homework05_1.py)  
[代码2](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_1/homework05_2.py)  
> 本题研究的人口模型由下式描述  
> ![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BdN%7D%7Bdt%7D%3DaN-bN%5E%7B2%7D)  
> 式中N为人口基数，是一个关于时间的函数，aN代表单位时间内的出生人数，bN2代表单位时间内的死亡人数。在该问题中，已将人口模型抽象为简单的数学模型，因此已经无量纲化。  
> 首先考虑无死亡的情况，此时b=0。使用欧拉法，程序中每时刻的人口由下式计算  
> 此外，该微分方程可以解析求解，在程序中亦画出了精确解。  
> 图1画出了程序模拟的结果，初始人口N=1000， a=1，模拟时间t=5，计算时间间隔dt=0.1，红线为数值结果，蓝线为解析理论值。可以看到，人口呈指数增长。但数值结果与解析解差异较大。  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_1/1.png)  
> 缩短dt=0.01，得到图2结果。  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_1/2.png)  
> 可以看到，数值解明显更准确了。有理由相信，通过缩短时间间隔dt，可以让数值解更精确地逼近解析解。接下来加入死亡率。图3画出了N=1000，a=1，b=0.1的结果，可以看到，死亡率过大，人口从一开始就急剧衰减。  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_1/3.png)  
> 降低b至0.01，如下图  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_1/4.png)  
> 可以看到，死亡放缓，但仍无法逃脱灭绝的命运。继续降低b至0.001，发现此时出生和死亡持平，人口稳定不变。  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_1/5.png)  
> 继续降低b至0.0001.  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_1/6.png)  
> 可以看到，此时人口在开始时增长较快，然后趋于稳定，符合实际的人口模型。  

## 致谢
> 无
