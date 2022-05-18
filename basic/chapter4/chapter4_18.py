
class B(object):
    def __init__(self, a):
        self.a = a
        self.pos = 0

    def __next__(self):
        if self.pos < self.a.num:
            self.pos += 1
            return self.pos
        raise StopIteration


class A(object):
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return B(self)


# 参数传递和返回值
# 1、引用传递(python中没有值传递)
# 2、参数是函数中的局部变量
# 3、引用可以指向任意对象，如int、list、function、lambda、declared class

# 函数参数定义:
#  1、def function(param): param可以按位置传参 或者 按关键字传参
#  2、def function(*params):  接收多个(包括0个)按位置传参, 按关键字传参报错
#  3、def function(**params): 接收多个(包括0个)按关键字传参, 按位置传参报错
#  # 通用(混合)形式
#  def function(p1, p2, *p3, p4, p5, **p6)
#      1).p1,p2如果按关键字传参，则*p3传空，p4,p5,**p6按关键字传参
#      2).p1、p2按位置传参，*p3按位置传参，p4、p5只能按关键字传参，p6只能按关键字传参
#  4、如果定义时有默认值，调用时可以不传，默认值在def解析时保存在function对象中，对于每次的函数调用来说是全局的
#     def function(p1, p2, *p3, p4, p5, **p6)
#      1).*p3,**p6不能设置默认值
#      2).p2如果没有默认值，p1不能设置默认值；p4,p5可随意设置默认值 （即: 按位置传参默认值从后向前设置，按关键字传参与顺序无关）
# 函数调用时传参形式: 按位置传参和按关键字传参
#  1、function(*iterable): 迭代后按位置传参
#  2、function(**dict): 解析dict形成key=value,按关键字传参
#  3、function(1),按位置传参，function(param=1),按关键字传参
#  4、按位置传参必须在按关键字传参之前
#  5、如果按关键字传参，顺序无关
#  6、对于有默认值的参数，可以不传值

def multi_param(*params):
    print(type(params))  # <class 'tuple'>
    for p in params:
        print(p, end=" ")


multi_param()
multi_param(1, '2', (1, '22'))  # 1 2 (1, '22')
print()

# multi_param(params=123)  # TypeError: got an unexpected keyword argument 'params'
# multi_param('2', name='1')  # TypeError: got an unexpected keyword argument 'name'
# multi_param(**{'a': 1, 'b': 2, 'c': 3})  # TypeError: got an unexpected keyword argument 'a'

# its = [1, '2', 3]
# its = "123"
# its = {1, 2, 3}
# its = {1: '1', 2: '2', 3: '3'}
its = A(3)
multi_param(*its)  # 1 2 3, 参数需iterable，迭代形成多个参数后按位置传参
print()

print("-------1------")


def multi_param2(**params):
    print(type(params))  # <class 'dict'>
    for p in params:
        print(p, "->", params[p], sep="", end=" ")
    return params


multi_param2()
multi_param2(num1=1, num2=2, str3='3')  # num1->1 num2->2 str3->3
print()

# multi_param2(1, num2=2)  # TypeError: takes 0 positional arguments but 1 was given
# multi_param2(*[1, 2, 3])  # TypeError: takes 0 positional arguments but 3 was given

mp = {'a': 1, 'b': 2, 'c': 3}
ret = multi_param2(**mp)  # a->1 b->2 c->3, 参数必须是dict并且key是str，解析成a=1,b=2,c=3形式，按关键字传参
print()
print(ret is mp)  # False

print("-------2------")


def hh(p1, *p2, p3, **p4):
    print(p1, end=" ")
    for p in p2:
        print(p, end=" ")
    print(p3, end=" ")
    for p in p4:
        print(p, "->", p4[p], sep="", end=" ")


# p1、p2按位置传参，p3、p4按关键字传参
hh(1, 2, 3, p3='4', key5=5, key6=6)  # 1 2 3 4 key5->5 key6->6
print()
# p1按关键字传参，p2只能不传，p3、p4按关键字传参
hh(p1=1, p3='4', key5=5, key6=6)  # 1 4 key5->5 key6->6
print()


print("------2.5------")


# 3、4
def fc(a, b, c):
    print(a, b, c)


fc(1, 2, 3)  # 按位置传参
fc(1, c=3, b=2)  # 按位置传参和按关键字传参混合
fc(*[1, 2, 3])  # 迭代后按位置传参
fc(**{'a': 1, 'b': 2, 'c': 3})  # 解析dict: a=1,b=2,c=3，按关键字传参
fc(1, *[2], **{'c': 3})  # 混合
# fc(a=1, 2, 3)  # 按位置传参必须在按关键字传参之前

print("-------3、4------")

