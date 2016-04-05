#第六次作业
##摘要
>本文为计算物理课程第六次作业报告，我完成了作业的Level 1及Level 2（[作业要求](https://github.com/caihao/computational_physics_whu/blob/master/Exercises.md)），分别对应教材习题2.9和2.10。正文主要包括解决问题的思路以及实现的代码；结论部分将给出程序运行结果及图片。

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
