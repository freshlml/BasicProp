

# class type:
#    __class__ = class type  # type类指向自己，type是class type类型
#
#    def __call__(cls, *args, **kwds):
#      tag1: {
#        cls is type
#        cls_ins = cls.__new__(cls, 'C', bases, attribute_dict)  # 构造cls类的实例对象
#        cls.__init__(cls_ins, 'C', bases, attribute_dict)  # 触发cls类的__init__方法
#        return cls_ins
#      }
#      tag2: {
#        cls is C
#        ins = cls.__new__(cls, 'C', bases, attribute_dict) # object中__new__, 构造cls类的实例对象
#        cls.__init__(ins, 'C', bases, attribute_dict) # object中__init__, 触发cls类的__init__方法
#        return ins
#      }
#      tag3: {
#        cls is SpamMeta
#        cls_ins = cls.__new__(cls, 'Spam', bases, attribute_dict)  # SpamMeta.__new__(cls, ...)
#        cls.__init__(cls_ins, 'Spam', bases, attribute_dict)  # SpamMeta.__init__(cls_ins, ...)
#        return cls_ins
#      }
#      tag4': {
#        cls is Spam
#        ins = cls.__new__(cls, 'Spam', bases, attribute_dict) # object中__new__, 构造cls类的实例对象
#        cls.__init__(ins, 'Spam', bases, attribute_dict) # object中__init__, 触发cls类的__init__方法
#        return ins
#      }
#
# class C(object):
#    __class__ = class type  # 类指向class type，C是class type类型
#
#    def __call__(self):
#       pass
#
#    # tag1:
#    # type的__class__指向自己(type是class type类型), 触发class type的__call__(type, 'C', bases, attribute_dict)
#    C = type('C', bases, attribute_dict)
#
# # tag2:
# # C.__class__是class type类型，触发其__call__(C, 'C', bases, attribute_dict)
# c_ins = C()
#
# c_ins的__class__指向C，触发其__call__(c_ins, param)
# c_ins(param)
#

class SpamMeta(type):

    def __new__(mcs, *args, **kwargs):
        print("SpamMeta __new__", type(mcs))  # SpamMeta __new__ <class 'type'>
        print("SpamMeta __new__", mcs)  # SpamMeta __new__ <class '__main__.SpamMeta'>
        cls = type.__new__(mcs, *args, **kwargs)
        print("SpamMeta __new__", cls)  # SpamMeta __new__ <class '__main__.Spam'>
        return cls

    def __init__(cls, *args, **kwargs):
        print("SpamMeta __init__", type(cls))  # SpamMeta __init__ <class '__main__.SpamMeta'>
        print("SpamMeta __init__", cls)  # SpamMeta __init__ <class '__main__.Spam'>
        cls.s = "s"

    # tag4:
    def __call__(cls, *args, **kwargs):
        print("SpamMeta __call__", type(cls))  # SpamMeta __init__ <class '__main__.SpamMeta'>
        print("SpamMeta __call__", cls)  # SpamMeta __init__ <class '__main__.Spam'>
        # tag4'
        ins = type.__call__(cls, *args, **kwargs)
        ins.tag = "tag"
        return ins

    # tag1:
    # class type, __call__(type, 'SpamMeta', bases, attribute_dict)
    # SpamMeta = type('SpamMeta', bases, attribute_dict)


print(type(SpamMeta))  # <class 'type'>
print(SpamMeta.__class__)  # <class 'type'>


class Spam(object, metaclass=SpamMeta):
    def __init__(self, param):
        self.param = param
        print("Spam __init__")

    def __call__(self, *args, **kwargs):
        print("Spam __call__")

    # tag3:
    # SpamMeta的__class__指向class type, __call__(SpamMeta, 'Spam', bases, attribute_dict)
    # Spam = SpamMeta('Spam', bases, attribute_dict)


print(type(Spam))  # <class '__main__.SpamMeta'>
print(Spam.__class__)  # <class '__main__.SpamMeta'>

print(Spam.s)  # s

# tag4:
# Spam是class SpamMeta类型，触发其__call__(Spam, 'spam', ...)
spam = Spam("param")
spam()
print(spam.tag, spam.param)  # tag param


# 类的类型是其元类，元类的类型是其元类, 最上层元类的类型是class type
# 类class执行: 元类的元类的__call__, 元类的__new__,__init__
# 类的实例对象: 元类的__call__

