names = ['pan', 'li', 'tan']

names.append("chao")
print(names)
print(names[0])
print(names[-2:-1])
# print(names[-1:-2]) 只能从左往右数

print(names[1:])
print(names[:3])
print(names.insert(1, 'man'))
print(names)

# add

names.extend(["ko", 'io'])
names.append("to")

# delete

names.remove("pan")
del names[0]
names.pop()
names.pop(1)

# index

names.index("ko")

# count

names.count("li")

# clear

names.clear()


print(names)
