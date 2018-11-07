"""取引所（バイナンス）から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import os
import sys

sys.path.append(os.path.abspath(os.path.join('..')))
import time
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
import ccxt  # 取引所ライブラリをインポート

sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
# sqlite3 標準モジュールをインポート
from sqlalchemy import exc
from app.module.money_exchange import btc_to_jpy
from app.module.exchangess.setting import session
from app.module.exchangess.exchangesdb import main, Exchanges


class BINANCE:
    """binanceからの取引データを処理するクラス"""

    @classmethod
    def private_binance(cls):
        """privateキーの処理"""

        try:
            print(BINANCE.get_api(1))
            api, secret = BINANCE.get_api(1)
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
    def public_binance(cls):
        """publicキーの処理"""
        binances = ccxt.binance()
        return binances

    def currencyinformation(self):
        """binanceの取引データを返す"""
        while True:
            try:
                # 通貨ペアself/JPYをcurrencypairに返却する。
                currencypair = BINANCE.currency_pair_creation(self)
                # biybankのcurrencypairのオーダーブックの取得
                binance_orderbook = BINANCE.public_binance().fetch_order_book(currencypair)
                # price_acquisitionからbitbank_bidにbitbank_orderbookのbidsの値を返却する。
                binance_bid = BINANCE.price_acquisition('bids', binance_orderbook)
                # price_acquisitionからbitbank_bidにbitbank_orderbookのbidsの値を返却する。
                binance_ask = BINANCE.price_acquisition('asks', binance_orderbook)
                #  タイプの確認のための処理
                return [BINANCE.public_binance().id,
                        btc_to_jpy.btc_to_jpy(binance_ask),
                        btc_to_jpy.btc_to_jpy(binance_bid)]
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                return messege == ['取引所から取引データを取得できません。']
                time.sleep(10)

    def currency_pair_creation(self):
        """ 通貨ペアを返却する"""
        return self + '/BTC'

    def price_acquisition(self, orderbook):
        """selfで選択した価格をorderbookから取得しその値を返却する。"""
        return orderbook[self][0][0] \
            if (orderbook[self]) else None

    @staticmethod
    def buy(currency, amount, price, ):
        """買い注文をするメソッド"""
        result = BINANCE.private_binance(). \
            create_limit_buy_order \
            (currency, amount, price)  # xrpを購入
        print(result)

    @staticmethod
    def sell(currency, amount, price, ):
        """売り注文をするメソッド"""
        result = BINANCE.private_binance(). \
            create_limit_sell_order \
            (currency, amount, price)  # xrpを売却　
        print(result)

    def get_address(self):
        """binanceの取引通貨ごとのアドレスを返す"""
        try:
            address = BINANCE.private_binance().fetch_deposit_address(self)['address']
            tag = BINANCE.private_binance().fetch_deposit_address(self)['tag']
            addressinformation = {'address': address, 'tag': tag}
            return addressinformation
        except ccxt.BaseError:
            print("取引所から取引データを取得できません。")
            print("10秒待機してやり直します")
            time.sleep(10)
        else:
            return None

    # 注文数を取得するメソッド
    def getOrdersCount(self, Symbol):

        try:
            # josnデータをいてる配列の作成
            orders = self
            oLen = []

            # for文で引数から指定された価格のペアの情報を検索
            for i, o in enumerate(orders):
                if (orders[i]['info']['sybol'] == Symbol):
                    oLen.append(i)
            Len = len(oLen)
            oLen.clear()
            return Len

        except Exchanges as e:
            print("Exception => Get Pending Orders Count", str(e))
            return None
        
        # jsonの取得（Orders のレスポンスの取得）
        orders = BINANCE.private_binance().fetch_open_orders()
        # 引数にjosnと価格のペアを指定して要素情報の取得
        orderCount = BINANCE.getOrdersCount(orders, 'XBTUSD')
        print(orderCount)

    def add_api(name, api, secret):
        """APIkキーを登録するメソッド"""
        try:
            # dbを作成する
            main(sys.argv)
            excanges = Exchanges()
            # binanceのIDは１
            excanges.id = 1
            excanges.name = name
            excanges.api = api
            excanges.secret = secret
            session.add(excanges)
            session.commit()
            print(name + 'で追加されました')
            return name, api, secret
        except exc.IntegrityError:
            session.rollback()
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


if __name__ == "__main__":  # テスト用に追加
    print(BINANCE.get_address('XRP'))
