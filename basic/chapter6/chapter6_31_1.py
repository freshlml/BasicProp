

# 函数调用传参校验，@link chapter4_8
class ArgCheckException(Exception):
    pass


class ArgCheckRangeException(ArgCheckException):
    def __init__(self, start, end, n, v, *args):
        self.start = start
        self.end = end
        self.n = n
        self.v = v
        Exception.__init__(self, *args)

    def __str__(self):
        return Exception.__str__(self) + ": [" + str(self.start) + ", " + str(self.end) + "], " + str(self.n) + "=" + str(self.v)


class ArgCheckNoneException(ArgCheckException):
    def __init__(self, n, v, *args):
        self.n = n
        self.v = v
        Exception.__init__(self, *args)

    def __str__(self):
        return Exception.__str__(self) + ": " + str(self.n) + "=" + str(self.v)


class Check(object):
    pass


class RangeCheck(Check):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __call__(self, param_name, *param_values):
        self.param_name = param_name
        for value in param_values:
            self.check(value)

    def check(self, value):
        try:
            # print(11.9999999999999 == 11.9999999999998999994)  # True, 浮点数运算本身问题
            if value < self.end and value >= self.start:
                return
        except Exception as e:
            raise e

        raise ArgCheckRangeException(self.start, self.end, self.param_name, value, "参数范围不合法")


def NothingCheck():
    def check(param_name, *param_values):
        pass
    return check


def NoneCheck():
    def check(param_name, *param_values):
        for value in param_values:
            if value is None:
                raise ArgCheckNoneException(param_name, value, "参数不能为空")
    return check


def ArgCheck(*exclude, **regulars):
    def Decorator(original):
        code = original.__code__
        def_pos_args = code.co_varnames[:code.co_argcount]
        original_name = original.__name__

        def onCheck(*args, **kwargs):
            posChecker = None
            remaindKeysChecker = None
            not_contains = None
            for v in regulars.values():
                try:
                    if '*' in v:
                        posChecker = v[0]
                    elif '**' in v:
                        remaindKeysChecker = v[0]
                        not_contains = v[2]
                except Exception:
                    pass
            # check位置参数
            pos_i = 0
            for pos_param_value in args:
                if pos_i < len(def_pos_args):
                    pos_param_name = def_pos_args[pos_i]
                    try:
                        checker = regulars[pos_param_name]
                    except KeyError:
                        pass
                    else:
                        if checker is not None:
                            checker(pos_param_name, pos_param_value)
                    pos_i = pos_i + 1
                else:
                    if posChecker is not None:
                        posChecker(pos_param_name, pos_param_value)
            # check关键字参数
            for param_name, param_value in kwargs.items():
                if param_name in exclude:
                    try:
                        checker = regulars[param_name]
                    except KeyError:
                        pass
                    else:
                        if checker is not None:
                            checker(param_name, param_value)
                    continue
                elif len(exclude) > 0:
                    if remaindKeysChecker is not None:
                        remaindKeysChecker(param_name, param_value)
                    continue

                try:
                    checker = regulars[param_name]
                except KeyError:
                    checker = None
                if checker is None:
                    if remaindKeysChecker is not None:
                        if not_contains is None:
                            remaindKeysChecker(param_name, param_value)
                        elif param_name not in not_contains:
                            remaindKeysChecker(param_name, param_value)
                else:
                    try:
                        if '**' in checker or "*" in checker:
                            pass
                    except Exception:
                        checker(param_name, param_value)
                    else:
                        if remaindKeysChecker is not None:
                            remaindKeysChecker(param_name, param_value)

            return original(*args, **kwargs)

        onCheck.original = original
        return onCheck

    return Decorator


'''
@ArgCheck(a=RangeCheck(-100, 100),  # 每一个参数都定义，不校验的指定为NothingCheck(),不要设置为None
          f=NoneCheck(),
          ff=NothingCheck(),
          b=RangeCheck(-100, 100),
          c=RangeCheck(-100, 100),
          d=RangeCheck(-100, 100),
          e=NothingCheck(),
          ee=NothingCheck(),
          args=(RangeCheck(-100, 100), "*"),
          kwargs=(RangeCheck(-10, 10), '**'))
'''


'''
@ArgCheck('a', 'f', 'ff', 'b', 'c', 'd', 'ee',
          a=RangeCheck(-100, 100),  # 不校验的参数可以不定义，checker可以设置为None, 增加exclude参数
          f=NoneCheck(),
          # ff
          b=RangeCheck(-100, 100),
          c=RangeCheck(-100, 100),
          d=RangeCheck(-100, 100),
          e=NothingCheck(),
          # ee
          args=(RangeCheck(-100, 100), "*"),
          kwargs=(RangeCheck(-10, 10), '**'))
'''


@ArgCheck(a=RangeCheck(-100, 100),  # 不校验的参数如果不定义，则要将之放到**中，checker不要设置为None
          f=NoneCheck(),
          # ff
          b=RangeCheck(-100, 100),
          c=RangeCheck(-100, 100),
          d=RangeCheck(-100, 100),
          e=NothingCheck(),
          # ee
          args=(RangeCheck(-100, 100), "*"),
          kwargs=(RangeCheck(-10, 10), '**', ('ff', 'ee')))
def m1(a, f, ff, b=1000, *args, c=1000, d, e, ee, **kwargs):
    lp = "lp"
    print("m1 run...")


ori = m1.original
print(ori.__code__.co_varnames)  # ('a', 'f', 'ff', 'b', 'c', 'd', 'e', 'ee', 'args', 'kwargs', 'lp')
print(ori.__code__.co_varnames[:ori.__code__.co_argcount])  # ('a', 'f', 'ff', 'b')


m1(1, 1, 1000, 10, 1, 2, 3, 0, d=1, e=2, ee=-11, args=-10, kwargs=1, t=1)

