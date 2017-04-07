class A():
    name = "pan"


class B():
    person = A()
    age = 30



b = B()

print(b.person.name)