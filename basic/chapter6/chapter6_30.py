from collections.abc import Iterator
from collections.abc import Iterable


# 函数式编程
# 第一：函数式作为参数传递: 将函数作为参数传递, 这在python中有天然的优势，因为py中函数(方法)本身就是class Function的实例对象，py本身就可以传递函数(方法)
# 第二：数据流过一系列函数: python通过迭代器实现
#   1.流式调用:
#       list.stream().filter(elem -> elem.isJava()).map(elem -> elem.getId()).reduce(Integer::sum)
#   2.嵌套式调用:
#       lst = [1, 2, -1, 4, -2]
#       one = filter(lambda x: x > 0, lst)
#       two = map(lambda x: x+1, one)
#       ret = reduce(lambda x, y: x+y, two)
class C(object):

    def m(self, param):
        pass

    @staticmethod
    def s_m(x, y):
        return x+y


# functools module
from functools import reduce
lst = [1, 2, -1, 4, -2]
one = filter(lambda x: x > 0, lst)
two = map(lambda x: x+1, one)
ret = reduce(C.s_m, two)
print(ret)

print("-----------1-----------")

# itertools 和 sys 一样是 built-in module
import itertools
city_list = [('Decatur', 'AL'),
             ('Huntsville', 'AL'),
             ('Anchorage', 'AK'),
             ('Selma', 'AL'),
             ('Nome', 'AK'),
             ('Flagstaff', 'AZ'),
             ('Phoenix', 'AZ'),
             ('Tucson', 'AZ')]


dp = itertools.groupby(city_list, lambda el: el[1])
print(isinstance(dp, Iterator))  # True
print(isinstance(dp, Iterable))  # True
print(dp is dp.__iter__())  # True

al = next(dp)
print(al)
print(isinstance(al[1], Iterator))  # True
for e1 in al[1]:
    print(e1)


ak = next(dp)
print(ak)
for e2 in ak[1]:
    print(e2)


# operator module
import operator

