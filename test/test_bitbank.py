"""exchanges.pyのテスト"""
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
import unittest
from app.module.exchangess import bitbank

exhanges,ask,bid = bitbank.BITBANK.xrp('BTC');
class TestBitbank(unittest.TestCase):
    """bitbank.pyのテストクラス"""
    def test_bitbank_id_bitbank(self):
        """bitbankから値がとってこれているかどうか"""
        print(exhanges,ask,bid)
        self.assertEquals('bitbank', exhanges)


if __name__ == "__main__":
    unittest.main()
