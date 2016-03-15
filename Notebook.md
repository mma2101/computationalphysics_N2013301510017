# Notebook for the course
## 一、Markdown语法查询
- [Markdown 语法说明 (简体中文版)](http://www.appinn.com/markdown/)
- [StackEdit](https://stackedit.io/editor)

## 二、在Ipython中运行保存好的.py格式文件
- 方法一
```
import os
os.chdir("文件夹路径")
execfile("带格式文件名")
```
- 方法二
```
import os
os.system("python 完整路径")
```

## 三、清楚屏幕
```python
import os
os.system('cls')
```
