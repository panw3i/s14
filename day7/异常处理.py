try:
    name[3]
    data["anme"]

except Exception as e:
    print("这里出错了:",e)
#
# except KeyError as e:
#     print(e)

# 抓住所有的错误

finally:
    print("不管错不错,最后都会执行")