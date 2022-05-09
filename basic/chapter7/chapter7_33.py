

# else子句, 没有异常时执行(与except互斥)，注意else先于finally（怪）
def e1(*param):
    print("e1执行")
    try:
        i = param[1] / param[0]
    except IndexError as ee1:
        print("e1处理异常", ee1)
    except Exception as re:
        print("e1处理异常", re)
    else:
        print("没有发生异常", i)
    finally:
        print("finally执行")

    print("继续执行")


# e1执行
# 没有发生异常 1.0
# finally执行
# 继续执行
e1(1, 1)


def e2(*param):
    print("e2执行")
    try:
        f = None
        f = open("nothing", "r", encoding="utf-8")
    except Exception as re:
        print(type(re))
        print("e2处理异常", re)
    finally:
        if f:
            print(f)
            f.close()

    print("继续执行")


# e2执行
# <class 'FileNotFoundError'>
# e2处理异常 [Errno 2] No such file or directory: 'nothing'
# 继续执行
e2()


# raise from语法
def e3():
    1/0


def e4():
    try:
        e3()
    except Exception as ee:
        print(ee)  # division by zero
        raise Exception("e4异常") from ee


try:
    e4()
except Exception as mee:
    print(mee)  # e4异常
    print(mee.__cause__)  # division by zero

# print(mee)  # NameError: name 'mee' is not defined


# 异常中的局部域
def e5():
    try:
        e5_try = "e5_try"
        1/0
    except Exception as e5_e:
        e5_ex = "e5_ex"
    else:
        e5_el = "e5_el"
    finally:
        e5_fl = "e5_fl"

    print(e5_try)  # e5_try
    # print(e5_e)  # UnboundLocalError: local variable 'e5_e' referenced before assignment
    # print(e5_ex) # e5_ex
    # print(e5_el)  # e5_el
    print(e5_fl)  # e5_fl


# 仅e5_e是局部域
e5()

