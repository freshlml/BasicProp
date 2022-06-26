from array import array
from collections.abc import Iterable
from collections.abc import Iterator

# list与array存储形式不同
lst = [1, 2, 3, 4]                # lst指向class list的实例对象，实例对象空间中的数组，存class int实例对象的引用
arr = array("l", (1, 2, 3, 4))    # arr指向class array的实例对象，实例对象空间的数组，存数值，模型等同于 java中primitive数组


a_l = array("l", (1, 2147483647, -2147483648))  # 4个字节有符号整数数组，max=2^31-1=2147483647; min=-2^31=-2147483648
print(a_l)
a_L = array("L", (1, 4294967295, 0))  # 4个字节无符号整数数组，max=2^32-1=4294967295; min=0
print(a_L)

# 1个字节无符号整数数组，max=2^8-1=255; min=0
a_B = array("B", [0, 1, 3, 2, 255])

# is mutable
# 支持通用索引操作，分片操作
a_B[0] = 123
print(a_B[0:2])  # 分片取值
print(a_B[0])   # 索引取值

# is iterable, but is not Iterator
print(isinstance(a_B, Iterable))  # True
print(isinstance(a_B, Iterator))  # False

# 有序性



