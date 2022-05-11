

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
print("---1----------------")


# 属性管理: 描述符协议class Descriptor
class Name(object):
    def __get__(self, instance, owner):
        if instance is not None:
            return instance.cap_name
        return owner.cap_name

    def __set__(self, instance, v):
        if v:
            instance.cap_name = v

    def __delete__(self, instance):
        del instance.cap_name


class B(object):
    name = Name()

    def __init__(self, name):
        self.cap_name = name


b = B(1)
b.name = "任意"  # 翻译成b.name.__set__(b, "任意")
print(b.name)  # 翻译成b.name.__get(b, b.__class__)
print("---2----------------")


# 属性管理: 协议方法 @link chapter6_29_3





