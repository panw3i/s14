name = "   pa  nA     "

name.find("n")  # 2

detail = "{name} is  23".format(name="pan")

print(detail)
print(name.isalnum())
print(name.isalpha())
print(name.isdecimal())
print('10'.isdecimal()) #十进制
print('中a1A'.isidentifier()) #判断是否是合法的标识符
print(' a1A'.isidentifier()) #判断是否是合法的标识符
print('__________1A'.isidentifier()) #判断是否是合法的标识符
print('a'.islower())
print('Aa'.islower())
print('a'.isnumeric())
print('9.0'.isnumeric())
print('9'.isnumeric())
print('9f'.isnumeric())        #判断是否是纯数字
print(''.isspace())
print('   '.isspace())
print('MY'.istitle())
print('My Is'.istitle())
print("....".join(['1','2']))
print(name.ljust(50,"-"))
print(name.rjust(50,"*"))
print(name.lower())
print(name.upper())
print(name)
print(name.lstrip())
print(name.rstrip()+"kkkkkk")
print(name.strip())
print(name)
print("llio".replace("l","L",1))
print("--------------------")
print("lolio".rfind("o"))
print("lolio".find("o"))
print("1+2+3".split("+"))
print('li li'.title())
print('lll'.zfill(20))            #补零