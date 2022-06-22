

# 单例对象
class Meta(type):
    def __call__(cls, *args, **kwargs):
        # error: type(cls, *args, **kwargs) , 应该: type.__call__(type, cls, *args, **kwargs)
        return type.__call__(cls, *args, **kwargs)


class SingletonMeta(type, metaclass=Meta):

    def __new__(mcs, *args, **kwargs):
        cls = type.__new__(mcs, *args, **kwargs)
        return cls

    def __init__(cls, *args, **kwargs):
        pass

    def __call__(cls, *args, **kwargs):
        try:
            exists = cls.instance
            if exists is not None and isinstance(exists, Singleton):
                return exists
        except AttributeError:
            pass
        ins = type.__call__(cls, *args, **kwargs)
        type.__setattr__(cls, 'instance', ins)
        return ins

    def __setattr__(self, key, value):
        if key == 'instance':
            try:
                exists = self.instance
                if exists is not None and isinstance(exists, Singleton):
                    return
            except AttributeError:
                pass
            type.__setattr__(self, key, value)
        else:
            type.__setattr__(self, key, value)

    def __delattr__(self, item):
        if item == 'instance':
            try:
                exists = self.instance
                if exists is not None and isinstance(exists, Singleton):
                    return
            except AttributeError:
                pass
            type.__delattr__(self, item)
        else:
            type.__delattr__(self, item)


class Singleton(object, metaclass=SingletonMeta):

    @staticmethod
    def getInstance():
        return Singleton()


Singleton.instance = "1"
Singleton.instance = "2"
del Singleton.instance
Singleton.instance = "3"
Singleton.i = "111"
print(dir(Singleton))  # 'getInstance', 'i', 'instance'

s1 = Singleton()
print(dir(s1))  # 'getInstance', 'i', 'instance'
s2 = Singleton.getInstance()
print(s1 is s2)  # True
Singleton.instance = "2"
print(Singleton.instance is s1)  # True

del Singleton.instance
print(Singleton.getInstance() is s1)  # True

s1.sl_attr = "yyyy"
print(s2.sl_attr)  # yyyy

