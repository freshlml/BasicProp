

# 异常1: 捕获并处理异常
def e1(*param):
    print(type(param))
    try:
        i = param[0]/param[1]
        print("异常后不会执行，没有异常会执行")
    except Exception as e:
        print("处理异常", e)
    finally:
        print("finally执行")

    print("继续执行")

    return


# <class 'tuple'>
# 处理异常 division by zero
# finally执行
# 继续执行
e1(1, 0)
# <class 'tuple'>
# 异常后不会执行，没有异常会执行
# finally执行
# 继续执行
e1(1, 1)


# 异常2: 抛异常，向上层抛异常意味着这一层的结束
def e2(*param):
    print("e2开始执行")
    try:
        i = param[0] / param[1]
        print("e2,异常后不会执行，没有异常会执行")
    except Exception as e:
        print("e2处理异常", e)
        raise Exception("e2执行失败")
    finally:
        print("e2,finally执行")

    print("e2继续执行")

    return


def e3(*param):
    print("e3开始执行")
    try:
        e2(*param)
        print("e3,异常后不会执行，没有异常会执行")
    except Exception as e:
        print("e3处理异常", e)
    finally:
        print("e3,finally执行")

    print("e3继续执行")

    return


# e3开始执行
# e2开始执行
# e2处理异常 division by zero
# e2,finally执行
# e3处理异常 e2执行失败
# e3,finally执行
# e3继续执行
e3(1, 0)


# 异常3: 异常到达python解释器
def e4(*param):
    print("e4开始执行")
    e2(*param)
    print("e4继续执行")


# e4开始执行
# e2开始执行
# e2处理异常 division by zero
# e2,finally执行
# python解释器: ZeroDivisionError: division by zero
e4(1, 0)

print("not run...")
