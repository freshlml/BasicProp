

# 函数，方法装饰器
class Decorator(object):
    def __init__(self, original):
        self.original = original

    def __call__(self, *args):
        print("Decorator before")
        try:
            instance = self.instance
        except AttributeError:
            rr = self.original(*args)
        else:
            rr = self.original(instance, *args)
        print("Decorator after")
        return rr

    def __get__(self, instance, owner):
        if instance is None:
            try:
                del self.instance
            except AttributeError:
                pass
        else:
            self.instance = instance
        return self


@Decorator
def mm(*params):  # 1.def执行: mm=class function, 2.@Decorator执行: mm = Decorator(mm)
    return params


print(type(mm))  # class Decorator
r = mm("11", "22")  # 1.mm("11", "22")， 2.Decorator.__call__(mm, "11", "22")，3.mm("11", "22")
print(r)  # ('11', '22')


class A(object):

    @Decorator
    def m(self, *params):    # 1.def执行:m = class function，2.@Decorator执行: m = Decorator(m)
        return params


a = A()
print(type(a))  # class A
print(type(A.m))  # class Decorator
print(type(a.m))  # class Decorator
print(A.m is a.m)  # True
print(a.m.original)  # class A def m

# 1.A.m(a, "pp1", "pp2"), 2.__get__触发，3.Decorator.__call__(m, a, "pp1", "pp2"), 4.A.m(a, "pp1", "pp2")
print(A.m(a, "pp1", "pp2"))  # ('pp1', 'pp2')
# 1.a.m("params"), 2.__get__触发，设置instance=a, 3.Decorator.__call__(m, "params"), 3.A.m(a, "params")
print(a.m("params"))  # ('params',)


print("-----1---------")


def f1():
    def f2():
        pass
    return f2


print(f1() is f1())  # False, 函数每次运行都是一个局部域


# 使用嵌套函数实现 函数，方法装饰器
def funcDecorator(original):
    def funcDecoratorImpl(*params):
        print("funcDecorator before")
        rrr = funcDecoratorImpl.__dict__['original'](*params)
        print("funcDecorator after")
        return rrr

    funcDecoratorImpl.__dict__['original'] = original
    return funcDecoratorImpl


class AA(object):

    @funcDecorator
    def m(self, *params):  # 1.def执行:m = class function，2.@funcDecorator执行: m = funcDecorator(m)
        return params


aa = AA()
print(aa.m)  # funcDecoratorImpl
# 1.aa.m('oo1', 'oo2'); 2.funcDecoratorImpl(aa, 'oo1', 'oo2'); 3.AA.m(aa, 'oo1', 'oo2')
print(aa.m("oo1", "oo2"))  # ('oo1', 'oo2')

print("-------1.1------")


# 类装饰器
class ClzDecorator(object):

    def __init__(self, original):
        self.original = original

    def __call__(self, *args):
        print("ClzDecorator before")
        print(self)  # Dec object
        print("ClzDecorator after")
        return self.original(*args)


@ClzDecorator
class B(object):    # 1.class执行:B = class type，2.@ClzDecorator执行:B = ClzDecorator(B)

    def __init__(self, *param):
        self.param = param

    def mm(self):
        return self.param


print(type(B))  # class ClzDecorator
print(B.original)  # B,class type
b = B("参数1", "参数2")  # 触发ClzDecorator.__call__
print(type(b))  # class B
print(b.mm())  # ('参数1', '参数2')


# python中装饰器 ===  Java中动态代理和Aop
'''
def Transactional(original):
    def Decorator(*params):
        print("@Transactional 前置执行");
        ret = Decorator.original(*params);
        print("@Transactional 后置执行");
    
    Decorator.original = original
    return Decorator
    
class A:
    @Transactional
    def m1(self):
        print("A m1")
    
    @Annotation2
    def m2(self):
        print("A m2")


    
interface I {
    void m1();
    void m2();
}
class A implements I {
    @Transactional
    void m1() {System.out.println("A m1");}
    @Annotation2
    void m2() {System.out.println("A m2");}
}
A a = new A();
I a_proxy = (I) Proxy.newProxyInstance(A.class.getClassLoader(), new Class[]{I.class}, new Ivh(a));

System.out.println(I.class.getMethod("m1"));  //public abstract void org.example.pr.I.m1()
System.out.println(A.class.getMethod("m1")); //public void org.example.pr.A.m1()
System.out.println(a_proxy.getClass()); //class com.sun.proxy.$Proxy0
System.out.println(a_proxy.getClass().getMethod("m1")); //public final void com.sun.proxy.$Proxy0.m1()

a_proxy.m1();
a_proxy.m2();

class Ivh implements InvocationHandler {
    private I target;  //被代理对象
    public Ivh(I target) {
        this.target = target;
    }

    @Override
    public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
        //proxy: 代理对象，即a_proxy

        //public abstract void org.example.pr.I.m1()
        //public abstract void org.example.pr.I.m2()
        //因为I a_proxy = Proxy...
        System.out.println(method);

        Method p_m = proxy.getClass().getMethod(method.getName());
        //public final void com.sun.proxy.$Proxy0.m1()
        //public final void com.sun.proxy.$Proxy0.m2()
        System.out.println(p_m);
        Method a_m = target.getClass().getMethod(method.getName());
        //public void org.example.pr.A.m1()
        //public void org.example.pr.A.m2()
        System.out.println(a_m);

        //null
        System.out.println(method.getAnnotation(Transactional.class));
        //null
        System.out.println(method.getAnnotation(Annotation2.class));
        //null
        System.out.println(p_m.getAnnotation(Annotation2.class));
        //null
        System.out.println(p_m.getAnnotation(Annotation2.class));

        Object ret = null;
        Transactional t = a_m.getAnnotation(Transactional.class);
        if(t != null) {
            System.out.println("@Transactional 前置执行");
            ret = method.invoke(target, args);
            System.out.println("@Transactional 后置执行");
        }
        Annotation2 at = a_m.getAnnotation(Annotation2.class);
        if(at != null) {
            System.out.println("@Annotation2 前置执行");
            ret = method.invoke(target, args);
            System.out.println("@Annotation2 后置执行");
        }

        return ret;
    }
}


'''








