import pickle
import json
info = {
    "name":"okoko",
    "age":20
}

json.dump(info,open('3.txt','r+'))

print(json.load(open("4.json",'r')))

# 可以加载外部文件
# load, dump
# 从外部JSON文件变成dict字典(外部文件一定要是json格式)
# json.load(open('a.json', "r"))
# 把dict字典变成json格式，生成到外部文件里面
# json.dump(dict, open('a.json', "w"))
#
# 从内存处理
# json = {"name": "abc"}
# json.load(json)
# 从内存处理
# dict = {"name": "abc"}
# json.load(dict)