# 第三次作业
## Level 2
- 显示字典中存在的字母，并根据用户输入的字符串进行输出
```python
alphabet={
'z':['#####','   # ','  #  ',' #   ','#####'],
'h':['#   #','#   #','#####','#   #','#   #'],
'e':['#####','#    ','#####','#    ','#####'],
'n':['#   #','##  #','# # #','#  ##','#   #']
}
ava=alphabet.keys()
print 'Please type your letters, you can choose them from:',
for n in ava:
    print n,
print
name=list(raw_input())
for i in [0,1,2,3,4]:
    for j in name:
        print alphabet[j][i],' ',
    print
```
## Level 3
- 弹球动画
```python
import os
x=1
right=1
down=1
loc=[1,1]
pic=[""]*25
for i in range(25):
    pic[i]=[" "]*79
while x==1:
    os.system('cls')
    pic[loc[0]][loc[1]]="G"
    for i in range(25):
        print "".join(pic[i]),
    loc[0]=loc[0]+down
    loc[1]=loc[1]+right
    for i in range(25):
        pic[i]=[" "]*79
    if loc[0]+1==25 or loc[0]-1==-1:
	down=-down
    if loc[1]+1==79 or loc[1]-1==-1:
	right=-right
```
