class Lst:

    def __init__(self, lss):
        self.lss = lss

    def __getitem__(self, item):
        # 分片取值代码逻辑
        if type(item) == slice:
            if item.start >= self.lss:
                return "取不到"
            elif item.start >= 0:
                s = item.start
            elif item.start >= -self.lss:
                s = item.start + self.lss
            else:
                s = 0

            if item.stop <= -self.lss:
                return "取不到"
            elif item.stop < 0:
                e = item.stop + self.lss
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


lst = Lst(5)
print(lst[0])  # 0
# print(c[-6])  # Exception: index out of range
# print(c[5])  # Exception: index out of range

# 分片取值逻辑测试，@link chapter2.py#分片取值逻辑测试
print(lst[-9:-8])  # [], 取不到: stop=-8<=-5
print(lst[-7:-8])  # [], 取不到: stop=-8<=-5
print(lst[-3:-8])  # [], 取不到: stop=-8<=-5
print(lst[2:-8])   # [], 取不到: stop=-8<=-5
print(lst[5:-8])   # [], 取不到: stop=-8<=-5
print(lst[-5:-5])  # [], 取不到: stop=-8<=-5

print(lst[-6:-4])  # [1], [0,1)
print(lst[-5:-4])  # [1], [0,1)
print(lst[-3:-4])  # [], [2,1) 取不到
print(lst[2:-4])   # [], [2,1) 取不到
print(lst[5:-4])   # [], 取不到: start=5>=5
print(lst[6:-5])  # [], 取不到: start=6>=5

print(lst[-9:0])  # [], [0,0) 取不到
print(lst[-5:0])  # [], [0,0) 取不到
print(lst[-4:0])  # [], [1,0) 取不到
print(lst[-9:1])  # [1], [0,1)
print(lst[-5:1])  # [1], [0,1)
print(lst[-4:1])  # [], [1,1) 取不到
print(lst[-3:1])  # [], [2,1) 取不到
print(lst[2:1])  # [], [2,1) 取不到

print(lst[-9:5])  # [1, 2, 3, 4, 5], [0,5)
print(lst[-4:5])  # [2, 3, 4, 5], [1,5)
print(lst[1:5])   # [2, 3, 4, 5], [1,5)


print(lst[5:6])   # [], 取不到: start=5>=5
print(lst[6:6])   # [], 取不到: start=6>=5
print(lst[5:-6])  # [], 取不到: start=5>=5
print(lst[5:-5])  # [], 取不到: start=5>=5
print(lst[5:-2])  # [], 取不到: start=5>=5
print(lst[5:0])  # [], 取不到: start=5>=5
print(lst[5:5])  # [], 取不到: start=5>=5
print(lst[5:6])  # [], 取不到: start=5>=5

print(lst[1:6])  # [2, 3, 4, 5], [1,5)
print(lst[1:0])  # [], [1,0) 取不到
print(lst[1:-4])  # [], [1,1) 取不到
print(lst[1:-5])  # [], 取不到: stop=-5<=-5
print(lst[0:-4])  # [1], [0,1)

print(lst[-5:-4])  # [1], [0,1)
print(lst[-5:0])  # [], [0,0) 取不到
print(lst[-5:6])  # [1, 2, 3, 4, 5], [0,5)
print(lst[-4:-4])  # [], [1,1) 取不到
print(lst[-4:-3])  # [2], [1,2)
print(lst[-4:0])  # [], [1,0) 取不到
print(lst[-4:1])  # [], [1,1) 取不到
print(lst[-4:2])  # [2], [1,2)

print(lst[-6:-5])  # [], 取不到: stop=-5<=-5
print(lst[-6:-4])  # [1], [0,1)
print(lst[-6:0])  # [], [0,0) 取不到
print(lst[-6:1])  # [1], [0,1)
print(lst[-6:6])  # [1, 2, 3, 4, 5], [0,5)

print(lst[-3:-4])  # [], [2,1) 取不到
print(lst[-6:-6])  # [], 取不到: stop=-8<=-5
