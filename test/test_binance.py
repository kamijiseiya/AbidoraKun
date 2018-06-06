"""exchanges.pyのテスト"""
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
import unittest
from app.module.exchangess import binance


class TestBitbank(unittest.TestCase):
    """bainasu.pyのテストクラス"""

    def test_returnbinancedata_id(self):
        """bainasuから値がとってこれているかどうか"""
        testdata = binance.BINANCE.xrp(0)
        print(testdata)
        print(testdata['binance'].get('binance_id'))
        self.assertEqual('binance', testdata['binance'].get('binance_id'))


if __name__ == "__main__":
    unittest.main()
