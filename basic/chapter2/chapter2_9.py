
# 1、相对路径和绝对路径
# 相对路径: 相对于python命令执行时所在的目录（当前工作目录）,os.getcwd()
#    D:\pyProjects\BasicProp\basic>python chapter2/chapter2_9.py
# 绝对路径: linux中，/dir/**/*
#   win中，C:\dir\**\*

# 字符串写，编码=utf-8
# 传入字符串，字符串按encoding编码成字节序列，写入字节序列
wf = open("tm", 'w', encoding="utf-8")
wf.write("字符串")    # 参数传字符串类型
wf.write(" 换行\n")   # 参数传字符串类型
wf.write((str(["123", 2]) + "\n"))   # 其他类型，转换成字符串
lst = ["1", "2", '3']
wf.writelines(lst)   # 参数传可迭代类型，每一个元素是字符串

wf.flush()
wf.close()


# 字符串读，编码=utf-8
# 读出字节序列，按encoding解码成字符串，返回字符串
rf = open("rd", 'r', encoding="utf-8")
# sa = rf.read()        # 读取全部内容，返回字符串
# print(type(sa))       # class<'str'>
# print(sa)
# sls = rf.readlines()  # 返回class<'list'>, 每一个元素是字符串
# print(type(sls))      # class<'list'>
# print(sls)
i = 1
while i > 0:
    s = rf.readline()  # 读取一行,返回的结果末尾带换行符
    i = len(s)
    if s.endswith("\n"):
        s = s[0:-1]
    # print(s)

rf.close()

# 字符串读，编码=utf-8
# 读出字节序列，按encoding解码成字符串，返回字符串
rf = open("rd", 'r', encoding="utf-8")
i = 1
while i > 0:
    s = rf.read(10)  # 读取十个字符
    i = len(s)
    s = s.replace("\n", '')
    # print(s)

rf.close()


# 字节读，截断现象
# 读出字节序列，返回字节序列
rf = open("rd", 'rb')
i = 1
while i > 0:
    s = rf.read(10)  # 读取十个字节
    i = len(s)
    # s = s.replace("\n", '')
    # print(s.decode("utf-8", errors="replace"))  # 如果字节序列转化成字符串，截断现象

rf.close()


# 字节写
# 外部转化成字节序列，传入字节序列，写入字节序列
wf = open("tm", 'wb')
wf.write("中h𝄞\n".encode("utf-8"))  # 字符串encode成字节序列后写入
wf.write((str(1)+"\n").encode("utf-8"))  # 数字先转换成字符串，然后encode成字节序列后写入
wf.write((str(["123", 2]) + "\n").encode("utf-8"))  # list先转换成字符串，然后encode成字节序列后写入

wf.flush()
wf.close()


# 字节读
# 读出字节序列，返回字节序列
rf = open("tm", 'rb')
one = rf.readline()
print(one.decode("utf-8").replace("\n", ""))  # 第一行是字符串
two = rf.readline()
print(int(two.decode("utf-8")))  # 第二行是数字，调用int函数转换
the = rf.readline()
print(eval(the.decode("utf-8")))  # 第三行是list，eval函数

rf.close()




