# 同时安装多个版本Python
多个版本Python分别对应各自的安装路径，使用每一个版本的Python解释器执行py文件，会将当前Python解释器的标准库路径写入sys.path。
注意: 不是将环境变量指向的Python版本的标准库路径写入sys.path
### 系统安装了两个版本python
C:\Users\DELL\AppData\Local\Programs\Python\Python37
```shell script
C:\Users\DELL\AppData\Local\Programs\Python\Python37> ls
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2021/9/16     15:41                DLLs
d-----         2021/9/16     15:41                Doc
d-----         2021/9/16     15:41                include
d-----         2021/9/16     15:41                Lib
d-----         2021/9/16     15:41                libs
d-----         2022/7/17     17:10                Scripts
d-----         2021/9/16     15:41                tcl
d-----         2021/9/16     15:41                Tools
-a----         2019/3/25     22:26          30195 LICENSE.txt
-a----         2019/3/25     22:26         665470 NEWS.txt
-a----         2019/3/25     22:23          99856 python.exe
-a----         2019/3/25     22:22          58896 python3.dll
-a----         2019/3/25     22:22        3748368 python37.dll
-a----         2019/3/25     22:23          98320 pythonw.exe
-a----         2019/3/25     21:22          89752 vcruntime140.dll
C:\Users\DELL\AppData\Local\Programs\Python\Python37> python -V  # 环境变量指向Python37
Python 3.7.3
C:\Users\DELL\AppData\Local\Programs\Python\Python37> pip -V     # 环境变量指向Python37
pip 19.0.3 from c:\users\dell\appdata\local\programs\python\python37\lib\site-packages\pip (python 3.7)
C:\Users\DELL\AppData\Local\Programs\Python\Python37> .\python.exe -V
Python 3.7.3
```
C:\Users\DELL\AppData\Local\Programs\Python\Python310
```shell script
C:\Users\DELL\AppData\Local\Programs\Python\Python310> ls
Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
d-----         2022/7/22      1:04                DLLs
d-----         2022/7/22      1:04                Doc
d-----         2022/7/22      1:04                include
d-----         2022/7/22      1:04                Lib
d-----         2022/7/22      1:04                libs
d-----         2022/7/22      1:04                Scripts
d-----         2022/7/22      1:04                tcl
d-----         2022/7/22      1:04                Tools
-a----          2022/6/6     16:24          32763 LICENSE.txt
-a----          2022/6/6     16:25        1261162 NEWS.txt
-a----          2022/6/6     16:24         100336 python.exe
-a----          2022/6/6     16:24          63472 python3.dll
-a----          2022/6/6     16:24        4450288 python310.dll
-a----          2022/6/6     16:24          98800 pythonw.exe
-a----          2022/6/6     16:24          98224 vcruntime140.dll
-a----          2022/6/6     16:24          37256 vcruntime140_1.dll
C:\Users\DELL\AppData\Local\Programs\Python\Python310> .\python.exe -V
Python 3.10.5
```
### 使用Python37解释器执行sys_path_test.py
```shell script
C:\Users\DELL\AppData\Local\Programs\Python\Python37> .\python.exe D:\pyProjects\BasicProp\basic\chapter5\sys_path_test.py
['D:\\pyProjects\\BasicProp\\basic\\chapter5',                                              # top_level_package(当前py文件所在目录)
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',                # 指向当前解释器的标准库路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages']
sys.prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37                           # 指向当前解释器的标准库路径
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
```
### 使用Python310解释器执行sys_path_test.py
```shell script
C:\Users\DELL\AppData\Local\Programs\Python\Python310> .\python.exe D:\pyProjects\BasicProp\basic\chapter5\sys_path_test.py
['D:\\pyProjects\\BasicProp\\basic\\chapter5',                                               # top_level_package(当前py文件所在目录)
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\python310.zip',               # 指向当前解释器的标准库路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\DLLs', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\lib', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310', 
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages']
sys.prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python310                            # 指向当前解释器的标准库路径
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python310
sys.exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python310
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python310
```

# 虚拟环境
### 通过venv创建虚拟环境
* 需要python3.4版本以上?
* 原理: 创建venv环境目录，并将相关目录写入项目的sys.path路径

