

class People:

    def __init__(self,name,age):
        print("in the People")
        self.name = name
        self.age = age


    def eat(self):
        print('%s is eating ...'%self.name)

    def drink(self):
        print('%s is drinking .. '%self.name)




class Make_friend():
    def make(self,obj):
        print('%s make friend with %s'%(self.name,obj.name))

class Man(People,Make_friend):
    def __init__(self,name,age,work):
        super(Man,self).__init__(name,age)
        print(work)

    def foo(self):
        print('%s is fooing ....'%self.name)






class Woman(People):
    def bar(self):
        print("%s is baring...."%self.name)



m1 = Man("pan",90,'IT')
w1 = Woman("li",90)

m1.make(w1)
# m1.eat()
# m2 = Man()

# w1 = Woman("li",90,"IT")
# w1.bar()
# # w1.foo()






# python3 中经典类和新式类统一按广度优先的原则