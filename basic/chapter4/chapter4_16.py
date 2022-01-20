
# 并没import builtins，调用open函数(注意在python中函数名实际上就是变量名)，使用open这个名称搜索: 从本module作用域开始搜索
#   没有搜到，在到默认的builtins module中搜索
wf = open("tm", 'w', encoding="utf-8")
wf.close()


# 本module中创建与open同名的函数
def open(file: str, mode: str, encoding: str):
    print("module_open")


open("tm", 'w', encoding="utf-8")  # module_open, 搜索open: 从本module搜到

module_param = "module_param"
function_param = "module_function_param"


# def执行，创建一个函数对象class function，创建变量function_name保存函数对象的引用值 (这和lst = [1, 2, 3]没有本质的区别)
def function_name(param: int, param2: int, param3='3'):

    print(module_param)  # module_param，从本地作用域开始搜索，在全局作用域(本module)找到了
    function_param = "function_param"  # 在函数中创建变量function_param，其名称和本module中一样
    print(function_param)  # function_name, 变量搜索时先从本地作用域开始，在本地作用域(函数内)找到了

    def open(file: str, mode: str, encoding: str):
        print("function_open")

    open("tm", 'w', encoding="utf-8")  # function_open, 搜索open: 在函数局部作用域搜到

    return param


print(type(function_name))  # <class 'function'>


# 传参:   引用传递(python中没有值传递),该引用值可指向任意对象
# 返回值: 引用传递(python中没有值传递),该引用值可指向任意对象
param = 1
ret_value = function_name(param, 2)  # 函数调用,通过function_name变量名称搜索，执行函数调用
print(param is ret_value)  # True

# 递归: 每次函数(或方法)调用都有一个局部作用域(想一想递归，想一想java中每一个方法调用对应线程栈中的一个栈帧)

# global
global_param = "global_param"


def glb():
    global global_param, global_param1  # 在外部module中查找并引用之，如果外部module没有该变量后续可能在外部module中创建一个同名变量
    global_param1 = 2  # 在外部module中创建变量
    return global_param


print(glb())  # global_param
print(global_param1)  # 2


# 嵌套
def outer():
    n = 2

    def inner():
        return 2 ** n  # 内嵌的函数，函数体中引用变量n，在执行的时候获取变量n（def执行的时候创建function，但此时并不执行函数体代码，所以此时不知道n）
    return inner


outer_inner = outer()
print(outer_inner())  # 4


def outer2():
    ret = []
    for n in range(2):
        ret.append(lambda param1, x=n: param1 ** x)  # lambda的参数列表中使用参数x保存每次循环的n值
    return ret


ou2 = outer2()
print(ou2[0](2))  # 1
print(ou2[1](2))  # 2


# nonlocal
def outer3(n):
    state = n

    def inner():
        nonlocal state  # 在外层def中查找变量state并引用之，如果没有会报错
        state = state + 1
        return state

    return inner


# state闭包，每次调用outer3，产生一个局部变量state,inner使用各自的state
outer3_inner = outer3(2)
print(outer3_inner())  # 3
print(outer3_inner())  # 4, 重复调用inner

outer3_inner_2 = outer3(3)
print(outer3_inner_2())  # 4
print(outer3_inner_2())  # 5

