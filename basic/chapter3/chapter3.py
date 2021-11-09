
# 第三部分练习题

# 1、打印字符串s中每个字符的ASCII码 (题目存在歧义)
s = '12ab符😚'
for p in s:
    code_point = ord(p)
    if code_point > 127:
        print("'" + p + "' is not a ASCII字符", end=' ')
    else:
        print(p, end=' ')
print()

lst = [ord(p) if ord(p) <= 127 else "'" + p + "' is not a ASCII字符" for p in s]
print(lst)

print("----------1--------")


# 3、字典排序
dc = {2: "2", "12": '1', 3: "3", "": 1}


def consume_key(o1):
    c = None
    if isinstance(o1, int):
        c = str(o1)
    elif isinstance(o1, str):
        if len(o1) >= 1:
            if len(o1) == 1:
                c = o1
            else:
                c = o1[0]
    if c is None:
        return -1
    return ord(c)


lst = sorted(dc, key=consume_key)  # 排序规则: consume_key(key1) < consume_key(key2)
print(lst)  # ['', '12', 2, 3]

print("----------2--------")


