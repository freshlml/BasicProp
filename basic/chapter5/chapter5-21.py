import sys
# import
# 1. 如果该module已被import，不重复import
# 2. 搜索module,按"搜索路径"依次搜索
#    1).当前运行的module所在的目录；
#    2).PYTHONPATH环境环境变量定义的目录；
#    3).当前工作目录:python命令执行时目录(一般和1)相同，但也可以不同)；
#    4).python标准库目录；
#    5). .pth文件
# 3. 将module的源代码编译成字节码或者直接使用已存在的字节码
# 4. 执行module的字节码，生成class module对象，赋值给此中变量
import imported1
import imported2

# 打印"搜索路径"，TODO，一些目录需要认识
print(sys.path)

print(imported1.module_param)

# todo,disutils,venv









