
import unittest
from app import module


class TestBitbank(unittest.TestCase):
    # 値がとってこれるかどうか　エラーが発生するかどうか
    def test_returnbinancedata_id_binance(self):
        """bainasuから値がとってこれているかどうか"""
        testdata = module.exchanges.BINANCE.xrp(0)
        print(testdata)
        print(testdata['binance'].get('binance_id'))
        self.assertEqual('binance', testdata['binance'].get('binance_id'))

    def test_bitbank_id_bitbank(self):
        """bitbankから値がとってこれているかどうか"""
        bitbankdata = module.exchanges.bitbank.xrp(0)
        print(bitbankdata)
        self.assertEquals('bitbank' , bitbankdata['bitbank'].get('bitbank_id'))


if __name__ == "__main__":
    unittest.main()
