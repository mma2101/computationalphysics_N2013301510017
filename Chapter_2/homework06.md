#第六次作业
##摘要
>本文为计算物理课程第六次作业报告，我完成了作业的Level 1及Level 2（[作业要求](https://github.com/caihao/computational_physics_whu/blob/master/Exercises.md)），分别对应教材习题2.9和2.10。正文主要包括解决问题的思路以及实现的代码；结论部分将给出程序运行结果及图片。

##背景介绍
>计算物理课程第二章旨在计算真实抛体的运动轨迹，本质上是数值求解二阶线性常微分方程组，使用方法仍为欧拉法。  

>考虑炮弹的飞行轨迹，忽略空气阻力的话，运动方程由牛顿第二定律给出，如下式
>
>![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2x%7D%7Bdt%5E2%7D%3D0)
>
>![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E2y%7D%7Bdt%5E2%7D%3D-g)
