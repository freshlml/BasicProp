

class A(object):
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name


# __getattr__何时触发
class Wrapper(object):

    def __init__(self, obj):
        self.obj = obj

    # 实例对象.属性，当属性不存在时，触发，但，隐式的协议方法调用就算不存在也不会触发
    def __getattr__(self, item):
        print("getattr:", item)

        return getattr(self.obj, item)


# Wrapper.other  # 通过类获取属性不会触发__getattr__
# Wrapper.getOther()
w = Wrapper(A(1))
w.__dict__['obj']      # 不会触发__getattr__
# w.__dict__['other']  # 不会触发__getattr__
w.obj  # 当属性存在时，不会触发__getattr__
# w.other  # getattr: other, 通过 实例对象.不存在的属性 时 触发
w.__str__()  # 当属性存在时，不会触发__getattr__
print(w)  # <__main__.Wrapper object at ...>, 未触发__getattr__
# w.__getitem__()  # getattr: __getitem__, 当属性不存在时，触发
# w[0]  # 隐式的__getitem__()调用不会触发 __getattr__

# getattr: getName
# 1
print(w.getName())

print("-----------1------------------")


# __setattr__何时触发
class B(object):
    attr = "attr"

    # 实例对象.属性 = 属性值 时 触发
    def __setattr__(self, key, value):
        print("设置属性: ", key, " = ", value)
        self.__dict__[key] = value   # avoid loops


B.attr = "修改attr"  # 类修改属性，不会触发
B.newAttr = "新设置attr"  # 类设置属性，不会触发
b = B()
b.__dict__['name'] = "通过dict设置值"  # 通过__dict__设置值不会触发
print(b.name)  # 通过dict设置值

b.name = "修改name"  # 设置属性:  name  =  修改name
b.newName = "设置新name"  # 设置属性:  newName  =  设置新name

print("-----------2------------------")


# __getattribute__何时触发
class C(object):
    attr = "attr"

    def __init__(self, name):
        self.name = name

    # 实例对象.属性 时触发，隐式的协议方法调用不会触发
    def __getattribute__(self, item):
        print("getattribute:", item)
        if item == "other":
            return "不存在"
        # return self.__dict__[item]  # 获取__dict__递归
        return object.__getattribute__(self, item)  # avoid loops


# C.attr  # 通过类获取属性不会触发
# C.getOther()
c = C("name值")
c.__dict__['name']  # __dict__触发，getattribute: __dict__，name属性未触发
# c.__dict__['other']  # __dict__触发，getattribute: __dict__，other属性未触发
c.name  # getattribute: name, 实例对象.属性 触发
c.other  # getattribute: other, 实例对象.属性 触发
c.__str__()  # getattribute: __str__, 触发
print(c)  # <__main__.C object at 0x000002263BEF0B00>， 未触发




