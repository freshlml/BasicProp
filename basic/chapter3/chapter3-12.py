
# 真值测试
# 非零数字和非空字符串为True，数字0和空字符串为False，None是False
# list、tuple、dic、set递归比较 or relative with __bool__方法 todo

print(type(True))  # <class 'bool'>, bool类型对象，存True(整数1)
print(type(False))  # <class 'bool'>, bool类型对象，存False(整数0)

# 逻辑运算， and、or、not
# a and b:  测试对象a，如果对象a为False返回对象a(短路)[注意不是返回False对象]
lo = 0
ret = lo and '1'
print(ret)        # 0
print(ret is lo)  # True
print(type(ret))  # <class 'int'>

# a and b: 测试对象a，如果对象a为True，返回对象b
lo = ''
ret = 1 and lo
print(ret)        # ''
print(ret is lo)  # True
print(type(ret))  # <class 'str'>

# a or b: 测试对象a，如果对象a为True，返回对象a(短路)[注意不是返回True对象]
lo = 1
ret = lo or ''
print(ret)        # 1
print(ret is lo)  # True
print(type(ret))  # <class 'int'>

# a or b: 测试对象a，如果对象a为False，返回对象b
lo = ' '
ret = 0 or lo
print(ret)        # ' '
print(ret is lo)  # True
print(type(ret))  # <class 'str'>

# 虽然是逻辑运算的规则不同(一般的逻辑运算返回true or false), 但与真值表一致
lo = 1
if lo or '':
    print("真值测试")


