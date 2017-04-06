class School(object):
    def __init__(self,name,addr):
        self.name = name
        self.addr = addr
        self.students = []
        self.teachers = []

    def enroll(self,stu_obj):
        print("为学员%s办理注册手续"%stu_obj.name)
        self.students.append(stu_obj)


    def hire(self,staff_obj):
        print("雇佣了新员工%s"%staff_obj)
        self.teachers.append(staff_obj)



class People(object):
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex  =sex

    def tell(self):
        pass


class Teacher(People):
    def __init__(self,name,age,sex,course):
        super(Teacher,self).__init__(name,age,sex)
        self.course = course

    def tell(self):
        pass




class Student(People):
    def __init__(self,name,age,sex,stu_id,grade):
        super(Student, self).__init__(name,age,sex)
        self.stu_id = stu_id
        self.grade = grade

    def tell(self):
        pass




