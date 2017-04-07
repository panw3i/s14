class Dog(object):

    def __init__(self,name):
        self.name = name

    @staticmethod
    def eat(obj):
        print('%s is eating'%obj.name)


d = Dog("po")
Dog.eat(d)



'''
staticmethod 静态方法只是普通的函数,和类没有实质的关系
相当于是类命名空间下的调用一个普通的函数
或者就叫作 类的工作包

'''