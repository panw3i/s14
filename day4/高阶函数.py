import time

'''
 a. 把一个函数名当做实参传给别外一个函数
 b. 返回值中包含函数名

'''

def bar():
    time.sleep(3)
    print('in the bar')


def t1(func):
    a = time.time()

    func()
    b = time.time()

    print(b-a)


t1(bar)



