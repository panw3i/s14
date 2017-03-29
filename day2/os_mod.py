import os


bash_result = os.system("ls")
print(bash_result)  # 返回结果为0 代表命令执行成功

bash_result = os.popen("ls").read()
print("------>",bash_result)


print(os.system('df'))
print(os.system('ls -al'))


os.mkdir("new_dir")