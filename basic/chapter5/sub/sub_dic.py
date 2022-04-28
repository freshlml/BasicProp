import sys

# 被__main__依赖的module之间相互可以使用绝对导入，更深层目录可以使用相对导入
# from .. import current_dic  #ValueError: attempted relative import beyond top-level package(指__main__所在目录)
import current_dic

print("sub_dic", sys.path, sep=": ", end="\n")
print("sub_dic", current_dic, sep=": ", end="\n")
