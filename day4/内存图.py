#coding:utf-8

def foo():
    print('in foo()')
    bar()


def bar():
    print('in bar()')


foo()


# 函数体在内存就是普通的字符串
# 函数名引用函数体
