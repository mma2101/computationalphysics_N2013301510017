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
