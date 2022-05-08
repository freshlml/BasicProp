
class A(object):
    a_attr = "a_attr"  # 类的属性

    def __init__(self, attr):  # 初始化方法，类的实例对象构造后自动调用
        self.attr = attr

    def mtd(self):
        return self.attr


print(type(A))  # <class 'type'>
print(dir(A))  # 'a_attr'
A.clz_attr = "clz_attr"  # 为类添加属性
print(dir(A))  # 'a_attr', 'clz_attr'
print(A.clz_attr)  # clz_attr
print(A.a_attr)  # a_attr
# print(A.attr)  # AttributeError: type object 'A' has no attribute 'attr'

a = A("a1")  # 构造A类的实例对象
print(type(a))  # <class '__main__.A'>
print(dir(a))  # 'a_attr', 'attr', 'clz_attr'
print(a.attr)  # a1 ,A类实例对象的属性
print(a.a_attr)  # a_attr ,A类的属性，相当于A.a_attr
print(a.clz_attr)  # clz_attr ,A类的属性

b = A("b1")  # 构造A类的实例对象
print(dir(b))  # 'a_attr', 'attr', 'clz_attr'
print(b.attr)  # b1
print(b.a_attr)  # a_attr

# 类的属性保存在类中，类的实例对象共享之
A.a_attr = "a_attr修改"
print(A.a_attr)  # a_attr修改
print(a.a_attr)  # a_attr修改
print(b.a_attr)  # a_attr修改

# 实例a中定义和A同名的属性
a.a_attr = "同名属性"
print(dir(a))  # 'a_attr', 'attr', 'clz_attr'
print(a.a_attr)  # "同名属性"
print(A.a_attr)  # a_attr修改
print(b.a_attr)  # a_attr修改


print("------1-------------------------------------------")


class Base1(object):
    base1_attr = "base1_attr"

    def __init__(self, attr):
        self.attr = attr

    def bs1(self):
        return self


class Base2(object):
    base2_attr = "base2_attr"


class B(Base1, Base2):
    b_attr = "b_attr"


print(type(Base1))  # <class 'type'>
print(dir(Base1))  # 'base1_attr', 'bs1'

print(type(Base2))  # <class 'type'>
print(dir(Base2))  # 'base2_attr'

print(type(B))  # <class 'type'>
# 类B继承了基类Base1,Base2的属性和方法
print(dir(B))  # 'b_attr', 'base1_attr', 'base2_attr', 'bs1'
print(B.base1_attr)  # base1_attr
print(B.base2_attr)  # base2_attr

bb = B("bbb")  # 构造B类的实例对象, 会立马调用初始化方法，通过方法搜索将会调用基类Base1中__init__方法
print(dir(bb))  # 'attr', 'b_attr', 'base1_attr', 'base2_attr', 'bs1'
print(bb.attr)  # bbb
print(bb.b_attr)  # b_attr
print(bb.base2_attr)  # base2_attr
Base1.base1_attr = "Base1修改base1_attr"
print(bb.base1_attr)  # Base1修改base1_attr
print(bb.bs1().attr)  # bbb


# 属性搜索: 对象属性，类属性，基类(从左到右，深度优先)属性
# 方法搜索: 类方法，基类(从左到右，深度优先)方法，注意方法搜索只看方法名(这和其他语言不一样，因为python中所谓的方法名和属性变量没有任何区别)
class T(object):
    attr = "attr_t"

    def mt(self):
        return "t"


class One(T):
    o_attr = "attr_one"

    def o_mt(self):
        return self

    def mm(self, param):
        return "one mm " + param

    def mm2(self, param):
        return "one mm2 " + param


class Two(object):
    attr = "attr_two"

    def mt(self):
        return "two"


class C(One, Two):
    c = "类"

    def __init__(self):
        self.c = "实例"

    def mm(self, param, param2="param2"):
        return "C " + param + param2

    def mm2(self, param, param2):
        return "mm2 " + param + param2


c = C()
print(c.c)  # 实例
print(c.attr)  # attr_t
print(c.attr is T.attr)  # True
print(c.mt())  # t
print(c.mm("111 "))  # C 111 param2 ,方法搜索: 仅根据方法名称，而不管参数
# print(c.mm2("111 "))  # TypeError: mm2() missing 1 required positional argument: 'param2'
