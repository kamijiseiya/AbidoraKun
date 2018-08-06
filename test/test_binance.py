"""exchanges.pyのテスト"""
import os  # パスを操作するモジュール
import unittest
import sys  # パスを読み込むモジュール

sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
from app.module.exchangess import binance

EXHANGES, ASK, BID = binance.BINANCE.currencyinformation('XRP')


class TestBitbank(unittest.TestCase):
    """bainasu.pyのテストクラス"""
    def test_returnbinancedata_id(self):
        """bainasuから値がとってこれているかどうか"""

        print(EXHANGES, ASK, BID)
        print(EXHANGES)
        self.assertEqual('binance', EXHANGES)

    def test_get_address_btc_address(self):
        """get_addressからBTCのアドレスが返されるかのテスト"""
        addressdata = binance.BINANCE.get_address('BTC')
        print(binance.BINANCE.get_address('BTC'))
        print(addressdata)
        print(addressdata.get('address'))
        self.assertEqual('1BXWsTqpUf23wottHy7utAqrCU3ygpMwCZ', addressdata['address'])

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

    def test_get_address_jpy_none(self):
        """XRPとBTC以外の値(JPY)の場合get_addressからNoneが返されるかのテスト"""
        addressdata = binance.BINANCE.get_address('JPY')
        print(addressdata)
        self.assertIsNone(addressdata)

    def test_get_address_number_none(self):
        """XRPとBTC以外の値(数値)の場合get_addressからNoneが返されるかのテスト"""
        addressdata = binance.BINANCE.get_address(0)
        print(addressdata)
        self.assertIsNone(addressdata)

    def test_add_api(self):
        """APIキーが保存されたかどうか"""
        none = binance.BINANCE.add_api('test', '01', '02')
        """同じAPIキーが保存された場合例外処理が発生したかどうか"""
        self.assertIsNone(none)

    def test_get_api(self):
        """APIキーが検索できるかどうか"""
        apikey, secret = binance.BINANCE.get_api(1)
        print(apikey)
        self.assertEqual('zeJ2xO6LKOkWCX6Eb6E7b84P17oKUNrbhDYuZjWKWlEzrWLQAgv7mcjghQO5TbwG', apikey)
        """APIキーが保存されてない場合の処理"""
        none = binance.BINANCE.get_api(99)
        self.assertIsNone(none)

if __name__ == "__main__":
    unittest.main()
