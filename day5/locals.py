def foo():
    local_var  =333
    print('local():%s'%locals())


foo()
print(globals())
