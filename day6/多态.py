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