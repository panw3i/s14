class PanError(Exception):   # 所有的自定义异常都要继续自己Exception
    def __init__(self,msg):
        self.message = msg

    def __str__(self):
        return self.message

print(PanError(';;;'))

try:
    #a[0] = 1  程序在执行到这里的时候会抛出异常并被except接收到同时停止运行,所以出现错误的语句放在前后打印的结果不一样

    raise PanError("这是我写的第一个异常")
    a[0] = 1

except Exception as e:
    print(e)


"""
PanError 是  Exception 的子类
e 是 PanError的 实例
__str__  打印实例时显示的字符串


"""