# 第一: 当前module chapter5_21运行，重命名成__main__，其所在的目录为top-level package
# 第二: 绝对导入
#  如果模块已存在，直接使用
#  否则，根据"模块搜索路径"搜索模块，执行并赋值给变量
#   1.内置模块，如sys等
#   2.sys.path
#     当前py文件所在目录(top-level package): D:\\pyProjects\\BasicProp\\basic\\chapter5
#     环境变量PYTHONPATH指定目录
#     标准库目录: C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\..
#     .pth指定目录
import sys
import string
# todo，这里爆红但是运行不报错
import current_dic as current_dic1
# pycharm特殊: pycharm中运行不报错，那是因为在pycharm中运行时将工程目录(D:\\pyProjects\\BasicProp)添加到了sys.path
# from basic.chapter5 import current_dic as current_dic2

# top-level package的子目录
from sub import sub_dic

# 相对导入top-level package平级或者之上
# from ..chapter5_t import chapter5_t  # error: attempted relative import beyond top-level package

# 相对导入top-level package内或者其子目录中模块
# from . import current_dic                  # error: 当前运行的py不能使用相对导入,cannot import name 'current_dic' from '__main__'

import current_loop

# sys.path: 当前py文件所在目录，标准库目录，todo
print("chapter5_21", sys.path, sep=": ", end="\n")

# 一般是在标准库目录中搜索到string.py
# 很明显，如果在优先级更高的目录中存在string.py,则标准库目录中的会被覆盖
print(string)  # <module 'string' from 'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib\\string_覆盖.py'>

print(current_dic1)
print(sub_dic)  # <module 'sub.sub_dic' from 'D:\\pyProjects\\BasicProp\\basic\\chapter5\\sub\\sub_dic.py'>

# todo,__import__
