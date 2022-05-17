

class ArgCheckDefException(Exception):
    pass


class ArgCheckException(Exception):

    def __init__(self, start, end, p, v, *args):
        self.start = start
        self.end = end
        self.p = p
        self.v = v
        Exception.__init__(self, *args)

    def __str__(self):
        return Exception.__str__(self) + ": [" + str(self.start) + ", " + str(self.end) + "], " + str(self.p) + "=" + str(self.v)


def ArgCheck(**kargs):
    class Decorator(object):
        def __init__(self, original):
            self.original = original
            code = original.__code__
            self.def_all_arg = list(code.co_varnames)
            self.def_pos_arg = list(code.co_varnames[:code.co_argcount])

        @staticmethod
        def check(param_name, param, start, end):
            try:
                # print(11.9999999999999 == 11.9999999999998999994)  # True, 浮点数运算本身问题
                if param < end and param >= start:
                    return
            except Exception as e:
                raise e

            raise ArgCheckException(start, end, param_name, param, "参数范围不合法")

        def __call__(self, *args, **kwargs):
            pos_param_tag = True
            key_param_tag = True
            for (arg_name, (start, end, *remain)) in Decorator.kwargs.items():
                if remain and len(remain) > 0 and remain[0] == '*' and pos_param_tag:
                    try:
                        args_i = self.def_pos_arg.index(remain[1])
                    except ValueError as e:
                        raise ArgCheckDefException("*定义错误: args=(-100, 100, '*', 'pos')")
                    else:
                        args_i = args_i + 1
                        while args_i < len(args):
                            Decorator.check("position[" + str(args_i) + "]", args[args_i], start, end)
                            args_i = args_i + 1
                    pos_param_tag = False
                elif remain and len(remain) > 0 and remain[0] == '**' and key_param_tag:
                    for (key_name, param_value) in kwargs.items():
                        try:
                            pt = key_name in remain[1]
                        except Exception as e:
                            raise ArgCheckDefException("**定义错误: kwargs=(-100, 100, '**', ('args', 'kwargs')")
                        if pt or key_name not in self.def_all_arg or self.def_all_arg.index(key_name) >= remain[2]:
                            Decorator.check(key_name, param_value, start, end)
                    key_param_tag = False
                elif arg_name in kwargs:
                    Decorator.check(arg_name, kwargs[arg_name], start, end)
                elif arg_name in self.def_pos_arg:
                    Decorator.check(arg_name, args[self.def_pos_arg.index(arg_name)], start, end)
                else:
                    raise ArgCheckDefException("ArgCheck定义异常")

    Decorator.kwargs = kargs
    return Decorator


@ArgCheck(a=(-100, 100), b=(-100, 100), c=(-100, 100), d=(-100, 100), args=(-100, 100, '*', 'b'), kwargs=(-100, 100, '**', ('args', 'kwargs'), 6))
def m1(a, b, *args, c, d, **kwargs):
    lp = "lp"
    pass


m1(0, 0, 0, 0, c=0, d=5, args=6, kwargs=0, ke=0, lp=100000)
m1(0, 0, c=0, d=5, args=6, kwargs=0, ke=0)


@ArgCheck(a=(-10, 10), b=(-10, 10))
def m2(a, b):
    pass


m2(1, 2)
m2(1, b=2)
m2(b=2, a=1)
print("--------------")


# 函数参数分析
def md(a, b, *args, c, d, **kwargs):
    pass


# 1.反射/内省
md_code = md.__code__
print(md_code.co_varnames)  # ('a', 'b', 'c', 'd', 'args', 'kwargs'),可以得到参数名称, args，kwargs没有特别的标记不能通过args得到函数定义中的该参数的下标
print(md_code.co_varnames[:md_code.co_argcount])  # ('a', 'b'), 仅得到位置参数

# 2.函数调用传参分析
#   __call__(*args, **kwargs)
#
#   md中c,d只能是保存在kwargs中，kwargs['c']取值
#   md中a,b要么在kwargs中或者args中, kwargs['c']取值 或者 i = md.__code__.co_varnames[:md_code.co_argcount].index('a'), args[i]
#   md中args: 需要知道剩余的位置参数的开始下标
#   md中kwargs: kwargs中的关键字参数, not in md.__code__.co_varnames || == md中定义的'args' || == md中定义的'kwargs'
md(0, 1, 2, 3, c='c', d='d', args="args", kwargs='kwargs')




