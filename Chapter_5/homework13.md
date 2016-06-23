# 第十三次作业  
　　　2013301510017　　　　　马汉臻  

# 摘要  
> 本次作业完成第五章习题5.3，利用Gauss-Seidel方法数值求解拉普拉斯方程，研究两个有限大小的平行电容板附近的电势分布。由于本题情况有比较高的对称性，可以只计算四分之一个区域的电势分布，在扩展到全区域。我画出了电势分布的三维图像以及等势面图。  

# 背景介绍  
> 在无电荷区域，电势分布满足拉普拉斯方程  
　　　　　![](http://latex.codecogs.com/gif.latex?%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20x%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20y%5E2%7D&plus;%5Cfrac%7B%5Cpartial%5E2%20V%7D%7B%5Cpartial%20z%5E2%7D%3D0)  
> 尽管大多数常微分方程可以利用Euler法或Runge-Kutta法进行数值求解，但至今没有关于偏微分方程的通用方法。针对不同的偏微分方程，我们往往使用特定的方法。对于本题目中遇到的拉普拉斯方程，我们将它写成离散的形式  
　　　　　![](http://latex.codecogs.com/gif.latex?V%28i%2Cj%2Ck%29%3D%5Cfrac%7B1%7D%7B6%7D%5BV%28i&plus;1%2Cj%2Ck%29&plus;V%28i-1%2Cj%2Ck%29&plus;V%28i%2Cj&plus;1%2Ck%29&plus;V%28i%2Cj-1%2Ck%29&plus;V%28i%2Cj%2Ck&plus;1%29&plus;V%28i%2Cj%2Ck-1%29%5D)  
> 利用relaxation method，给定一定边界条件，在所求区域内不断“更新”各点的电势值，直到各点电势收敛，我们就认为得到了方程的数值解。为了使收敛的速度更快，扫描的速度更少，我在这题中采用Gauss-Seidel方法。  

## 正文  

### 问题提出  
> 5.3：针对课本图5.6的问题，利用对称性，至计算四分之一个区域，得到全区域的电势分布。  

### 解决方法  
> [代码链接](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_5/homework13_5.3.py)    
> 该问题的对称性如下：电势分布关于x轴对称，关于y轴反对称。因此我们只需要计算左上角的区域。为了程序编写方便，取左上角为原点。在该四分之一区域内划分50×50个像素点，其中比较特殊的点有：1、两个边界，电势保持为0；2、两个对称轴，其电势计算使用Runge-Kutta法，注意对称性；3、电容板，电势恒为1。  
> 不断重复更新各点电势值，直到前后两次所有点的电势差值之和小于0.1，认为达到足够精度。  

### 结论  
> 计算完四分之一区域后，利用对称性求得另外三个区域的电势分布，综合起来画出电势分布的三维图像，如下图。  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_5/2.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_5/3.png)  
> 可见，电势分布与预期符合。  
> 另外，画出了x-y平面上的等势线（面）。  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_5/5.png)  
![](https://raw.githubusercontent.com/mma2101/computationalphysics_N2013301510017/master/Chapter_5/5.png)  

### 致谢  
> 无
