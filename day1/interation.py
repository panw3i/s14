
# python2.x raw_input
# 3.x input

name = input("请输入你的姓名!")
age = input("年龄:")
job = input("工作:")
salary = input("工资:")


info = '''

-------- info of {_name} ----------

Name = {_name}
Age = {_age}
Job = {_job}
Salary = {_salary}


'''.format(_name=name,
           _age=age,
           _job=job,
           _salary=salary)


print(info)