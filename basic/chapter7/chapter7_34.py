
# 异常基类BaseException,Exception
# Exception类中__init__(self, *args, *kwargs)
# BaseException类中__str__(self, *args, **kwargs)
# todo,内置异常类，内置异常类的继承结构


class Exp(Exception):

    def __init__(self, *args):
        Exception.__init__(self, *args)
        if args:
            self.one = args[0]

    def __str__(self):
        return Exception.__str__(self) + self.one


def e1():
    try:
        1/0
    except Exception as ex:
        raise Exp("参数", "错误") from ex


def e2():
    try:
        e1()
    except Exception as ex:
        print(ex.args)  # ('参数', '错误')
        print(ex.one)  # 参数
        print(ex)  # ('参数', '错误')参数
        print(ex.with_traceback(ex.__traceback__))
        tb = ex.__traceback__
        while tb:
            print(tb.tb_frame, tb.tb_lasti, tb.tb_lineno)
            tb = tb.tb_next


e2()




