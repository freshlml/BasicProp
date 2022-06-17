

# python 类，对象, inherit_mode.uxf
class T(object):

    def __init__(self, t_sl_attr):
        self.t_sl_attr = t_sl_attr

    def mt(self, param):
        print("T_" + param)
        return self


class One(T):

    def __init__(self, one_sl_attr):
        self.one_sl_attr = one_sl_attr

    def one_mt1(self):
        return self


class Two(object):

    def __init__(self, two_sl_attr):
        self.two_sl_attr = two_sl_attr

    def mt(self, param):
        print("Two_" + param)
        return self


class A(One, Two):
    pass


print(A.mro())  # A One T Two object
# python中，可以从两个角度理解如下语句
# 1. 面向对象角度: 构造A类的实例对象并调用A.__init__方法
# 2. python的机制角度: __call__协议方法
a = A("参数")  # A.__init__方法搜到One的
print(a.one_sl_attr)  # 参数
# print(a.two_sl_attr)  # AttributeError: 'A' object has no attribute 'two_sl_attr'
# print(a.t_sl_attr)  # AttributeError: 'A' object has no attribute 't_sl_attr'
a.mt("mro")  # T_mro, mt方法搜到T的


