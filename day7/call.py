class A(object):
    n = 1

    def __init__(self,m):
        self.m = m

    def __call__(self, *args, **kwargs):
        print(*args)

    def foo(self):
        print('in the foo')

    def __str__(self):
        return self.m




a = A('tt')
a('lll')
a.ll = ";;"
print(A.__dict__) # 打印类的所有属性和方法
print(a.__dict__)  # 打类实例的所有属性
print(a.n)
print(a)

# 类中的特殊方法就是通过不同调用方式来执行,而且类和实例在调用这些特殊方法时返回的结果可能是不一样的