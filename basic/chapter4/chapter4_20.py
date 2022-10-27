

# 生成器函数
def generate(n: int = 5):
    for i in range(n):
        # print("测试是否函数调用时函数代码是否会执行")
        yield i
        # print(i)  # 测试在哪里挂起


ret = generate(2)  # 函数调用，返回一个class generator对象 (此时函数代码未执行)
print(type(ret))  # <class 'generator'>， is Iterator
print(dir(ret))
# 每次__next__方法调用，它会从上次挂起位置(yield执行之后挂起)恢复执行 或者 从头开始执行
print(ret.__next__())  # 0
print(ret.__next__())  # 1
# print(ret.__next__())  # StopIteration
print("------------1--------")


def generate2(n: int = 5):
    i = 0
    while i < n:
        v = yield i
        if v is not None:
            i = v
        else:
            i = i + 1


ge = generate2(10)
# print(ge.send(5))  # TypeError: can't send non-None value to a just-started generator
print(next(ge))  # 0
# 调用send方法，从挂起位置唤醒并且将值传递过去
print(ge.send(5))  # 5

ge.close()
# ge.__next__()  # StopIteration

print("------------2--------")

# 生成器表达式: class generator = (expression for x in iterable if predicate)
lst = [1, 2, 3]
gene = (x * 10 for x in lst)
print(type(gene))  # <class 'generator'>， is Iterator

print(next(gene))  # 10
print(next(gene))  # 20
print(next(gene))  # 30
# print(next(gene))  # StopIteration

# 构造list时引用值拷贝，而没有深拷贝
lst2 = [x for x in lst]
print(lst2[0] is lst[0])  # True

lst3 = list(x for x in lst)
print(lst3[0] is lst[0])  # True

