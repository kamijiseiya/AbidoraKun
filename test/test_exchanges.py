"""exchanges.pyのテスト"""
import unittest
import app.module.exchanges as module
class TestBitbank(unittest.TestCase):
    """exchanges.pyのテストクラス"""

    def test_returnbinancedata_id(self):
        """bainasuから値がとってこれているかどうか"""
        testdata = module.Binance.xrp(0)
        print(testdata)
        print(testdata['binance'].get('binance_id'))
        self.assertEqual('binance', testdata['binance'].get('binance_id'))

    def test_bitbank_id_bitbank(self):
        """bitbankから値がとってこれているかどうか"""
        bitbankdata = module.Bitbank.xrp(0)
        print(bitbankdata['bitbank'].get('bitbank_id'))
        self.assertEquals('bitbank', bitbankdata['bitbank'].get('bitbank_id'))


if __name__ == "__main__":
    unittest.main()
