# デコレーター
def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("デコレーターによる追加")
        return res + "!!!"

    return wrapper


# デコレートされる関数
def display(str):
    print(str)
    return str


print_something = decorator(display)
p_something = print_something("hello")
print(p_something)
