

# python 类，对象，继承模型
class E(object):
    attr = "e"

    def m(self):
        print("e_m")
        return self

    def __call__(self, *args, **kwargs):
        print("e_call")


class D(object):
    attr = "d"

    def m(self):
        print("d_m")
        return self


class F(object):
    attr = "f"

    def m(self):
        print("f_m")
        return self


class C(D, F):
    attr = "c"

    def m(self):
        print("c_m")
        return self


class B(E, D):
    pass


class AMeta(type):
    attr = "a_meta"
    attr1 = "a_meta"

    def __new__(mcs, *args, **kwargs):
        cls = type.__new__(mcs, *args, **kwargs)
        return cls

    def __init__(cls, *args, **kwargs):
        pass

    def __call__(cls, *args, **kwargs):
        print("a_meta_call")
        return type.__call__(cls, *args, **kwargs)

    def m(self):
        print("a_meta_m")
        return self

    def m1(self):
        print("a_meta_m")
        return self


class A(B, C, metaclass=AMeta):

    def __init__(self):
        self.attr1 = "attr"
        self.m = lambda: print(1)


# print(AMeta.mro())
print(A.mro())  # A B E C D F object
print(A.attr)    # e,   在类A上搜索属性, 类A的mro路径 + (类A作为实例对象)类A.__class__的mro路径
print(A.attr1)   # a_meta
A.m(None)         # e_m, 在类A上搜索方法, 类A的mro路径 + (类A作为实例对象)类A.__class__的mro路径
A.m1()           # a_meta_m, 在类A上调用方法的self约定: (类A作为实例对象)类A.__class__的mro路径 中搜索到的方法将自身作为第一个参数
print("------------1------------")
a = A()        # a_meta_call, 对类A的调用，__call__协议方法，从(类A作为实例对象)类A.__class__的mro路径 中搜索
print(a.attr)  # e, 类A的实例对象上搜索属性, 实例对象 + 实例对象.__class__的mro路径
a.m()          # 1, 类A的实例对象上搜索方法, 实例对象 + 实例对象.__class__的mro路径
print()        # ,  类A的实例对象上调用方法的self约定: 实例对象.__class__的mro路径 中搜索到的方法将自身作为第一个参数
a.__call__ = lambda self, *args: print("a_call")
a()            # e_call, 类A的实例对象的调用，__call__协议方法，从实例对象.__class__的mro路径 中搜索
print("------------2------------")
a2 = A()
A.__init__(a2)  # __init__方法的搜索和普通方法一样: 类A的mro路径 + (类A作为实例对象)类A.__class__的mro路径
a2.__init__ = lambda self: print("a2_init")
a2.__init__(None)  # a2_init, __init__方法的搜索和普通方法一样: 实例对象 + 实例对象.__class__的mro路径

print("#####################")


class F(object):
    a = "F"

    def aa(self):
        print("f_aa")
        return self


class E(F):
    a = "E"

    def aa(self):
        print("e_aa")
        return self


# class G(F, E):  # TypeError: Cannot create a consistent method resolution order (MRO) for bases F, E
#    pass




