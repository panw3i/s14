#coding:utf-8


class Dog:
    def __init__(self,name):
        self.name = name

    def bulk(self):
        print("%s: wang wang wang!" % self.name)


d1 = Dog("....")
d2 = Dog("00000")
d3 = Dog("陈老泡")

d1.bulk()
d2.bulk()
d3.bulk()

# class Dog:
#     def __int__(self,name):
#         self.name = name
#
#     def bulk(self):
#         print("%s : wang wang wange"%(self.name))
#
#
# d1 = Dog('pppp')


#
# d1.bulk()


