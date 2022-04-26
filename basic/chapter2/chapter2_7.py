
# ord函数返回一个unicode字符的码点, chr函数on the contrary
print(hex(ord('中')))   # 0x4e2d
print(hex(ord('h')))   # 0x68             0110 1000
print(hex(ord('𝕆')))   # 0x1d546
print(hex(ord('中')))   # 0x4e2d          0100 1110 0010 1101
print(hex(ord('😚')))   # 0x1f61a
print(hex(ord('符')))   # 0x7b26
print(hex(ord('𝄞')))   # 0x1d11e          0001 1101 0001 0001 1110

print(chr(0x1f61a))     # 😚
print(chr(0x4e2d))      # 中
print(chr(0x1D11E))     # 𝄞

print("-----------1-----------\n")

# 没有字符类型
s = '中h𝄞'
print(type(s[0]))  # class<'str'>
print(s[0][0][0])  # 中
lst = ['s', 'f']
print(type(lst[0]))  # class<'str'>
print(lst[0][0][0])  # s

# 字符串类型
s = '中h𝄞'      # 字符串str有三个unicode字符，str对象的内存空间中存的是unicode字符的码点[0x4e2d,0x68,0x1d11e]
print(type(s))  # <class 'str'>, 字符串类型
print(len(s))   # 3, 一个字符为一个元素;    java中的char(因为限定了两个字节的大小)则存在缺陷
print(s)        # 中h𝄞

print("-----------2-----------\n")


ba = '中h𝄞'.encode("utf-8")  # '中'按utf-8编码: 0xe4b8ad,三个字节存放, h:0x68,一个字节, '𝄞'按utf-8编码: 0xf09d849e,四个字节存放
print(type(ba))  # <class 'bytes'>, 字节序列类型
print(len(ba))   # 8, 3+1+4=8,一个字节为一个元素(类似字节数组)
print(ba)        # b'\xe4\xb8\xadh\xf0\x9d\x84\x9e', <=0x7f转化成字符,否则输出字节的十六进制值，注意utf-8多字节时每个字节都比0x7f大(但utf-16等其他编码中就不一定了)
#                 \xe4 \xb8 \xad h(0x68) \xf0 lx9d lx84 lx9e

print("----------3------------\n")


# 字节序列类型
# b = b'中h𝄞'   # error bytes can only contain ASCII literal characters
b = b'1aA'      # 每个字符的码点必须<=0x7f
print(type(b))  # <class 'bytes'>, 字节序列类型
print(len(b))   # 3, 每个字符的码点<=0x7f, 一个字符需要一个字节存储, 一个字节为一个元素(类似于字节数组)
print(b)        # b'1aA'
# b[0] = '2'      # 不能索引修改
nb = b.replace(b'1', b'2')
print(b)          # b'1aA'
print(nb)         # b'2aA'
print(nb is b)  # False      <class 'bytes'>不可变

print("-----------4-----------\n")


# 编码与解码

# utf-8
ba = '中h𝄞'.encode("utf-8")  # '中'按utf-8编码: 0xe4b8ad,三个字节存放, h:0x68,一个字节, '𝄞'按utf-8编码: 0xf09d849e,四个字节存放
print(len(ba))   # 8, 3+1+4=8
print(ba)        # b'\xe4\xb8\xadh\xf0\x9d\x84\x9e', <=0x7f转化成字符,否则输出字节的十六进制值，注意utf-8多字节时每个字节都比0x7f大(但utf-16等其他编码中就不一定了)
#                 \xe4 \xb8 \xad h \xf0 lx9d lx 84 lx9e
print(ba.decode("utf-8"))  # 中h𝄞

print("-----------5-----------\n")


# utf-16
baa = '中h𝄞'.encode("utf-16")  # 默认使用cpu的字节序，intel是小字节序，'中'按utf-16le编码: 0x2d4e,两个字节，h: 0x6800,两个字节，'𝄞': 0x34d81edd,四个字节
print(len(baa))   # 10   小字节序标记0xff 0xfe需要两个字节2+2+2+4=10
print(baa)        # b'\xff\xfe-Nh\x004\xd8\x1e\xdd'
#                   \xff \xfe -(0x2d) N(0x4e) h(0x68) \x00 4(0x34) \xd8 \x1e \xdd
print(baa.decode("utf-16"))  # 中h𝄞, 解码

print("-----------6-----------\n")


# utf-16le
baa = '中h𝄞'.encode("utf-16le")  # 使用小字节序，'中'按utf-16le编码: 0x2d4e,两个字节，h: 0x6800,两个字节，'𝄞': 0x34d81edd,四个字节
print(len(baa))   # 8, 使用utf-16le没有添加bom
print(baa)        # b'-Nh\x004\xd8\x1e\xdd'
#                   -(0x2d) N(0x4e) h(0x68) \x00 4(0x34) \xd8 \x1e \xdd
print(baa.decode("utf-16le"))  # 中h𝄞, 解码

print("-----------7-----------\n")


# utf-16be
baa = '中h𝄞'.encode("utf-16be")  # 使用大字节序，'中'按utf-16be编码: 0x4e2d,两个字节，h: 0x0068,两个字节，'𝄞': 0xd834dd1e,四个字节
print(len(baa))   # 8, 使用utf-16be没有添加bom
print(baa)        # b'N-\x00h\xd84\xdd\x1e'
#                   N(0x4e) -(0x2d) \x00 h \xd8 4(0x34) \xdd \x1e
print(baa.decode("utf-16be"))  # 中h𝄞, 解码

print("-----------8-----------\n")


# 其他编码
# o = '中h𝄞'.encode("gbk")      # '𝄞'字符不能映射到gbk直接报错: UnicodeEncodeError
o = '中h𝄞'.encode("gbk", errors='ignore')  # '𝄞'字符不能映射到gbk时，指定ignore（跳过错误的字符）
print(o.decode("gbk"))  # 中h, 解码后𝄞没有了
o = '中h𝄞'.encode("gbk", errors='replace')  # '𝄞'字符不能映射到gbk时，使用替代字符(这也是java中的策略)
print(o.decode("gbk", errors='replace'))  # 中h?

print("-----------9-----------\n")






