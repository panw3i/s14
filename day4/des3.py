import time



def timer(func):
    def bar(*args,**kwargs):
        a = time.time()
        func(*args,**kwargs)
        b = time.time()
        print(b-a)
    return bar



@timer
def foo(name,age):
    print('%s in the foo %s'%(name,age))



foo(name="pan",age=56)