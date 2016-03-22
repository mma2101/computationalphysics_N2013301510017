#第四次作业
##摘要
> 本文为计算物理课程第四次作业，本人完成了第一章习题1.5，通过用Euler method数值求解简单的一阶线性常微分方程组，模拟平衡过程并作出演化曲线。

##背景介绍
> 对常微分方程进行数值求解的最简单方法是欧拉方法，亦即模拟微分方程中的无穷小量变化，用有限小量近似无穷小量。当计算变量的间隔足够小时，数值求解的结果逼近解析解。

##正文

> ###题目
>> 考虑某原子可在态A与B之间跃迁，跃迁速率由以下方程组决定
>> $$\frac{dN_A}{dt}=\frac{N_B}{\tau}+\frac{N_A}{\tau}$$
>> $$\frac{dN_B}{dt}=\frac{N_A}{\tau}+\frac{N_B}{\tau}$$
>> 给定初始两种态的原子数及特征时间，求出两态原子数随时间的变化关系，指出系统平衡态的特点。

>###解决思路
>>使用欧拉方法，在用户输入初始条件后，利用方程的有限元近似形式，计算每隔dt时间后N的变化量dN及N(t+dt)，并将历次算得的N(t)和t分别存为列表，最后利用matplotlib作出变化曲线Na(t)与Nb(t)。

>###解决方法
>>代码如下
>>[代码链接](https://github.com/mma2101/computationalphysics_N2013301510017/blob/master/homework04.py)
>>```python
import matplotlib.pyplot as plt
na=[]
nb=[]
t=[]
tao=1.0
dt=0.1
na.append(input("Initial Na:"))
nb.append(input("Initial Nb:"))
time=input("time:")
t.append(0)
while t[-1]<time:
    dna=(nb[-1]-na[-1])*dt/tao
    dnb=(na[-1]-nb[-1])*dt/tao
    na.append(na[-1]+dna)
    nb.append(nb[-1]+dnb)
    t.append(t[-1]+dt)
plt.plot(t,na,color="red",linewidth=2.0,linestyle="-",label="Na")
plt.plot(t,nb,color="yellow",linewidth=2.0,linestyle="-",label="Nb")
plt.plot([0,time],[na[-1]]*2,color="blue",linewidth=1.5,linestyle="-.")
plt.legend(loc="upper right", frameon=True)
plt.show()
```
>>程序运行后，输入初始条件Na=200，Nb=50，time=5，输出曲线图如下
>> ![homework04_pic](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/homework04_pic.png)
