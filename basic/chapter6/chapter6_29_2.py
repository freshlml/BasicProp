

# Descriptor: 属性查找，属性设置，属性删除时的回调机制
# 数据描述器: 定义了__set__() 或 __delete__()
# 非数据描述器: 仅定义了 __get__()
class AttrDescriptor(object):

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is not None:
            try:
                # return instance.__name
                return getattr(instance, "__" + self.name)
            except AttributeError:
                return None
        return owner

    def __set__(self, instance, v):
        if v:
            # instance.__name = v
            setattr(instance, "__" + self.name, v)

    def __delete__(self, instance):
        # del instance.__name
        delattr(instance, "__" + self.name)


class C(object):
    attr1 = AttrDescriptor()  # 调用__set_name__(attr1, C, "attr1")
    attr2 = AttrDescriptor()  # 调用__set_name__(attr2, C, "attr2")


class B(C):
    pass


b = B()
print(b.__dict__)  # {}

# 如果attr1属性在b.__class__的mro路径中存在并且attr1属性是Descriptor with __set__方法，则调用attr1.__set__(b, '任意')，而不是为b设置attr1属性
b.attr1 = "任意"
print(b.__dict__)  # {'__attr1': '任意'}

# attr1属性在B的mro路径中存在，而不是在B.__class__的mro路径中，所以将为B设置attr1属性而不是调用attr1.__set__(...)
# B.attr1 = "覆盖"


# attr1属性是b.__class__的mro路径中的数据描述器，调用attr1.__get__(b, b.__class__)
print(b.attr1)  # 任意

# attr1属性是B的mro路径中的数据描述器，调用attr1.__get__(None, B)
print(B.attr1)  # class B

# attr1属性是C的mro路径中的数据描述器，调用attr1.__get__(None, B)
print(C.attr1)  # class C

print("--------------1----------------")


# 链式属性描述器
class GetterSetter(object):
    def __get__(self, obj, objtype):
        if obj is None:
            return obj.__gs
        return "Tag"

    def __set__(self, instance, v):
        instance.__gs = v


class Meta(type):
    gs = GetterSetter()


class Cls(object, metaclass=Meta):
    # 没有进入object.__setattr__，所以不会引发Descriptor机制，而是直接为Cls设置属性gs
    # 可通过Cls.属性的形式引发
    gs = "1"


print(Meta.__dict__)  # 'gs': __main__.GetterSetter object
print(Cls.__dict__)  # gs': '1'
print(Cls.gs)  # Tag

print("--------------2----------------")


# property is a 数据描述器
class PropertyTest(object):
    def getx(self):
        return self.__x

    def setx(self, value):
        self.__x = value

    def delx(self):
        del self.__x

    x = property(getx, setx, delx, None)


p = PropertyTest()
p.x = "ppp"  # setx(p, "ppp")
print(p.x)   # getx(p)
print(p.__dict__)
print(PropertyTest.x)  # <property object> 类.x，返回x本身
del p.x      # delx(p)
print(p.__dict__)
'''
class property(object):
    def __init__(self, fget, fset, fdel, doc):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel
        if doc is None and fget is not None:
            doc = fget.__doc__
        self.__doc__ = doc
    
    def __get__(self, obj, objtype):
        if obj is None:
            return self
        assert self.fget is not None
        return self.fget(obj)
    
    def __set__(self, obj, value):
        assert self.fset is not None
        self.fset(obj, value)
        
    def __delete__(self, obj):
        assert self.fdel is not None
        self.fdel(obj)
    ...
'''

print("--------------property原理----------------")


# self约定的原理
class S(object):
    def m(self):
        pass


s = S()
print(S.m)  # function S.m
print(s.m)  # bound method S.m
print(s.m is S.m)  # False
'''self约定的python等价实现
class Function(object):
    def __get__(self, obj, objtype):
        if obj is None: return self
        return MethodType(self, obj)
        
class MethodType(object):
    def __init__(self, func, obj):
        self.__func__ = func
        self.__obj__ = obj
        
    def __call_(self, *args, **kwargs):
        return self.__func__(self.__obj__, *args, **kwargs)
'''

print("--------------self约定原理----------------")


# @staticmethod 原理
class Sta(object):
    @staticmethod
    def m():
        pass


sta = Sta()
print(Sta.m)  # function Sta.m at 0x000002A48BA54F28
print(sta.m)  # function Sta.m at 0x000002A48BA54F28
print(sta.m is Sta.m)  # True
'''@staticmethod装饰器, 描述器
class staticmethod(object):
    def __init__(self, func):
        self.func = func
    
    def __get__(self, obj, objtype):
        return self.func
'''

print("--------------@staticmethod原理----------------")


# @classmethod 原理

