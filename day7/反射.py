
def bulk(self):

    print("bulking......... ")

class Dog(object):
    pass

d = Dog()

if hasattr(d,"eat"):
    print(" eating")
    f = getattr(d,'eat')
    f("gou")

else:
    setattr(d,"op",bulk)
    d.op("oo")


    '''
    
    给实例动态的装载属性和方法
    属性和方法都是通过字符串来来给实例绑定属性和方法
    
    
    hasattr(obj,name_str)
    getattr(obj,name_str)
    setattr(obj,'y',z)    方法在类的外部
    delattr(obj,name_str)
    
    
    '''