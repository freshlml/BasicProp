

# 属性管理: property特性
class A(object):

    def __init__(self, name):
        self.cap_name = name

    def get_name(self):
        try:
            return self.cap_name
        except AttributeError as e:
            return None

    def set_name(self, v):
        if v:
            self.cap_name = v

    def del_name(self):
        del self.cap_name

    name = property(get_name, set_name, del_name, "cap_name属性")


a = A(1)
a.name = "任意"  # 1.a.name = "任意": 找到A类的name属性；2.翻译成a.set_name("任意")
print(a.name)  # "任意", 1.a.name: 找到A类的name属性；2.翻译成a.get_name()
del a.name  # 1.del a.name: 找到A类的name属性；2.翻译成a.set_name()
print(a.name)  # None
print("--------------1----------------")


# 属性管理: 描述符协议class Descriptor
class Name(object):
    def __get__(self, instance, owner):
        if instance is not None:
            try:
                return instance.cap_name
            except AttributeError:
                return None
        return owner

    def __set__(self, instance, v):
        if v:
            instance.cap_name = v

    def __delete__(self, instance):
        del instance.cap_name


class C(object):
    name = Name()


class B(C):
    pass


b = B()
print(b.__dict__)  # {}

# 如果name属性在b.__class__的mro路径中存在并且name属性是Descriptor with __set__方法，则调用name.__set__(b, '任意')，而不是为b设置name属性
b.name = "任意"
print(b.__dict__)  # {'cap_name': '任意'}

# B.name = "覆盖"  # name属性在B的mro路径中存在，而不是B.__class__的mro路径中存在，所以不满足条件，将为B设置name属性


# b，b.__class__ or b.__class__的mro?
# name属性存在并且是Descriptor with __get__方法，调用name.__get__(b, b.__class__) {在b.__class__的mro路径中搜索到name属性}
print(b.name)  # 任意

# name属性存在并且是Descriptor with __get__方法，调用name.__get__(None, B) {在B的mro路径中搜索到name属性}
print(B.name)  # class B

# name属性存在并且是Descriptor with __get__方法，调用name.__get__(None, C) {在C的mro路径中搜索到name}
print(C.name)  # class C

print("---2----------------")





