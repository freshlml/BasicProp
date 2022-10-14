

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
#   1.A.__new__，搜到object中__new__，构造A类的实例对象
#   2.A.__init__，搜到One中__init__
a = A("参数")
print(a.one_sl_attr)  # 参数
# print(a.two_sl_attr)  # AttributeError: 'A' object has no attribute 'two_sl_attr'
# print(a.t_sl_attr)  # AttributeError: 'A' object has no attribute 't_sl_attr'
a.mt("mro")  # T_mro, mt方法搜到T的


module_pp = "module_pp"


# 嵌套作用域的属性搜索与类声明时的属性定义
class D(object):
    class_pp = "class_pp"  # 在类的空间设置属性，不在嵌套作用域的属性搜索范围之内
    class_pp2 = module_pp

    def d1(self):
        print(module_pp)  # 类中定义的方法和函数有一样的属性搜索原则: 本def,module,builtins；注意:没有class
        print(class_pp)  # error
        print(class_pp2)  # error

    def d2(self):
        d1(self)  # error

    class DD(object):
        dd_pp = module_pp
        dd_pp2 = class_pp  # error


d = D()
d.d1()
d.d2()
