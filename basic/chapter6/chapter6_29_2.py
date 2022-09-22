

# Descriptor: 属性查找，属性设置，属性删除时的回调机制
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

# attr1属性在B的mro路径中存在，而不是在B.__class__的mro路径中，所以将为B设置attr1属性而不是调用__set__(...)
# B.attr1 = "覆盖"


# attr1属性存在，不是实例对象属性，并且是Descriptor with __get__方法，调用attr1.__get__(b, b.__class__)
print(b.attr1)  # 任意

# attr1属性存在，不是实例对象属性，并且是Descriptor with __get__方法，调用attr1.__get__(None, B)
print(B.attr1)  # class B

# attr1属性存在，不是实例对象属性，并且是Descriptor with __get__方法，调用attr1.__get__(None, C)
print(C.attr1)  # class C

# 实例对象上的Descriptor属性
b.ins_attr = AttrDescriptor()
# 实例对象上的ins_attr属性是Descriptor with __get__方法，不会调用ins_attr.__get__(None, b)
print(b.ins_attr)  # <__main__.AttrDescriptor object at ...>

print("--------------1----------------")


# property机制类似 Descriptor



