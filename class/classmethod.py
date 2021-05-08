"""
classmethod使用方法
メリット:クラスから直接メソッドを呼べる（クラスをインスタンス化する必要なし）
使われるケース：メソッドの処理とそれに基づいて変更されたインスタンス変数にアクセスできる
"""


# classmethodを使用しないケース
class Item1:

    def __init__(self, id, name):
        self.id = id
        self.name = name


def retrieve_item(id):
    data = {"name":"taka"}
    return Item1(id, data["name"])


# classmetodを使用するケース
class Item2:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @classmethod
    def retrieve_item(cls, id):
        data = {"name": "taka"}
        return cls(id, data["name"])  # コンストラクタに引数が渡される


if __name__ == '__main__':
    # classmethodを使用しないケース
    # moduleのインストールは、Item1とretrieve_itemの二つ
    out = retrieve_item(2)
    print(out.id)
    print(out.name)

    # classmetodを使用するケース
    # moduleのインストールは、Item2のクラスだけで良い
    out = Item2.retrieve_item(2)
    print(out.id)
    print(out.name)
