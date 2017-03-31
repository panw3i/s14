def foo_1():
    print(" in the test ")
    pass        # 默认返回None


def foo_2():
    return 1   # 返回后中止当前函数的运行

    print("test foo_1")


def foo_3():
    return 1 , 2 , "fff"  # 返回一个值,元组

print(foo_1())
print(foo_2())
print(foo_3())


'''
返回值数=0 ,返回值为None
返回值数=1,返回址为Object
返回值数>1,返回值为Tuple

'''



def test(x,y):
    print(x)
    print(y)

test(1,2)   # 与形参一一对应
test(y=1,x=2)  # 关键字参数顺序无关


# 关键字参数一定在要位置参数后面







