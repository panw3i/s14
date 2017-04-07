class Dog(object):

    age = 20

    @classmethod
    def eat(cls,new_age):
        age = new_age
        print(age)

d = Dog()

print('类方法修改前实例的类属性为:%s'%d.age)

Dog.eat(90)

print('类方法修改后类属性为:%s'%d.age)


'''
classmethod 只能访问类的属性

'''



