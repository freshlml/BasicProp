import sys

# 赋值语句

# 变量 = 任意对象
bl = "spam"
# bl = ['s', 'p', 'a', 'm']


# 元组赋值
# 变量a, 变量b = 任意对象1, 任意对象2 相当于 (变量a, 变量b) = (任意对象1, 任意对象2)
obj1 = "123"
obj2 = 1
param1, param2 = obj1, obj2  # (obj1, obj2)创建临时tuple,然后iterable

# 列表赋值
# [变量a, 变量b] = [任意对象1, 任意对象2]
obj1 = "123"
obj2 = 1
[param1, param2] = [obj1, obj2]  # [obj1, obj2]创建临时list,然后iterable
print(param1)            # 123
print(param1 is obj1)    # True


# 通用化: 变量1, 变量2/(变量1, 变量2)/[变量1, 变量2] = iterable
# 通用化例子: 变量a, 变量b, 变量c, 变量d = iterable
a, b, c, d = bl
print(a)           # s
print(type(a))     # class<'str'>
print(a is bl[0])  # True
print(c)           # a
print(type(c))     # class<'str'>
print(c is bl[2])  # True
# 特殊用法: 嵌套 ((变量01, 变量02), 变量10)/[[变量01, 变量02], 变量10] = iterable,其中iter(0)也需要是iterable
((param01, param02), param10) = "xp", 1
print(param01)     # x
for ((a, b), c) in [([1, 2], 3), [(4, 5), 6]]:
    print(a, b, c)

# 变量first, *变量remain = iterable
first, *remain = bl
print(first)           # s
print(type(first))     # class<'str'>
print(first is bl[0])  # True
print(remain)              # ['p', 'a', 'm']
print(type(remain))        # class<'list'>
print(remain[0] is bl[1])  # True
# a, *b, c, *d, e = "123456789"  # error: two starred expressions,所以最多只能有一个*
# *a = "123"                     # error: starred assignment target must be in a list or tuple
*a, = "123"                # ['1', '2', '3']
a, *b = "12"               # b只有一个值，仍然是list: ['2']
a, *b = "1"                # b是空list: []


# 变量1 = 变量2 = 任意对象
sp = hm = "123"
print(sp)             # 123
print(hm)             # 123
print(sp is hm)       # True


# 运算符赋值，eg param += 1
# 不可变对象
i = 1
j = i
i += 1  # the same as i = i + 1
print(i)        # 2
print(j)        # 1
print(i is j)   # False
# 可变对象
lst = [1, 2]
m = lst
lst += 'new'      # the same as lst.extend(iterable), note: l = [1, 2] + 'new'合并运算类型不同时报错
print(lst)        # [1, 2, 'n', 'e', 'w']
print(m)          # [1, 2, 'n', 'e', 'w']
print(m is lst)   # True
# lst += 3   # error: 'int' object is not iterable

# note: +=可以理解成运算符重载，每一个类型只要重载了+=就可以使用+=


# print函数
# note: file参数的协议是_Writer, _Writer协议定义write(str)方法,即只要定义了write(str)方法的类型都可以
#       函数传值只是传递引用值，引用值可任意指向任意类型对象，在运行时通过引用值拿到对象才知道对象类型
#       print(1, "2", [1, '3'], sep=' ', end="\n", file=1)  # 在运行时使用file.write(str)方法，只是class<'int'>没有定义该方法罢了
print(1, "2", [1, '3'], sep=' ', end="\n", file=sys.stdout)
print(type(sys.stdout))  # <class '_io.TextIOWrapper'>
print(type(sys.stderr))  # <class '_io.TextIOWrapper'>

wf = open("tm", 'w', encoding="utf-8")
print(type(wf))          # <class '_io.TextIOWrapper'>
print(1, "2", [1, '3'], sep=' ', end="\n", file=wf, flush=True)

wf.close()

# sys.stdout重定向，注意与shell中标准输出流的重定向概念上是不同的
# orig = sys.stdout
# sys.stdout = open("tm", 'w', encoding="utf-8")
#   do something
# sys.stdout.close()
# sys.stdout = orig



