

# python类，对象，继承模型,inherit_mode.uxf
# 从实现上讲
#   属性搜索(根据属性名称):  实例对象, 类(实例对象.__class__), 基类(类.__bases__)的从左到右深度优先
#   方法搜索(仅根据方法名称): 类(实例对象.__class__), 基类(类.__bases__)的从左到右深度优先
#          仅根据方法名称，参数无关
# 如果要从继承的角度讲:
#     实例对象 继承 类(对象), 类(对象) 继承 基类(对象)
class T(object):
    t_attr = "t_attr"  # 类属性，实例对象共享之

    def __init__(self, t_sl_attr):  # 初始化方法，实例对象构造后调用
        self.t_sl_attr = t_sl_attr

    def t_mt1(self):
        return self

    @staticmethod
    def t_mt2():
        return T.t_attr

    def mt(self, param):
        print(param)
        return self

    def mt2(self):
        print("mt2")
        return self


print(type(T))  # <class 'type'>, class语句执行，创建类，变量T指向class type类型的对象(即类)，这和def没有任何区别
print(T.t_attr)  # t_attr, 获取类属性
print(T.t_mt2())  # t_attr
T.t_attr_1 = "添加属性"
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__',
#  '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__',
#  '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__',
#  '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 't_attr', 't_attr_1', 't_mt1', 't_mt2',]
print(dir(T))
b1_1 = T("b1_1")  # 构造T类的实例对象
print(b1_1.t_sl_attr)  # b1_1
b1_2 = T("b1_2")  # 构造T类的实例对象
print(b1_2.t_sl_attr)  # b1_2
# 类属性，实例对象共享之
T.t_attr = "修改"
print(T.t_attr)  # 修改
print(b1_1.t_attr)  # 修改
print(b1_2.t_attr)  # 修改
print(b1_1.t_attr is T.t_attr)  # True
# 实例对象中定义同名属性
b1_1.t_attr = "b1_1"
print(b1_1.t_attr)  # b1_1
print(T.t_attr)  # 修改
print(b1_2.t_attr)  # 修改
print("-------1------------")


class One(T):
    one_attr = "one_attr"

    def __init__(self, one_sl_attr):
        self.one_sl_attr = one_sl_attr

    def one_mt1(self):
        return self


class Two(object):
    two_attr = "two_attr"
    two_attr_1 = "two_attr_1"

    def __init__(self, two_sl_attr):
        self.two_sl_attr = two_sl_attr

    def two_mt1(self):
        return self

    def mt(self, param):
        print("mt")
        return self

    def mt2(self, param):
        print(param)
        return self


class A(One, Two):
    a_attr = "a_attr"


a1 = A("参数")  # 构造A类实例对象对象，__init__方法搜到One的
print(a1.one_sl_attr)  # 参数
# print(a1.two_sl_attr)  # AttributeError: 'A' object has no attribute 'two_sl_attr'
print(a1.a_attr)  # a_attr
a1.mt("深度优先")  # 深度优先
# a1.mt2("方法搜索和参数无关")  # TypeError: mt2() takes 1 positional argument but 2 were given
