user,passwd = 'li',78

def auth(func):
    def wrapper(*args,**kwargs):
        username = input("your name : ")
        password = input(" your passwd ")

        if user == username and passwd == password:
            print("succuess!~")
            func(*args,**kwargs)
        else:
            exit("sb")
    return  wrapper()


@auth
def index():
    print('welcome to index page')

@auth
def home():
    print('welcome to home page')

@auth
def bbs():
    print('welcome to bbs page')
