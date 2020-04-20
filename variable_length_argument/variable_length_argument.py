"""
可変長引数
*=任意の複数の引数をtupleで受け取る
**=任意の複数のキーワード引数をdictionaryで受け取る

慣例として、変数名に*argsと**kwargsを使用する
"""


def func_args(*a):
    print(a)
    print(type(a))


def func_kwargs(**b):
    print(b)
    print(type(b))


def func_conbi(*a, **b):
    print(a)
    print(type(a))
    print(b)
    print(type(b))



#sunc_args(1, 2, 3)
#func_kwargs(key1=1, key2=2, key3=3)

#func_conbi(1, 2, 3)
#func_conbi(key1=1, key2=2, key3=3)

"""
引数のtypeから、
*argsなのか**kwargsなのか判断を行う
"""
func_conbi(1, 2, 3, key1=1, key2=2, key3=3)
