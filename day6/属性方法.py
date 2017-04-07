class Dog(object):

    def __init__(self,name):
        self.name = name

    @property
    def eat(self):
        print('%s is eating'%self.name)

    @eat.setter
    def eat(self,name):
        print('%s is eating'%name)

    @eat.deleter
    def eat(self):
        del self.name


d = Dog("po")
#
# d.eat

# d.eat = "0000"  # AttributeError: can't set attribute

d.eat = "p00000"

del d.eat

# d.eat

'''
属性方法就是对内部具体实话进行封装,对外拍提供查询,修改,删除的接口
'''


print(Dog.__doc__)








