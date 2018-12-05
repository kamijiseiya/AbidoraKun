"""quoinex.pyのテスト"""
import os  # パスを操作するモジュール
import unittest
import sys  # パスを読み込むモジュール

sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
from app.module.exchangess import quoinex

EXHANGES, ASK, BID = quoinex.Quoinex.currencyinformation('XRP')


class TestBitbank(unittest.TestCase):
    """quoinex.pyのテストクラス"""
    def test_public_returnbinancedata_id(self):
        """public.quionexから値がとってこれているかどうか"""
        print(EXHANGES, ASK, BID)
        print(EXHANGES)
        self.assertEqual('quoinex', EXHANGES)

    def test_currency_pair_btc_jpy(self):
        self.assertEqual('XRP/JPY', quoinex.Quoinex.currency_pair_creation('XRP'))
if __name__ == "__main__":
    unittest.main()
