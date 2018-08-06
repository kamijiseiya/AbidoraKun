"""取引所から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import sys
import time
import ccxt  # 取引所ライブラリをインポート
# sqlite3 標準モジュールをインポート

from sqlalchemy import exc
from app.module.exchangess.setting import session
from app.module.exchangess.exchangesdb import main, Exchanges


class BITBANK:
    """bitbankからの取引データを処理するクラス"""

    @classmethod
    def private_bitbank(cls):
        """privateキーの処理"""
        try:
            api, secret = BITBANK.get_api(2)
            binances = ccxt.binance({
                'apiKey': api,
                'secret': secret
            })
            return binances
        except ccxt.BaseError:
            print("取引所から取引データを取得できません。")
            print("10秒待機してやり直します")
            time.sleep(10)

    @classmethod
    def public_bitbank(cls):
        """publicキーの処理"""
        bitbank = ccxt.bitbank()
        return bitbank

    def currencyinformation(self):
        """bitbankのself(選択した通貨)/JPY取引データを返す"""
        while True:
            try:
                # 通貨ペアself/JPYをcurrencypairに返却する。
                currencypair = BITBANK.currency_pair_creation(self)
                # biybankのcurrencypairのオーダーブックの取得
                bitbank_orderbook = BITBANK.public_bitbank().fetch_order_book(currencypair)
                # price_acquisitionからbitbank_bidにbitbank_orderbookのbidsの値を返却する。
                bitbank_bid = BITBANK.price_acquisition('bids', bitbank_orderbook)
                # price_acquisitionからbitbank_bidにbitbank_orderbookのbidsの値を返却する。
                bitbank_ask = BITBANK.price_acquisition('asks', bitbank_orderbook)
                print(bitbank_bid, bitbank_ask)

                return {BITBANK.public_bitbank().id, bitbank_ask, bitbank_bid}

            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

    def currency_pair_creation(self):
        """ 通貨ペアを返却する"""
        return self + '/JPY'

    def price_acquisition(self, orderbook):
        """selfで選択した価格をorderbookから取得しその値を返却する。"""
        return orderbook[self][0][0] \
            if (orderbook[self]) else None

    def tickers(self):
        """XRPの取引高を取得するメソッド"""
        currencypair = BITBANK.currency_pair_creation(self)
        volume = BITBANK.public_bitbank().fetch_ticker(currencypair)
        return volume
    @staticmethod
    def buy(currency, amount, price,):
        """買い注文をするメソッド"""
        result = BITBANK.public_bitbank()\
            .create_limit_buy_order(currency, amount, price)  # xrpを購入
        print(result)

    @staticmethod
    def sell(currency, amount, price, ):
        """売り注文をするメソッド"""

        result = BITBANK.public_bitbank()\
            .create_limit_sell_order(currency, amount, price)  # xrpを売却　
        print(result)

    def add_api(name, api, secret):
        """APIkキーを登録するメソッド"""
        try:
            # dbを作成する
            main(sys.argv)
            excanges = Exchanges()
            # bitbankのIDは2
            excanges.id = 2
            excanges.name = name
            excanges.api = api
            excanges.secret = secret
            session.add(excanges)
            session.commit()
            session.rollback()
            print(name + 'で追加されました')
            return name, api, secret
        except exc.IntegrityError:
            print('すでに追加されています。')
            return None

    def get_api(self):
        """apiキーを取得するメソッド"""
        try:
            excanges = session.query(Exchanges).get(self)
            return excanges.api, excanges.secret
        except AttributeError:
            print('登録されていません')
            return None