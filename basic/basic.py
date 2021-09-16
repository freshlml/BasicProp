import sys

print(sys.path)

'''
标识符
  第一个字符是字符或者下划线，其他字符可以是数字，字符，下划线。字符可以是非ASKII字符
'''
_中 = 1
中 = "hello 中"

'''
单行注释: #, 注意代码规范
多行注释: \''' 、 \"""
'''

#  一条语句结束不用加;

'''
多行语句
  通常一行写完一条语句，如果需要换行，使用\连接
  total = item_one + \
          item_two + \
          item_3
  在[], {}, ()中的多行语句不需要使用反斜杠
  total = ['item_one', 'item_two'
           'item_3', 'item_4']
'''

'''
变量定义不需要要指定类型，变量有隐式的类型
字符串类型:
  单引号和双引号完全相同
  使用\''', \"""定义一个多行字符串
  转义符: \
  字符串前加r或者R表示自然字符串, r"fkasdjf \n"则\n会显示而不会换行
'''
s = '''字符串
    fdkafjsd
'''
print(s)

'''
使用import，from ... import导入
import module 导入整个模块
from module import func 从某个模块导入某个函数
from module import func1,func2
from module import *
'''

'''
python basic.py执行这个脚本文件
在linux中的basic.py文件，开头#!/usr/bin/env python
修改文件权限: chmod u+x basic.py
运行脚本文件: sh basic.py
'''