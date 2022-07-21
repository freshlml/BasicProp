import os
import sys
if "D:\\pyProjects\\BasicProp\\venv\\lib\\site-packages" not in sys.path:
    sys.path.append("D:\\pyProjects\\BasicProp\\venv\\lib\\site-packages")
import requests  # requests是一个package, import package,执行package的_init__.py

print(requests)
print(sys.path)

print(sys.prefix)
print(sys.base_prefix)
print(sys.exec_prefix)
print(sys.base_exec_prefix)

print("-----------------------------------------------")
# 相对路径: 相对于python命令执行时所在的目录（当前工作目录）
current_work_dir = os.getcwd()
print(os.getcwd())

# 切换到__file__ or sys.argv[0]目录
current_py_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_py_dir)
print(os.getcwd())

f = open("./sub/sub_dic.py", 'r', encoding="utf-8")
print(f.name)
f.close()

os.chdir(current_work_dir)
print(os.getcwd())
