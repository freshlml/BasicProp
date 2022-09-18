# python解析器
python解析器
### python -m命令语法
```shell script
# 1.将当前工作目录添加到sys.path
# 2.在sys.path中搜索
D:\pyProjects\BasicProp\basic> python -m package_name/module_name

# 搜索package, 运行package下__main__.py
D:\pyProjects\BasicProp\basic> python -m package_name

# 搜索module, 以__main__运行
D:\pyProjects\BasicProp\basic> python -m module_name

# 搜索module, 以__main__运行
D:\pyProjects\BasicProp\basic> python -m package.module
```
### python script
```shell script
# 1.py文件路径可以是绝对路径，或者相对路径，相对于当前工作目录
# 2.将py文件所在目录的绝对路径添加到sys.path
D:\pyProjects\BasicProp\basic> python ./chapter5/test.py

# 1.package路径可以是绝对路径，或者相对路径，相对于当前工作目录
# 2.执行package下__main__.py, 将./basic/chapter5添加到sys.path
D:\pyProjects\BasicProp> python ./basic/chapter5

```


