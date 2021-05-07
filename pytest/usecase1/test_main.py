"""
シンプルな実用例
内容：検証項目で分類するテストケース
記述方法：pytestでテストケースをコーディングする場合は、クラス名とメソッド名の先頭は「test」にする
"""

from main import validate


class TestValid:
    def test_valid(self):
        """検証が正しいケース"""
        assert validate("a")
        assert validate("a" * 100)

    def test_invalid_too_log(self):
        """ 検証が正しくないケース 文字数が多い場合"""
        assert not validate("a" * 101)

    def test_invalid_too_short(self):
        """ 検証が正しくないケース 文字数が少ない場合"""
        assert not validate("")