# encoding: utf-8


a = 1           # a--->1
b = a           # b--->1
a = a + 2       # a--->3

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
G = F[:]
G[0] = 'shrubbery'

print(F)  # ['spam']
print(G)  # ['shrubbery']


