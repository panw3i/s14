import time

def timmer(func):
    def warpper(*args,**kwargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('use %s'%(stop_time - start_time))
    return warpper



@timmer
def t1():
    time.sleep(3)
    print('in t1')

t1()







