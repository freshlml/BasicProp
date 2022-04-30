import sys
# 第五部分练习题
import chapter5_2

if len(sys.argv) == 2:
    chapter5_2.test(open(sys.argv[1], "r", encoding="utf-8"))
elif len(sys.argv) == 1:
    chapter5_2.test(open(sys.argv[0], "r", encoding="utf-8"))
else:
    chapter5_2.test(open("chapter5_1.py", "r", encoding="utf-8"))


