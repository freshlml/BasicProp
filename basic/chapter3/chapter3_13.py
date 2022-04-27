from collections.abc import Iterable
from collections.abc import Iterator

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




