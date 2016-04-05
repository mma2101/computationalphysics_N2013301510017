#第六次作业
##摘要
>本文为计算物理课程第六次作业报告，我完成了作业的Level 1及Level 2（[作业要求](https://github.com/caihao/computational_physics_whu/blob/master/Exercises.md)），分别对应教材习题2.9和2.10。正文主要包括解决问题的思路以及实现的代码；结论部分将给出程序运行结果及图片。

##背景介绍
>计算物理课程第二章旨在计算真实抛体的运动轨迹，本质上是数值求解二阶线性常微分方程组，使用方法仍为欧拉法。  
考虑炮弹的飞行轨迹，忽略空气阻力的话，运动方程由牛顿第二定律给出，如下式  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2x%7D%7Bdt%5E2%7D%3D0)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2y%7D%7Bdt%5E2%7D%3D-g)  
其中x和y分别为水平和垂直坐标，g为重力加速度。这是一个二阶常微分方程组，我们可以把它化为四个一阶常微分方程，如下式  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7Dx%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_%7Bx%7D)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7Dv_%7Bx%7D%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D0)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7Dy%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3Dv_%7By%7D)  
![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cmathrm%7Bd%7Dv_%7By%7D%20%7D%7B%5Cmathrm%7Bd%7D%20t%7D%3D-g)  
