import getpass

username = input("username:"+"\n")
# passwd = input("password:"+"\n")


# 密码显示为密文
passwd = getpass.getpass("password:")


_username = "pan"
_passwd = "123"

if _username == username and _passwd == passwd:
    print("Welcome {_name}".format(_name=username))
else:
    print("Invalid username or password")