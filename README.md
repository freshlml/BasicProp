# 虚拟环境
### 通过venv创建虚拟环境
* 需要python3.4版本以上？
* 原理: 创建venv环境目录，并将相关目录写入项目的sys.path路径
##### 使用标准库python运行
```shell script
$ D:\pyProjects\BasicProp\basic\chapter5> python test.py
'D:\\pyProjects\\BasicProp\\basic\\chapter5',                                     # top_level package
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',      # python标准库路径  (取自环境变量指向路径)
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',              # python标准库Dll路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib',               # python标准库lib路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37',                    # python标准库路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages' # python标准库site-packages路径
sys.prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
!!!不会自动关联venv环境
```
##### 在pycharm中运行
```shell script
'D:\\pyProjects\\BasicProp\\basic\\chapter5',                                     # top_level package
'D:\\pyProjects\\BasicProp',                                                      # 项目目录
...pycharm的目录
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',      # python标准库路径  (取自pyvenv.cfg的name)
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',              # python标准库Dll路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib',               # python标准库lib路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37',                    # python标准库路径
'D:\\pyProjects\\BasicProp\\venv'                                                 # venv目录
'D:\\pyProjects\\BasicProp\\venv\\lib\\site-packages'                             # venv的site-packages路径
...pycharm的目录
sys.prefix = D:\pyProjects\BasicProp\venv
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.exec_prefix = D:\pyProjects\BasicProp\venv
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
!!!关联了venv环境
```
##### 使用虚拟环境的python运行
```shell script
(venv) D:\pyProjects\BasicProp\venv\Scripts>python ../../basic/chapter5/test.py
'D:\\pyProjects\\BasicProp\\basic\\chapter5',                                     # top_level package
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip',      # python标准库路径  (取自pyvenv.cfg的name)
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\DLLs',              # python标准库Dll路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37\\lib',               # python标准库lib路径
'C:\\Users\\DELL\\AppData\\Local\\Programs\\Python\\Python37',                    # python标准库路径
'D:\\pyProjects\\BasicProp\\venv'                                                 # venv目录
'D:\\pyProjects\\BasicProp\\venv\\lib\\site-packages'                             # venv的site-packages路径
sys.prefix = D:\pyProjects\BasicProp\venv
sys.base_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
sys.exec_prefix = D:\pyProjects\BasicProp\venv
sys.base_exec_prefix = C:\Users\DELL\AppData\Local\Programs\Python\Python37
!!!关联了venv环境
```


### venv实例
##### 1.系统上可安装多个版本python
&nbsp;&nbsp;环境变量一次只能指向一个版本的python安装路径

##### 2.创建venv环境
```
projectDir$ python -m venv my_env       # 在projectDir目录下创建my_env目录(如果不存在)
  python解释器,pip工具拷贝一份放到Scripts目录，
  Lib/site-packages目录中默认写入pip，setuptools，后续安装的第三方依赖放置在此目录
  并没有将标准库的模块,dll,头文件复制到my_env中，而是在pyvenv.cfg文件通过name指向当前标准库路径
my_env
  -Include
  -Lib
    -site-packages
  -Scripts
  pyvenv.cfg

切换python版本(还是说只能升级): todo，待验证
  1.修改环境变量指向目标python版本（需要已在机器上安装）
  2.python -m venv my_env --upgrade

note: python -m venv -h 查看命令帮助
```


##### 3.激活 (进入虚拟环境)
```shell script
projectDir$                          cd my_env/Scripts/      # 进入Scripts目录
projectDir/my_env/Scripts$           activate                # 执行activate脚本
(my_env) projectDir/my_env/Scripts$                          # 可以看到，命令提示符切换到了my_env环境
(my_env) projectDir/my_env/Scripts$  python -V               # 打印my_env环境的python版本
Python 3.7.3
```


##### 4.退出虚拟环境
```shell script
(my_env) projectDir/my_env/Scripts$  deactivate     # 执行deactivate脚本
projectDir/my_env/Scripts$                          # 可以看到，退出了虚拟环境

```


##### 5.第三方依赖的管理
```
(my_env) projectDir/my_env/Scripts$ pip install 依赖名称==版本号      # 在my_env环境安装特定版本的依赖 (python -m pip install ...这条命令会搜索到标准库的pip?是否存在歧义呢?)
(my_env) projectDir/my_env/Scripts$ pip install --upgrade 依赖名称   # 更新到最新版
(my_env) projectDir/my_env/Scripts$ pip uninstall 依赖名称s          # 卸载
(my_env) projectDir/my_env/Scripts$ pip show 依赖名称                # 查看
(my_env) projectDir/my_env/Scripts$ pip list                        # 列出已安装的

pip install requests时，requests依赖的包也安装了，todo,requests的依赖关系如何维护
当依赖相互缠绕时，警惕可能出现的依赖版本冲突问题？
```


##### 6.第三方依赖的协同
```
多个开发环境的协同，开发环境和线上环境的协同
原理: 每一个开发环境和线上环境都创建本地的venv。1.pyvenv.cfg中name指向相同的python版本；2.通过依赖文件协同第三方依赖

(my_env) projectDir/my_env/Scripts$ pip freeze > ../../requirements.txt       # 将依赖信息写到文件
                                                                                        # 将文件提交给git
(my_env) projectDir/my_env/Scripts$ pip install -r ../../requirements.txt     # 安装文件中的依赖

```


# python解析器
python解析器
### python -m命令语法
```shell script
# 1.将当前工作目录添加到sys.path
# 2.在sys.path中搜索
D:\pyProjects\BasicProp\basic> python -m package_name/module_name

# 搜索package, 运行package下__main__.py
D:\pyProjects\BasicProp\basic> python -m package_name

# 搜索module, 以__main__运行
D:\pyProjects\BasicProp\basic> python -m module_name

# 搜索module, 以__main__运行
D:\pyProjects\BasicProp\basic> python -m package.module
```
### python <script>
```shell script
# 1.py文件路径可以是绝对路径，或者相对路径，相对于当前工作目录
# 2.将py文件所在目录的绝对路径添加到sys.path
D:\pyProjects\BasicProp\basic> python ./chapter5/test.py

# 1.package路径可以是绝对路径，或者相对路径，相对于当前工作目录
# 2.执行package下__main__.py, 将./basic/chapter5添加到sys.path
D:\pyProjects\BasicProp> python ./basic/chapter5

```

