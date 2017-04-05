import json

info = {
    "name":"okoko",
    "age":20
}

# print(json.dumps(info))

with open("1.txt",'r+') as f:
    content = f.read()
    dict_a = json.loads(content)
    print(dict_a['a'])


