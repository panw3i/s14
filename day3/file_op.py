f = open("1.txt", "w+")

print(f.tell())
print(f.readline())
print(f.tell())
f.seek(0)

print(f.encoding)
print("fileno%s"%f.fileno())
print(f.name)

f.write("h")
f.flush()

