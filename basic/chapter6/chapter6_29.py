from collections.abc import Iterable
from collections.abc import Iterator


# 运算符重载
# 协议方法def __iter__(self)，看方法名称+参数
class A:
    def __iter__(self, aa):
        pass


print(isinstance(A, Iterable))  # False
# for x in A():  # TypeError: __iter__() missing 1 required positional argument: 'aa'
#    pass


class B:

    # def __getitem__(self, item):
    #    return item

    def __getitem__(self):
        return "other"


b = B()
# print(b[0])  # TypeError: __getitem__() takes 1 positional argument but 2 were given

# todo,按需
