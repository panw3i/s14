class Animail(object):
    def talk(self):
        pass

    @staticmethod
    def animal_talk(obj):
        obj.talk()




class Dog(Animail):
    def talk(self):
        print("狗在叫")



class Cat(Animail):
    def talk(self):
        print("猫在叫")


a = Dog()
b = Cat()

Animail.animal_talk(b)
a.animal_talk(a)


'''     类  属性  实例变量 类变量
            方法
            构造方法
            析构函数 
            
        
        对象  实例化一个类之后得到的对象

        封装 把一些功能的实现细节不对外暴露
        
        继承 代码的重用  新式类在多继承中使用广度查找,初始化函数只会执行一次
        
        多态 接口重用,一种接口,多种实现
        
        




'''