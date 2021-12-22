from functools import reduce

# 第四部分练习题


# 第二题
def sm(left, right):
    s = left + right  # left or right是否支持+运算，right or left作为参数是否类型匹配
    return s


# print(sm(1, "2"))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("-------2------")


# 第三题
def smm(*params):
    if len(params) == 0:
        return None
    elif len(params) == 1:
        return params[0]
    first = params[0]
    for i in range(len(params)):
        if i == 0:
            continue
        else:
            first = first + params[i]  # first.+运算符协议方法(params[i]): 应该判断first是否支持+运算和参数类型是否匹配
    return first


def smm2(*params):
    ret = reduce(lambda x, y: x+y, params)
    return ret


print(smm([1], [2], [3]))  # [1, 2, 3]
# print(smm(1, "1"))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# print(smm({"1": 1, "2": 2}, {"3": 3}))  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

print(smm2([1], [2], [3]))  # [1, 2, 3]
# print(smm2(1, "1"))  # TypeError: unsupported operand type(s) for +: 'int' and 'str'

print("-------3------")


# 第五题: dict's copy
dc = {"1": 1, "2": 2}
dc2 = {k: dc[k] for k in dc}
print(dc is dc2)  # False
print(dc["1"] is dc2["1"])  # True

print("-------5------")


# 第六题
def un(dict1: dict, dict2: dict) -> dict:
    dcs = {k: dict1[k] for k in dict1}
    for k in dict2:
        dcs[k] = dict2[k]

    return dcs


print(un({"1": 1, "2": 2}, {"3": 3, "2": 2}))


print("-------6------")



