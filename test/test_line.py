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

        name, api, = line.LINE.registration('test', 'jojnvsidvnpsd')
        self.assertEqual(name == 'test', api == 'jojnvsidvnpsd')

        """例外処理が発生したかどうか"""
        self.assertEqual('none' ,line.LINE.registration('test', 'jojnvsidvnpsd2222'))

