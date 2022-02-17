import sys
# import
# 1. 如果该module已被import，不重复import
# 2. 搜索module,按"搜索路径"依次搜索
#    1).当前运行的module所在的目录；
#    2).PYTHONPATH环境环境变量定义的目录；
#    3).当前工作目录:python命令执行时目录(一般和1)相同，但也可以不同)；
#    4).python标准库目录；
#    5). .pth文件
# 3. 将module的源代码编译成字节码或者直接使用已存在的字节码
# 4. 执行module的字节码，生成class module对象，赋值给此中变量
import chapter5_21_1

# 打印"搜索路径"，TODO，一些目录需要认识
print(sys.path)

print(chapter5_21_1.module_param)

# todo,disutils,venv,__import__

print(type(chapter5_21_1))  # <class 'module'>

# dir()函数,__dir__()协议方法
print(dir(chapter5_21_1))
print(chapter5_21_1.__dir__())

print("-------2-------")

# 在搜索路径中查找 sub目录的chapter5_sub
import sub.chapter5_sub
# import sub.chapter5_sub as chapter5_sub
print(sub.chapter5_sub.sub)
print(type(sub))  # <class 'module'>, sub目录被解析成class module，对应该目录下的__init__.py文件,包首次被读取时执行
print(type(sub.chapter5_sub))  # <class 'module'>
print(sub is sub.chapter5_sub)  # False

from sub import chapter5_sub_from
print(chapter5_sub_from.sub_from)

print("--------3------")

# 规范写法?
from basic.chapter5.pol import qq
import basic.chapter5.pol.ww as ww
print(qq.var)
print(ww.var)

# 在相对路径中查找,.表示当前目录，..表示上层目录
from .rel import chapter5_21_rel
from .. import basics














