"""
シンプルな実用例
内容：検証項目で分類するテストケース
記述方法
・pytestでテストケースをコーディングする場合は、クラス名とメソッド名の先頭は「test」にする
・@pytest.mark.parametrize("変数名",[(タプル)])
　例　@pytest.mark.parametrize("test_input,expected", [("3+5", 8), ("2+4", 6), ("6*9", 42)])　
    二つの変数名に対して、要素２のタプルが３ケース分準備されている
"""
import pytest
from main import validate


class TestValid:
    @pytest.mark.parametrize("text", ["a", "a" * 100])
    def test_valid(self, text):
        """検証が正しいケース"""
        assert validate(text)

    @pytest.mark.parametrize("text", ["", "a" * 101])
    def test_invalid(self, text):
        """ 検証が正しくないケース 文字数が多い場合"""
        assert not validate(text)

