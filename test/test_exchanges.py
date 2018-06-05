"""exchanges.pyのテスト"""
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
import unittest
import app.module2.exchanges


class TestBitbank(unittest.TestCase):
    """exchanges.pyのテストクラス"""

    def test_returnbinancedata_id(self):
        """bainasuから値がとってこれているかどうか"""
        testdata = app.module2.exchanges.Binance.xrp(0)
        print(testdata)
        print(testdata['binance'].get('binance_id'))
        self.assertEqual('binance', testdata['binance'].get('binance_id'))

    def test_bitbank_id_bitbank(self):
        """bitbankから値がとってこれているかどうか"""
        bitbankdata = app.module2.exchanges.Bitbank.xrp(0)
        print(bitbankdata['bitbank'].get('bitbank_id'))
        self.assertEquals('bitbank', bitbankdata['bitbank'].get('bitbank_id'))


if __name__ == "__main__":
    unittest.main()
