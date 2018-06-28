"""line.pyのテスト"""
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
import unittest
from app.module.sns import line


class Testline(unittest.TestCase):
    """bitbank.pyのテストクラス"""

    def test_registration(self):
        """bitbankからXRPがとってこれているかどうか"""
        name, api, = line.LINE.registration('line','jojnvsidvnpsd');
        print(api, name)

        self.assertEqual('line' == name, 'jojnvsidvnpsd' == api)

if __name__ == "__main__":
    unittest.main()