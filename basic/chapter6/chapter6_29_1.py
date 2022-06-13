class Lst:

    def __init__(self, lss):
        self.lss = lss

    def __getitem__(self, item):
        # 分片取值代码逻辑
        if type(item) == slice:
            ''' 拉和翻转逻辑
            s = self.start
            if s < -self.lss:
                s = -self.lss
            if s < 0:
                s = s + self.lss    
            if s > self.lss:
                s = self.lss
            '''
            if item.start < 0:
                s = item.start + self.lss
                if s < 0:
                    s = 0
            elif item.start <= self.lss:
                s = item.start
            else:
                s = self.lss

            if item.stop < 0:
                e = item.stop + self.lss
                if e < 0:
                    e = 0
            elif item.stop <= self.lss:
                e = item.stop
            else:
                e = self.lss

            if s >= e:
                return "取不到"
            return s, e
        else:
            # 索引取值，判断下标是否超界
            if item < -self.lss or item >= self.lss:
                raise Exception("index out of range")
            return item

    def __setitem__(self, key, value):
        # 分片赋值代码逻辑
        if type(key) == slice:
            if key.start < 0:
                s = key.start + self.lss
                if s < 0:
                    s = 0
            elif key.start <= self.lss:
                s = key.start
            else:
                s = self.lss

            if key.stop < 0:
                e = key.stop + self.lss
                if e < 0:
                    e = 0
            elif key.stop <= self.lss:
                e = key.stop
            else:
                e = self.lss

            if s >= e:
                print(s, " insert", sep="", end="\n")
            else:
                print("[", s, ",", e, ")", " iterable(", value, ")", sep="", end="\n")
        else:
            # 索引赋值，判断下标是否超界
            if key < -self.lss or key >= self.lss:
                raise Exception("index out of range")
            # key下标替换成value
            print("[", key, "]=", value, sep="", end="\n")


lst = Lst(5)
# 索引取值
print(lst[1])  # 1
# print(lst[100])  # Exception: index out of range
# print(lst[-100])  # Exception: index out of range
# 索引赋值
lst[1] = 1  # [1]=1
# lst[100] = 1  # Exception: index out of range

print("----------------1---------------------")

# 分片取值
print(lst[-10:-8])  # 取不到, [0:0]
print(lst[-5:-8])  # 取不到,  [0:0]
print(lst[-2:-8])  # 取不到,  [3:0]
print(lst[0:-8])  # 取不到,   [0:0]
print(lst[3:-8])  # 取不到,   [3:0]
print(lst[5:-8])  # 取不到,   [5:3]
print(lst[7:-8])  # 取不到,   [5:3]
print(lst[7:-5])  # 取不到,   [5:0]

print(lst[-6:-2])  # (0, 3), [0:3]
print(lst[-5:-2])  # (0, 3), [0:3]
print(lst[-2:-2])  # 取不到, [3:3]
print(lst[-4:-2])  # (1, 3), [1:3]
print(lst[0:-2])  # (0, 3),  [0:3]
print(lst[1:-2])  # (1, 3),  [1:3]
print(lst[3:-2])  # 取不到,  [3:3]
print(lst[5:-2])  # 取不到,  [5:3]
print(lst[6:-2])  # 取不到,  [5:3]

print(lst[1:0])  # 取不到, [1:0]

print(lst[-6:3])  # (0, 3), [0:3]
print(lst[-5:3])  # (0, 3), [0:3]
print(lst[-1:3])  # 取不到, [4:3]
print(lst[-4:3])  # (1, 3), [1:3]
print(lst[0:3])  # (0, 3),  [0:3]
print(lst[1:3])  # (1, 3),  [1:3]
print(lst[3:3])  # 取不到,  [3:3]
print(lst[5:3])  # 取不到,  [5:3]
print(lst[6:3])  # 取不到,  [5:3]

print(lst[-6:7])  # (0, 5), [0:5]
print(lst[-5:7])  # (0, 5), [0:5]
print(lst[-1:7])  # (4, 5), [4:5]
print(lst[-4:7])  # (1, 5), [1:5]
print(lst[0:7])  # (0, 5),  [0:5]
print(lst[1:7])  # (1, 5),  [1:5]
print(lst[6:7])  # 取不到,  [5:5]
print(lst[7:7])  # 取不到,  [5:5]

print("----------------2---------------------")

# 分片赋值
lst[-9:-8] = "9"  # 0 insert, [0:0]
lst[-5:-8] = "4"  # 0 insert, [0:0]
lst[1:-8] = "1"  # 1 insert,  [1:0]
lst[0:-8] = "6"  # 0 insert,  [0:0]
lst[5:-8] = "6"  # 5 insert,  [5:0]

lst[-9:-4] = "6"  # [0,1) iterable(6), [0:1]
lst[-5:-4] = "6"  # [0,1) iterable(6), [0:1]
lst[1:-4] = "6"  # 1 insert,  [1:1]
lst[0:-4] = "6"  # [0,1) iterable(6),  [0:1]
lst[5:-4] = "6"  # 5 insert,  [5:1]
lst[6:-4] = "6"  # 5 insert,  [5:1]

lst[-9:0] = "6"  # 0 insert, [0:0]
lst[-5:0] = "6"  # 0 insert, [0:0]

lst[-9:5] = "6"  # [0,5) iterable(6), [0:5]
lst[-5:5] = "6"  # [0,5) iterable(6), [0:5]
lst[0:6] = "6"  # [0,5) iterable(6),  [0:5]
lst[5:6] = "6"  # 5 insert,  [5:5]
lst[7:6] = "6"  # 5 insert,  [5:5]

