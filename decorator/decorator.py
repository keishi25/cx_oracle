# デコレーター
def deco(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("デコレーターによる追加")
        return res + "!!!"

    return wrapper


# デコレートされる関数
@deco  # @decoを付けることでデコレートできる
def display(str):
    print(str)
    return str


p_something = display("hello")
print(p_something)
