
# 第二部分练习题

# 第一题1、基础
# /: 浮点数除法，返回值是浮点数
# 输出: 0.4, 2、5是准确存储的，0.4是浮点数，存储是不准确但是能够精确的输出(浮点数表中肯定有这个数的)
print(2 / 5)

# /: 浮点数除法，返回值是浮点数
# 输出: 0.4, 2、5.0是准确存储的，0.4是浮点数，存储是不准确但是能够精确的输出(浮点数表中肯定有这个数的)
print(2 / 5.0)

s = "ham"
ss = s[:0]
print(ss)         # 空字符串
print(type(ss))   # <class 'str'>
print(len(ss))    # 0
if ss:
    print(True)
else:
    print(False)  # 空字符串为false
print(s is ss)    # False，s指向字符串对象"ham", ss指向空字符串对象

lst_a = [1, 2, 3]
lst = lst_a + [4, 5, 6]  # 合并运算
print(lst)  # [1, 2, 3, 4, 5, 6]
print(lst is lst_a)  # False, lst指向一个新的对象
print(lst[0] is lst_a[0])  # True, 拷贝引用值
lst_a[0] = 2     # 无影响
print(lst)  # [1, 2, 3, 4, 5, 6]

print("------1--------\n")

# 第二题、索引运算和分片运算
# 索引赋值，lst[index]=任意对象，将任意对象的引用写入index位置
lst = [1, 2, 3, 4, 5]
lst[4] = []    # 索引赋值
print(lst)     # [1, 2, 3, 4, []]
lst[4] = 'new'
print(lst)     # [1, 2, 3, 4, 'new']
lst[4] = ['n', 'w']
print(lst)     # [1, 2, 3, 4, ['n', 'w']]

print("------2.1--------\n")

# 分片赋值，lst[i:j]=iterable，将iterable中每一个元素的引用写入[i:j)分片
lst = [1, 2, 3, 4, 5]
lst[0:2] = []     # 分片赋值, 当iterable为空时，表示将空赋值过去,理解为特殊的一种删除操作!!!注意
print(lst)        # [3, 4, 5]
lst[0:2] = ['1']  # 分片赋值，将列表iterable后写入
print(lst)        # ['1', 5]
lst[0:2] = 'new'  # 分片赋值，将字符串iterable后写入
print(lst)        # ['n', 'e', 'w']
# lst[0:2] = 1      # 报错: can only assign an iterable

print("------2.2--------\n")

# 索引index超界，取值、赋值、按索引删除均报错
lst = [1, 2, 3, 4, 5]
# lst[100]  # 索引取值时，index超界报错: index out of range
# lst[100] = 'n'  # list assignment index out of range

print("------2.3--------\n")

# 分片时i、j超界, 取值、赋值、按分片删除,i、j自动转换成默认值
lst = [1, 2, 3, 4, 5]
print(lst[-10:100])  # 分片取值时，i、j超界，自动传换成默认值: [1, 2, 3, 4, 5]
lst[2:100] = ['new']
print(lst)           # 分片赋值时，i、j超界，自动传换成默认值: [1, 2, 'new']

print("------2.4--------\n")

# 分片时i>j, 取值、赋值、按分片删除,其[i:j]缩放成[i:i]
lst = [1, 2, 3, 4, 5]
print(lst[3:1])     # 分片取值时，i>j,缩放成[i:i]: []
lst[3:1] = ['new']  # 分片赋值时，i>j,缩放成[i:i]
print(lst)          # [1, 2, 3, 'new', 5]

print("------2.5--------\n")

# 第三题、del
lst = [1, 2, 3, 4, 5]
del lst[0]     # 按索引删除，index超界报错
print(lst)     # [2, 3, 4, 5]
del lst[0:2]   # 按分片删除，分片超界，自动传换成默认值，分片i>j，所缩放成[i:i]
print(lst)     # [4, 5]


# 第四题
x = 'spam'
y = 'eggs'
x, y = y, x   # 只能说赋值运算符'='的优先级是比较低的
print(x)     # eggs
print(y)     # spam

print("------4--------\n")

# 第六题
# d = {'a': 1, 'c': 2}
# print(d['d'])   # 直接报错，KeyError: 'd'！！！注意
dic = {'a': 1, 'c': 2}
print(dic)
dic['d'] = '插入'
dic['c'] = '覆盖c'
print(dic)       # {'a': 1, 'c': '覆盖c', 'd': '插入'}

print("------5--------\n")

# 第七题
# print('123' + [1, 2, 3])  # 报错: can only concatenate str (not "list") to str
# print([1, 2] + ('123', '3'))  # 报错: can only concatenate list (not "tuple") to list
# print({'a': 123, 'b': '54'} + "12345")  # 报错: unsupported operand type(s) for +: 'dict' and 'str'，dict报错类型不一样


