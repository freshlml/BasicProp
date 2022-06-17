from collections.abc import Iterable
from collections.abc import Iterator


# __iter__协议方法: def __iter__(self)
class A:
    def __iter__(self, aa):
        pass


# 协议方法: 方法名称+参数, 协议方法隐式触发，则需要有比较固定的参数形式，eg: def 协议方法名称(*args)这样的协议方法定义，则是参数无关的
print(isinstance(A, Iterable))  # False, 参数定义不一致???
# for x in A():  # TypeError: __iter__() missing 1 required positional argument: 'aa'
#    pass


# __call__协议方法
# 触发与搜索规则: 对象(...)，触发__call__协议方法，被触发的协议方法从对象.__class__的mro路径中搜索
# (显示)调用协议方法，搜索规则和普通方法一致
class C(object):

    def __init__(self, param):
        self.param = param

    def __call__(self, *args):
        print(args)


c = C("构造")
C.__call__(c, "显示调用__call__")  # ('显示调用__call__',)
c.__call__("显示调用__call__")  # ('显示调用__call__',)
c("隐式触发__call__")   # ('隐式触发__call__',)





