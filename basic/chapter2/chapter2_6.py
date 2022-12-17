# encoding: utf-8

# python中没有基本类型，如下所示，int是引用
a = 1           # a--->1: 创建int对象存1，a指向该对象(a变量存引用值)
b = a           # b--->1: b指向a指向的对象，即将a变量的引用值赋给b变量
a = a + 2       # a--->3: 根据a变量引用取得整数1，和整数2做加法运算，得到整数3，创建int对象存3，a指向该对象

print(a)  # 3
print(b)  # 1

# 练习题
# 1、
A = 'spam'
B = A
B = 'shrubbery'

print(A)  # spam
print(B)  # shrubbery

# 2、
C = ["spam"]
D = C
D.append("shrubbery")
D[0] = 'berry'

print(C)  # ['berry', 'shrubbery']
print(D)  # ['berry', 'shrubbery']

# 3、
F = ['spam']
G = F[:]            # 1、F按分片[:]取值，取出'spam'的引用值，2、创建列表对象存引用值，G指向该对象
G[0] = 'shrubbery'

print(F)  # ['spam']
print(G)  # ['shrubbery']

# 4、
N = [1, 2]
F = ['spam', N]
G = F[:]     # 1、F按分片[:]取值，取出'spam'、N的引用值，2、创建列表对象存引用值，G指向该对象

# G的第二个元素和F的第二个元素都指向N变量指向的列表对象
print(F[1] is G[1])  # True
print(F[1] is N)     # True
# 所以此时要特别注意，因为列表是可变对象


