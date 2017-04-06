#coding:utf-8

def foo():
    print('in foo()')
    bar()


def bar():
    print('in bar()')


foo()


# python程序的执行是自上而下的顺序执行的

# 函数体在内存就是普通的字符串
# 函数名引用函数体
