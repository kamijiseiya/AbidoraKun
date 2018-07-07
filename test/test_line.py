"""line.pyのテスト"""
import unittest
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定

from app.module.sns import line


class Testline(unittest.TestCase):
    """bitbank.pyのテストクラス"""

    def test_registration(self):
        """入力された値が保存されたかどうか"""
        type = line.LINE.registration('test', 'jojnvsidvnpsd')
        """すでに登録された値が登録された場合の例外処理のテスト"""
        print(type)
        self.assertIsNone(type)

    def test_search_apykey(self):
     """値が取り出せるかどうか"""
     type = line.LINE.search_apykey('test')
     """すでに登録された値が登録された場合の例外処理のテスト"""
     print(type)
     self.assertEqual('[jojnvsidvnpsd]', type)

if __name__ == "__main__":
    unittest.main()