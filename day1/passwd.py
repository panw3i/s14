import getpass

name = input("username:"+"\n")
# passwd = input("password:"+"\n")


# 密码显示为密文
passwd = getpass.getpass("password:")
print(name,passwd)