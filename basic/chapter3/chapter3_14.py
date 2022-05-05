from collections.abc import Iterable
from collections.abc import Iterator

# _collections_abc
# Iterable(可迭代的): 定义了__iter__方法的对象是可迭代的(Iterable), "可迭代的"协议的定义在class Iterable中
#           __iter__方法，需要返回迭代器对象(即定义了__next__方法的对象)，或者返回Iterator(同时定义了__iter__和__next__方法)

# Iterator(迭代器): 定义了__iter__、__next__方法的对象是迭代器，"迭代器"协议的定义在class Iterator中
#           迭代器的__iter__方法返回自身(因为他自身就定义了__next__方法),迭代器调用__next__方法进行迭代
# note: 很多地方说需要Iterator类型，实际理解成需要__next__方法(而如果定义了__next__方法，那么__iter__方法就是举手之劳的，所以单独只定义__next__可行但是不规范)

# 迭代器对象: 定义了__next__方法的对象是迭代器对象
#           迭代器对象调用__next__方法进行迭代，在一系列迭代之后到达迭代器对象尾部，若再次调用.__next__方法，则触发StopIteration异常


# class list(object)定义了__iter__方法，没有定义__next__方法
lst = []
print(isinstance(lst, Iterable))  # True
print(isinstance(lst, Iterator))  # False
# class list的__iter__方法，返回list_iterator，他是一个Iterator
print(lst.__iter__())  # <list_iterator object at 0x00000194340C5710>
print(isinstance(lst.__iter__(), Iterator))  # True

# str、tuple、dict、set这些类型均定义了__iter__方法，没有定义__next__方法
print("---------1.1--------")

# class _io.TextIOWrapper定义了__next__方法，基类class _IOBase定义了__iter__方法
tm = open("tm", 'r', encoding="utf-8")
print(isinstance(tm, Iterable))  # True
print(isinstance(tm, Iterator))  # True
print(tm.__iter__() is tm)       # True, 返回自身

print("---------1.2--------")

# class list的Iterator: list_iterator
lst_n = ['1']
lst = [1, lst_n]
# class list的__iter__方法每调用一次，"新构造"一个list的Iterator返回
lst_iter1 = iter(lst)
lst_iter2 = lst.__iter__()
print(lst_iter1 is lst_iter2)  # False

# class list的Iterator在构造时，保存list的引用到成员变量如lst，同时初始化一个迭代下标如index=0，并没有遍历list中每一个元素，拷贝每一个元素的引用值到新创建的列表
# list的Iterator每次迭代时(调用__next__方法)，使用lst[index]获取元素，同时index=index+1
print(lst_iter1.__next__())        # 1
print(lst_iter2.__next__())        # 1

# lst.pop(1)  # 如果这条语句去掉注释，下面的语句将报StopIteration

p1 = lst_iter1.__next__()
print(p1)         # ['1']

lst_n[0] = '2'

p2 = lst_iter2.__next__()
print(p2)         # ['2']
print(p1 is p2)   # True

# str、tuple、dict、set这些类型和list的迭代器逻辑一致
print("---------1.3--------")

# class dict的keys()、values()、items()
dct = {"a": "aa", "1": 11}
# 每次调用keys()方法，构造一个class dict_keys对象(保存dict的引用值)返回
dct_keys = dct.keys()
print(type(dct_keys))  # <class 'dict_keys'> ?
# class dict_keys定义了__iter__方法,没有定义__next__方法
dct_keys_iter1 = dct_keys.__iter__()  # 每次调用__iter__方法，构造class dict_keyiterator对象返回
dct_keys_iter2 = dct_keys.__iter__()
print(type(dct_keys_iter1))  # <class 'dict_keyiterator'>
print(dct_keys_iter1.__next__())  # a
print(dct_keys_iter2.__next__())  # a

# values和items方法与keys方法一致
dct_values = dct.values()
print(type(dct_values))  # <class 'dict_values'>
print(isinstance(dct_values, Iterable))  # True
print(isinstance(dct_values, Iterator))  # False
dct_items = dct.items()
print(type(dct_items))   # <class 'dict_items'>
print(isinstance(dct_items, Iterable))  # True
print(isinstance(dct_items, Iterator))  # False

print("---------1.4--------")

# class range, 定义了__iter__,没有定义__next__
rg = range(3)
print(isinstance(rg, Iterable))  # True
print(isinstance(rg, Iterator))  # False
# class range的__iter__方法每调用一次，"新构造"一个list的Iterator返回
# class range的Iterator在构造时，保存range的step和stop值，同时初始化一个迭代下标如index=0
rg_iter1 = iter(rg)
rg_iter2 = iter(rg)
print(next(rg_iter1))  # 0
print(next(rg_iter2))  # 0

print("---------1.5--------")

# enumerate、zip、filter
# 定义了__iter__(返回自身，其实还有一种实现，返回构造时的Iterable.__iter__但充满歧义),定义__next__
# 节省内存空间 -->  构造时没有对参数迭代而是拷贝引用值
lst = [1, 2]
ft = filter(None, lst)
print(isinstance(ft, Iterator))  # True
print(ft.__iter__() is ft)       # True，filter的__iter__返回自身
one = next(ft)
two = next(ft)
# when others concurrency add element to lst, three will not be StopIteration
lst.append('3')
three = next(ft)  # StopIteration or not

# 构造器filter(None, lst)执行时，调用list.__iter__方法创建list的Iterator保存，并没有遍历list中每一个元素，拷贝每一个元素的引用值到新创建的列表
#  当对filter迭代(调用__next__方法)时，使用list的Iterator迭代

print("------1.6------")


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
#  2、nextOrIterator.__next__()

# for x in B():  # 报错, 'B' is not iterable
#    pass


# iter函数、next函数（@see Python 3.8标准库参考）
a = A()
a_iter = iter(a)     # 接收一个Iterable，调用iterable.__iter__方法返回
print(type(a_iter))  # <class '__main__.B'>

n = next(a_iter)   # 接收一个Iterator(本质上只要定义了__next__方法即可)，调用__next__方法获取下一个元素
print(n)
# next(a_iter)     # StopIteration

print("---------2--------")




