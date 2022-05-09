

# py中的装饰器
class Decorator(object):
    def __init__(self, calls):
        self.calls = calls

    def __call__(self, *args):
        print("before")
        print(self)  # <__main__.Decorator object at ...>
        print(args)
        print(self.calls)  # <function A.m at ...>
        self.calls(*args)
        print("after")


class A(object):

    @Decorator
    def m(self, params):    # 1.def执行:m = class function，2.@Decorator执行: m = Decorator(m)
        print(self)
        print(params)
        return self


a = A()
print(type(a))  # <class '__main__.A'>
print(type(a.m))  # <class '__main__.Decorator'>
print(type(A.m))  # <class '__main__.Decorator'>
A.m(A(), "pp")  # 1.A.m(A(), "ppp"), 2.Decorator.__call__(m, A(), "pp"), 3.A.m(A(), "pp")
# a.m("params")  # 1.Decorator.__call__(m, "params"), 3.A.m("params")  # a丢失，所以装饰器用在方法，应该用上面个这种方式调用


def dec(obj):
    print("before")
    return obj


@dec
class B(object):    # 1.class执行:B = class type，2.@dec执行:B = dec(B)
    pass
