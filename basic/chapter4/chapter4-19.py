from functools import reduce


def function_name(*params):
    pass


print(dir(function_name))
print(type(function_name))  # <class 'function'>

cd = function_name.__code__
print(dir(cd))
print(type(cd))  # <class 'code'>
print(cd.co_varnames)  # ('params',)


# 函数对象设置属性(就像是为函数对象设置非static的public成员变量一样)
function_name.public_attr = "public_attr"
print(dir(function_name))


# 注释，参数和返回值添加注释，给调用者以提示
def ni(a: int, b: 'str类型' = 4) -> int:
    pass


# 注意不要和"注解"搞混了
print(ni.__annotations__)  # {'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'int'>}

print("-----------------")

# lambda arg1[=default_value],arg1,...: expression
p = lambda param='default_value': param
print(type(p))  # <class 'function'>
print(p("lambda"))  # lambda

print("-----------------")

# map
lst = [1, 2, 3]
tp = ('1', '2', '3', '4')
ret = map((lambda x, y: (x+10, y+'-', )), lst, tp)
print(type(ret))  # <class 'map'>, is Iterator
for p in ret:
    print(p)
# (11, '1-')
# (12, '2-')
# (13, '3-')
if ret: print("123")

lst = [[1], [2], [3]]
ret = map(lambda x: x.append('x'), lst)
elem = ret.__next__()
print(elem)  # None
print(lst[0])  # [1, 'x']
print(lst[1])  # [2]


# 函数式编程
# 流式调用 or 嵌套调用
# list.stream().filter(elem -> elem.isJava()).map(elem -> elem.getId()).reduce(Integer::sum)
lst = [1, 2, -1, 4, -2]
one = filter(lambda x: x > 0, lst)  # class filter, is Iterator
two = map(lambda x: x+1, one)
ret = reduce(lambda x, y: x+y, two)  # reduce是函数
print(ret)  # 10


