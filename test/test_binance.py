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


    def test_get_address_btc_address(self):
        """get_addressからBTCのアドレスが返されるかのテスト"""
        addressdata = binance.BINANCE.get_address('BTC')
        print(addressdata.get('address'))
        self.assertEqual('1BXWsTqpUf23wottHy7utAqrCU3ygpMwCZ',addressdata['address'])

    def test_get_address_btc_tag(self):
        """get_addressからBTCのtagが返されるかのテスト"""
        addressdata = binance.BINANCE.get_address('BTC')
        print(addressdata.get('tag'))
        self.assertEqual('', addressdata['tag'])

    def test_get_address_xrp_address(self):
        """get_addressからXRPのaddressが返されるかのテスト"""
        addressdata = binance.BINANCE.get_address('XRP')
        print(addressdata.get('address'))
        self.assertEqual('rEb8TK3gBgk5auZkwc6sHnwrGVJH8DuaLh', addressdata['address'])

        def test_get_address_xrp_tag(self):
            """get_addressからXRPのtagが返されるかのテスト"""
            addressdata = binance.BINANCE.get_address('XRP')
            print(addressdata.get('tag'))
            self.assertEqual('103219183', addressdata['tag'])

if __name__ == "__main__":
    unittest.main()
