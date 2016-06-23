import math
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

v=[]
for i in range(50):
    v.append(range(50))
for i in range(50):
    v[0][i]=0.0
    v[i][0]=0.0
for i in range(20):
    v[49-i][30]=1.0

dv=10.0
a=0.0
while dv>1:
    dv=0.0
    for i in range(50):
        for j in range(50):
            a=v[i][j]
            if j==30 and i>29.5:
                v[i][j]=1.0
            elif i!=0 and i!=49 and j!=0 and j!=49:
                v[i][j]=(v[i+1][j]+v[i-1][j]+v[i][j+1]+v[i][j-1])/4.0
            elif i==49 and j!=49:
                v[i][j]=(v[i][j]+v[i-1][j]+v[i][j+1]+v[i][j-1])/4.0
            elif j==49 and i!=49:
                v[i][j]=(v[i+1][j]+v[i-1][j]-v[i][j]+v[i][j-1])/4.0
            elif i==49 and j==49:
                v[i][j]=(v[i][j]+v[i-1][j]-v[i][j]+v[i][j-1])/4.0
            dv=dv+abs(a-v[i][j])

x=[]
y=[]
z=[]
for i in range(100):
    z.append([])
    x.append(i)
    y.append(i)
    for j in range(100):
        if i<49.5 and j<49.5:
            z[i].append(v[i][j])
        elif i<49.5 and j>49.5:
            z[i].append(-v[i][99-j])
        elif i>49.5 and j<49.5:
            z[i].append(v[99-i][j])
        else:
            z[i].append(-v[99-i][99-j])

cs=plt.contour(x,y,z,30)
#plt.clabel(cs,inline = 1, fontsize = 10)
#fig = plt.figure()
#ax = fig.gca(projection='3d')
#ax.plot_trisurf(x, y, z, cmap=cm.jet, linewidth=0.01)
plt.show()
