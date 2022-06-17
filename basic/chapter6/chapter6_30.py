

# 类中方法定义第一个参数self只是一种约定，约定self是当前类(或子类)的实例对象
class A(object):

    def m(param):  # 第一个参数不写成self
        return param


print(A.m("123"))  # 123
a = A()
print(a.m())  # <__main__.A object at 0x000001A62C68FDA0>, a作为第一个参数传给param


# 类中方法定义按照约定，第一个参数应该定义成self，并且self约定为当前类(或子类)的实例对象
# python中有静态方法的概念: 使任何对象调用静态方法时都不会把自身作为第一个参数
class B(object):
    attr = 1

    @staticmethod
    def m(param):
        B.attr += 1
        return param


print(B.m("参数"))  # 参数
print(B.attr)  # 2
b = B()
print(b.m("参数2"))  # 参数2, 因为静态方法的缘故, b不会将自身作为第一个参数
print(B.attr)  # 3


# 函数式编程: 将函数作为参数传递, 这在python中有天然的优势，因为py中函数(方法)本生就是class Function的实例对象
#           py中本身就可以传递函数
#           类中定义的方法: 可以使用类引用，也可使用对象引用(此处借用java中的方法引用的概念，他们的逻辑是一样的)
class C(object):

    def m(self, param):
        pass

    @staticmethod
    def s_m(param):
        pass


# 类/对象引用静态方法
c_s_m = C.s_m
print(c_s_m)  # <function C.s_m at 0x00000277FCF34C80>
c_s_m("类引用静态方法")  # the same as C.s_m("类引用静态方法")
llc = C()
ll_m = llc.s_m
print(ll_m)  # <function C.s_m at 0x0000021F73E54C80>
ll_m("对象引用静态方法")  # the same as llc.s_m("类引用静态方法")
# 类引用
c_m = C.m
print(c_m)  # <function C.m at 0x000001CA5D234BF8>
c_m(C(), "类引用")  # the same as C.m(C(), "类引用")
# 对象引用
lc = C()
l_m = lc.m
print(l_m)  # <bound method C.m of <__main__.C object at 0x000001CA5D230B00>>
l_m("对象引用")  # the same as lc.m("对象引用")
print(l_m.__self__)  # <__main__.C object at 0x0000023CC1850AC8>
print(l_m.__self__ is lc)  # True
print(l_m.__func__)  # <function C.m at 0x0000023CC1854BF8>


module_pp = "module_pp"


# 类中属性有一定的封装性，不在嵌套作用域的属性搜索范围之内
class D(object):
    class_pp = "class_pp"
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
