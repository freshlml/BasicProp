

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
# A调用，触发__call__协议方法，在A.__class__的mro路径中搜索，搜到class type中的__call__方法
#   1.构造A类的实例对象
#   2.调用A.__init__方法
a = A("参数")  # A.__init__方法搜到One的
print(a.one_sl_attr)  # 参数
# print(a.two_sl_attr)  # AttributeError: 'A' object has no attribute 'two_sl_attr'
# print(a.t_sl_attr)  # AttributeError: 'A' object has no attribute 't_sl_attr'
a.mt("mro")  # T_mro, mt方法搜到T的
