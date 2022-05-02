
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

    def __init__(self, attr):
        self.attr = attr


print(type(Base1))  # <class 'type'>
print(dir(Base1))  # 'base1_attr', 'bs1'

print(type(Base2))  # <class 'type'>
print(dir(Base2))  # 'base2_attr'

print(type(B))  # <class 'type'>
# 类B继承了基类Base1,Base2的属性和方法
print(dir(B))  # 'b_attr', 'base1_attr', 'base2_attr', 'bs1'
print(B.base1_attr)  # base1_attr
print(B.base2_attr)  # base2_attr

bb = B("bbb")  # 构造B类的实例对象, 基类构造?todo
print(dir(bb))  # 'attr', 'b_attr', 'base1_attr', 'base2_attr', 'bs1'
print(bb.attr)  # bbb
print(bb.b_attr)  # b_attr
print(bb.base2_attr)  # base2_attr
Base1.base1_attr = "Base1修改base1_attr"
print(bb.base1_attr)  # Base1修改base1_attr
print(bb.bs1().attr)  # bbb


# 属性搜索优先级: 对象属性，类属性，基类(从左到右，深度优先)属性
# 方法搜索优先级: 类方法，基类(从左到右，深度优先)方法
class T(object):
    attr = "attr_t"

    def mt(self):
        return "t"


class One(T):
    o_attr = "attr_one"

    def o_mt(self):
        return self


class Two(object):
    attr = "attr_two"

    def mt(self):
        return "two"


class C(One, Two):
    c = "类"

    def __init__(self):
        self.c = "实例"


c = C()
print(c.c)  # 实例
print(c.attr)  # attr_t
print(c.mt())  # t
