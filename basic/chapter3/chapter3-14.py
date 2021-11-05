from collections.abc import Iterable
from collections.abc import Iterator

# Iterable(可迭代的): 定义了__iter__方法的对象是可迭代的(Iterable), "可迭代的"协议的定义在class Iterable中
#           __iter__方法，需要返回迭代器对象(即定义了__next__方法的对象)，或者返回Iterator(同时定义了__iter__和__next__方法)

# Iterator(迭代器): 定义了__iter__、__next__方法的对象是迭代器，"迭代器"协议的定义在class Iterator中
#           迭代器的__iter__方法返回自身(因为他自身就定义了__next__方法),迭代器的__next__方法迭代自身
# note: 很多地方说需要Iterator类型，实际理解成需要__next__方法(而如果定义了__next__方法，那么__iter__方法就是举手之劳的，所以单独只定义__next__可行但是不规范)

# 迭代器对象: 定义了__next__方法的对象是迭代器对象
#           迭代器对象调用__next__方法不断迭代自身，在一系列迭代之后到达迭代器对象尾部，若再次调用.__next__方法，则触发StopIteration异常


# class range(object)定义了__iter__方法，没有定义__next__方法
rg = range(5)
print(isinstance(rg, Iterable))  # True
print(isinstance(rg, Iterator))  # False
print(isinstance(rg.__iter__(), Iterator))  # True

# class list(object)定义了__iter__方法，没有定义__next__方法
lst = []
print(isinstance(lst, Iterable))  # True
print(isinstance(lst, Iterator))  # False
# class list的__iter__方法，返回list_iterator(对list进行遍历的Iterator)
print(lst.__iter__())  # <list_iterator object at 0x00000194340C5710>
print(isinstance(lst.__iter__(), Iterator))  # True, list_iterator是Iterator

# str、tuple、dict、set这些类型均定义了__iter__方法，没有定义__next__方法

# _io./class TextIOWrapper(_TextIOBase)定义了__next__方法，基类_IOBase定义了__iter__方法
tm = open("tm", 'r', encoding="utf-8")
print(isinstance(tm, Iterable))  # True
print(isinstance(tm, Iterator))  # True
print(tm.__iter__() is tm)       # True, 返回自身

print("---------1--------")


class B(object):
    def __init__(self):
        self.num = 1

    def __next__(self):
        if self.num:
            ori = self.num
            self.num = 0
            return ori
        raise StopIteration


class A(object):
    def __iter__(self):
        return B()

# for param in Iterable的逻辑代码:
#  1、nextOrIterator = Iterable.__iter__()
#  2、nextOrIterator.__next__()迭代

# for x in B():  # 报错, 'B' is not iterable
#    pass


# iter函数、next函数（@see Python 3.8标准库参考）
a = A()
a_iter = iter(a)     # 接收一个Iterable iterable参数，调用iterable.__iter__方法返回
print(type(a_iter))  # <class '__main__.B'>

n = next(a_iter)   # 接收一个定义了__next__方法的对象，调用__next__方法获取下一个元素，如果迭代器耗尽，则返回给定的default，如果没有默认值则触发StopIteration
print(n)
# next(a_iter)     # StopIteration

print("---------2--------")









