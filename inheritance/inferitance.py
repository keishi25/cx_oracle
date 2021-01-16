class Base(object):
    def __init__(self, base_val):
        self.base_val = base_val

    def print_value(self):
        print('base_val:', self.base_val)

    def base_only(self):
        print('defined in Base class')


# 単純な継承
class SimpleDerived(Base):
    pass


# 継承＆オーバーライド
class Derived(Base):
    """
    オーバーライド：サブクラスクラスが、スーパークラスのオブジェクトと同じ名前を使用し、機能を再定義すること
    オーバーライドすると、スーパークラスのインスタンス変数が使用不可になる
    """
    def __init__(self, base_val):
        super().__init__(base_val)
        # super().__init__()をすることで、スーパークラスのインスタンス変数が使用可能になる
        self.other = "aaa"

    # メソッドの単純オーバーライド
    # スーパークラスのメソッドを書き換える
    def print_value(self):
        print('base_val_over_ride:', self.base_val)

    # メソッドのオーバーライド＆スーパークラスのメソッド呼び出し
    # super()を使うことで、オーバーライド前のメソッドを呼べる
    def base_only(self):
        print('sub_class_method', self.base_val)
        super().base_only()  # オーバーライド前のスーパークラスのメソッド呼び出し

d = Derived(2)
print(d.base_val)
#d.base_only()
#d.print_value()


