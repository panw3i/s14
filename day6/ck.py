class Foo():
    n ="类变量"
    a_list = [1,2,3]
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def buy(self):
        self.__b = 90
        print("buy")

    def __del__(self):
        print("已死")

    def __t(self):
        print(self.__b)



r1  = Foo("pan",90)
r2  = Foo("li",89)
# r1.buy()
# del r1
# r2.buy()
# r1.n  = "修改类变量"
# r1.a_list.append([3,4])
# print(r1.n)
# print(r2.n)
# print(r2.a_list)

# 如果类属性是序列,作为实例的属性时,传入的是列表的地址

# 类变量的用途  作为公共属性使用


# 实例在内存中彻底的销毁的时候手动或者自动执行

# print(r1.__b)
r1.buy()
print(r1._Foo__t())