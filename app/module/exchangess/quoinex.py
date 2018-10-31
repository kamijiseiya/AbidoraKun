"""取引所（バイナンス）から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time
import ccxt  # 取引所ライブラリをインポート
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール

sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
# sqlite3 標準モジュールをインポート
from sqlalchemy import exc
from app.module.exchangess.setting import session
from app.module.exchangess.exchangesdb import *


class Quoinex:
    """binanceからの取引データを処理するクラス"""

    @classmethod
    def public_quoinex(self):
        quoinex = ccxt.quoinex()
        return quoinex

    def currencyinformation(self):
        """binanceの取引データを返す"""
        while True:
            try:
                # 通貨ペアself/JPYをcurrencypairに返却する。
                currencypair = Quoinex.currency_pair_creation(self)
                # quoinexのcurrencypairのオーダーブックの取得
                quoinex_orderbook = Quoinex.public_quoinex().fetch_order_book(currencypair)
                # price_acquisitionからquoinex_bidにbitbank_orderbookのbidsの値を返却する。
                quoinex_bid = Quoinex.price_acquisition('bids', quoinex_orderbook)
                # price_acquisitionからquoinex_bidにbitbank_orderbookのbidsの値を返却する。
                quoinex_ask = Quoinex.price_acquisition('asks', quoinex_orderbook)
                #  タイプの確認のための処理
                return [Quoinex.public_quoinex().id,
                        quoinex_ask,
                        quoinex_bid]
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

    @staticmethod
    def buy(currency, amount, price, ):
        """買い注文をするメソッド"""
        result = Quoinex.private_binance().create_limit_buy_order(currency, amount, price)  # xrpを購入
        print(result)

    @staticmethod
    def sell(currency, amount, price, ):
        """売り注文をするメソッド"""
        result = Quoinex.private_binance().create_limit_sell_order(currency, amount, price)  # xrpを売却　
        print(result)



    def add_api(name, api, secret):
        """APIkキーを登録するメソッド"""
        try:
            # dbを作成する
            main(sys.argv)
            excanges = Exchanges()
            # quoinexのIDは3
            excanges.id = 3
            excanges.name = name
            excanges.api = api
            excanges.secret = secret
            session.add(excanges)
            session.commit()
            session.rollback()
            print(name + 'で追加されました')
            return name, api, secret
        except exc.IntegrityError as error:
            session.rollback()
            print('sqlite3.IntegrityError:', error.args[0])
            print('すでに追加されています。')
            return None

    def get_api(id):
        """apiキーを取得するメソッド"""
        try:
            excanges = session.query(Exchanges).get(id)
            return excanges.api, excanges.secret
        except AttributeError as error:
            print('登録されていません')
            return None

if __name__ == "__main__":  # テスト用に追加
           print(Quoinex.get_api(2))