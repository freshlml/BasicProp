from collections.abc import Iterable
from collections.abc import Iterator
import datetime
import time

# for param in iterable
lst = [1, 2, '3', [1, '2']]
for perElement in lst:  # 每次iter后拷贝引用值
    print(perElement, end=", ")

print("\n------1------")

tm = open("tm", 'r', encoding="utf-8")
print(type(tm))    # <class '_io.TextIOWrapper'>
print(isinstance(tm, Iterator))  # True
for param in tm:   # <class '_io.TextIOWrapper'> is Iterator,__iter__返回自身，__next__每次返回一行
    print(param, end='')
tm.close()
print()

print("------2------")

tm = open("tm", 'r', encoding="utf-8")
while True:
    param = tm.readline()  # 读取一行
    # param = tm.read(10)  # 读取十个字符
    if not param:
        break
    print(param, end='')

tm.close()
print()

print("------3------")


# for in定制
# 索引遍历、并行遍历

# 索引遍历: class range
lst = [1, '5', 3, [1, '3']]
rg = range(len(lst))  # 构造函数
for i in rg:
    if (i+1) % 2 == 0:
        print(lst[i], end=' ')  # 5 [1, '3']

print()
print("------4------")

# 索引遍历: class enumerate
s = "abclml"
for (param, i) in enumerate(s):
    print(i, param, sep="->", end=' ')  # a->0 b->1 c->2 l->3 m->4 l->5

print()
print("------5------")

# 并行遍历: 使用class zip先合并在遍历
lst1 = [1, '5', 3, [1, '3']]
lst2 = ['a', 'd', "c"]
zp = zip(lst1, lst2)
for lst1Param, list2Param in zp:
    print(lst1Param, list2Param, sep=",", end=' ')  # 1,a 5,d 3,c

print()
print("------6------")

# date
date = datetime.date(1009, 2, 3)  # 指定年，月，日构造date
print(date)  # 1009-02-03

date = datetime.date.today()  # 获取系统默认时区的当前日期
print(date)  # 2022-06-24

# 57600 = 24*60*60 - 8*60*60
date = datetime.date.fromtimestamp(57599)  # 根据时间戳和系统默认时区构造date
print(date)  # 1970-01-01
date = datetime.date.fromtimestamp(57600)
print(date)  # 1970-01-02

print("------------date------------")

# datetime timezone
print(datetime.datetime.now())  # 系统默认时区的当前时间
print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))))  # +8时区的当前时间
print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8, minutes=50))))  # +8时区细分
print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=0))))  # UTC时间(0区的当前时间)

print("------------1-----------")

# 时间戳和时区无关
print(time.time())  # 时间戳
print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8))).timestamp())  # 时间戳
print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=+8, minutes=50))).timestamp())  # 时间戳
print(datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=0))).timestamp())  # 时间戳

print("------------2-----------")

# 根据时间戳构造datetime时，需要指定时区
print(datetime.datetime.fromtimestamp(time.time(), datetime.timezone(datetime.timedelta(hours=+8))))

print("------------3-----------")

# 格式化
print(datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S"))

print("------------4-----------")

# 相等性, datetime存储时区值，相等性比较时进行时区转换
s = time.time()
l8 = datetime.datetime.fromtimestamp(s, datetime.timezone(datetime.timedelta(hours=+8)))
l0 = datetime.datetime.fromtimestamp(s, datetime.timezone(datetime.timedelta(hours=0)))
print(l8)
print(l0)
print(l8 == l0)  # True

'''
时区时间的图形化 time.uxf
 |---------|      UTC(+0)
    |----------|  +8

'''



