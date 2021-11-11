
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