### 使用标准库的Python解释器执行
```shell script
$ D:\pyProjects\BasicProp\basic\chapter5> python test.py
'D:\\pyProjects\\BasicProp\\basic\\chapter5',                                     # top_level package
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',      # 指向当前解释器的标准库路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',              
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib',               
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37',                    
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages' 
sys.prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37                 # 指向当前解释器的标准库路径
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
!!!不会自动关联venv环境
```
### 在pycharm中运行
```shell script
'D:\\pyProjects\\BasicProp\\basic\\chapter5',                                     # top_level package
'D:\\pyProjects\\BasicProp',                                                      # 项目目录
...pycharm的目录
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',      # 取自pyvenv.cfg的name
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',              
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib',               
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37',                    
'D:\\pyProjects\\BasicProp\\venv'                                                 # venv目录
'D:\\pyProjects\\BasicProp\\venv\\lib\\site-packages'                             # venv的site-packages路径
...pycharm的目录
sys.prefix = D:\pyProjects\BasicProp\venv                                         
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.exec_prefix = D:\pyProjects\BasicProp\venv
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
!!!关联了venv环境
```
### 使用虚拟环境的python解释器运行
```shell script
(venv) D:\pyProjects\BasicProp\venv\Scripts>python ../../basic/chapter5/test.py
'D:\\pyProjects\\BasicProp\\basic\\chapter5',                                     # top_level package
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',      # 取自pyvenv.cfg的name
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',              
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib',               
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37',                    
'D:\\pyProjects\\BasicProp\\venv'                                                 # venv目录
'D:\\pyProjects\\BasicProp\\venv\\lib\\site-packages'                             # venv的site-packages路径
sys.prefix = D:\pyProjects\BasicProp\venv
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.exec_prefix = D:\pyProjects\BasicProp\venv
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
!!!关联了venv环境
```


# venv实例

### 1.使用Python37解释器创建venv环境
```shell script
projectDir$ C:\Users\DELL\AppData\Local\Programs\Python\Python37\python.exe -m venv venv37
```
### 2.使用Python310解释器创建venv环境
```shell script
projectDir$ C:\Users\DELL\AppData\Local\Programs\Python\Python310\python.exe -m venv venv310
```
虚拟环境目录说明
```
my_env
  -Include
  -Lib
    -site-packages          # 写入pip，setuptools等模块，后续安装的第三方依赖放置在此目录
  -Scripts                  # 将当前python解释器,pip工具拷贝一份放到此目录
  pyvenv.cfg                # 将当前解释器的标准库路径通过name属性关联

虚拟环境标准库版本升级，第三方依赖被保留
    使用更高版本的python解释器: python -m venv my_env --upgrade
虚拟环境标准库版本回退
    删除，使用低版本的python解释器重新创建，第三方依赖如何保留？

note: python -m venv -h 查看命令帮助
```


### 3.激活 (进入虚拟环境)
```shell script
projectDir$                          cd my_env/Scripts/      # 进入Scripts目录
projectDir/my_env/Scripts$           activate                # 执行activate脚本
(my_env) projectDir/my_env/Scripts$                          # 可以看到，命令提示符切换到了my_env环境
(my_env) projectDir/my_env/Scripts$  python -V               # 打印my_env环境的python版本
Python 3.7.3
```


### 4.退出虚拟环境
```shell script
(my_env) projectDir/my_env/Scripts$  deactivate     # 执行deactivate脚本
projectDir/my_env/Scripts$                          # 可以看到，退出了虚拟环境

```


### 5.第三方依赖的管理
```
(my_env) projectDir/my_env/Scripts$ pip install 依赖名称==版本号      # 在my_env环境安装特定版本的依赖 (python -m pip install ...这条命令会搜索到标准库的pip?是否存在歧义呢?)
(my_env) projectDir/my_env/Scripts$ pip install --upgrade 依赖名称   # 更新到最新版
(my_env) projectDir/my_env/Scripts$ pip uninstall 依赖名称s          # 卸载
(my_env) projectDir/my_env/Scripts$ pip show 依赖名称                # 查看
(my_env) projectDir/my_env/Scripts$ pip list                        # 列出已安装的

pip install requests时，requests依赖的包也安装了，todo,requests的依赖关系如何维护
当依赖相互缠绕时，警惕可能出现的依赖版本冲突问题？
```


### 6.第三方依赖的协同
```
多个开发环境的协同，开发环境和线上环境的协同
原理: 每一个开发环境和线上环境都创建本地的venv。1.pyvenv.cfg中name指向相同的python版本；2.通过依赖文件协同第三方依赖

(my_env) projectDir/my_env/Scripts$ pip freeze > ../../requirements.txt       # 将依赖信息写到文件
                                                                              # 将文件提交给git
(my_env) projectDir/my_env/Scripts$ pip install -r ../../requirements.txt     # 安装文件中的依赖

```

