# encoding: utf-8
import math

# 2.5习题
# 1、python中表达式 2 * (3 + 4)的值是多少
# 运算优先级; 整数做加法得到整数; 整数做乘法得到整数;
print(2 * (3 + 4))  # 14

# 4、计算一个数字的平方跟
# math.sqrt函数: 参数可传递一个整数或浮点数, 返回值是一个浮点数;
numb = 16
print(math.sqrt(numb))  # 4.0
numb = 10009998
print(math.sqrt(numb))  # 3163.8580878414887
numb = 16.0
print(math.sqrt(numb))  # 4.0
numb = 16.01
print(math.sqrt(numb))  # 4.001249804748512

# 6、怎么能够截断或者舍去浮点数的小数部分
# math.trunc截断函数; 使用floor除法
flt = 12.45
print(math.trunc(flt))  # 12
flt = -12.456
print(math.trunc(flt))  # -12
print(12.1 // 2)        # 6.0
print(-12.1 // 2)       # -7.0

# 7、如何将一个整数转化为一个浮点数
numb = 18
flt = numb / 1    # 18.0
print(flt)
flt = float(numb)
print(flt)        # 18.0


