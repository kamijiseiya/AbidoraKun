"""exchanges.pyのテスト"""
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
import unittest
from app.module.exchangess import binance

exhanges, ask, bid = binance.BINANCE.xrp(0)
class TestBitbank(unittest.TestCase):
    """bainasu.pyのテストクラス"""

    def test_returnbinancedata_id(self):
        """bainasuから値がとってこれているかどうか"""

        print(exhanges,ask,bid)
        print(exhanges)
        self.assertEqual('binance', exhanges)


if __name__ == "__main__":
    unittest.main()