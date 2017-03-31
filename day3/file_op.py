f = open("1.txt", "wb+")

print(f.tell())
print(f.readline())
print(f.tell())
# print(f.encoding)
print("fileno%s"%f.fileno())
print(f.name)
#
f.read()
f.write("p".encode())
f.flush()

