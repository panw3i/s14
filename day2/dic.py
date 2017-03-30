info = {"a":1,"b":2,"c":3}


print(info['a'])
info['a']=4

print(info)



#del

del info['a']
info.pop("b")
print(info)

print(info.get("a"))  #None



#info['a']  # keyError


{"a":1}.update({"b":1})

print(info.items())

c = dict.fromkeys([6,7,8],"test")
c = dict.fromkeys([6,7,8],[8,9,0])
print(c)


for i in info:
    print(i,info[i])

    
for k,v in info.items():
    print(k,v)