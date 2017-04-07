__author__ = "Alex Li"

def bulk(self):
    print("%s is yelling...." %self.name)

class Dog(object):
    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print("%s is eating..."%self.name,food)


d = Dog("NiuHanYang")


if hasattr(d,"eat"):
    getattr(d,"eat")
else:
    setattr(d,"op",bulk) #d.talk = bulk
    func = getattr(d, "op")
    func(d)