

class A(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


# __getattr__协议方法
# 触发与搜索规则: 对象.属性(包括方法)并且属性不存在时，触发__getattr__协议方法，被触发的协议方法从对象.__class__的mro路径中搜索
class Wrapper(object):

    def __init__(self, obj):
        self.obj = obj

    def __getattr__(self, item):
        print("getattr:", item)

        return getattr(self.obj, item)


# Wrapper.other  # other不存在，触发__getattr__，从Wrapper.__class__(等于type)的mro路径(type object)路径中搜索，搜索不到
a = A(1)
w = Wrapper(a)
w.__dict__['obj']      # 不会触发__getattr__
# w.__dict__['other']  # 不会触发__getattr__
w.obj  # 当属性存在时，不会触发__getattr__
# w.other  # 当属性不存在时，触发__getattr__
w.__str__()  # 当属性存在时，不会触发__getattr__
# w.__getitem__()  # 当属性不存在时，触发__getattr__
# w[0]  # w[0]触发__getitem__并且__getitem__不存在，但是不会触发 __getattr__
print(w.getName())


class WrapperSub(Wrapper):
    pass


sub = WrapperSub(A(2))
# sub.otherSub  # 触发Wrapper#__getattr__
print("-----------1------------------")


# __setattr__协议方法
# 触发与搜索规则: 对象.属性(包括方法) = 属性值时，触发__setattr__协议方法，被触发的协议方法从对象.__class__的mro路径中搜索
class B(object):
    attr = "attr"

    def __setattr__(self, key, value):
        print("设置属性: ", key, " = ", value)
        object.__setattr__(self, key, value)  # avoid loops, or self.__dict__[key] = value


B.attr = "修改attr"  # 触发__setattr__，从B.__class__(type)的mro路径(type object)中搜索，搜到type中__setattr__，不会搜索到B中__setattr__
B.newAttr = "新设置attr"
b = B()
b.__dict__['name'] = "通过dict设置值"  # 通过__dict__设置值不会触发__setattr__
print(b.name)

b.name = "修改name"  # 触发__setattr__， 从b.__class__(B)的mro路径(B object)中搜索，搜到B中__setattr__
b.newName = "设置新name"
print("-----------2------------------")


# __getattribute__协议方法
# 触发与搜索规则: 对象.属性(包括方法)时，触发__getattribute__协议方法，被触发的协议方法从对象.__class__的mro路径中搜索
# 对象.属性(包括方法)先触发__getattribute__协议方法，进入object.__getattribute__开启属性/方法搜索规则
class C(object):
    attr = "attr"

    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        print("getattribute:", item)
        if item == "other":
            return "不存在"
        return object.__getattribute__(self, item)  # avoid loops， return self.__dict__[item]将导致递归(__dict__)


# 触发__getattribute__协议方法，从C.__class__(type)的mro路径(type object)中搜索，搜到type中__getattribute__，不会搜到C中__getattribute__
print(C.attr)  # attr
c = C("name值")
c.__dict__['name']  # 通过__dict__获取值不会触发__getattribute__，(__dict__本身触发)
c.name  # 触发__getattribute__协议方法，从c.__class__(C)的mro路径(C object)中搜索，搜到C中__getattribute__
c.other
c.__str__()  # 触发__getattribute__协议方法，从c.__class__(C)的mro路径(C object)中搜索，搜到C中__getattribute__
# print函数中调用c.__str__()，但未触发C中__getattribute__
print(c)  # <__main__.C object at 0x000002263BEF0B00>




