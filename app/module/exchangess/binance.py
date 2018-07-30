"""取引所（バイナンス）から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time
import ccxt  # 取引所ライブラリをインポート
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
# sqlite3 標準モジュールをインポート
import sqlite3
import re  # 正規表現を使用するため
from app.module.money_exchange import btc_to_jpy
from app.config.setting import  session
from app.config.exchanges import *

# データベースファイルのパス
DBPATH = '../../module/config'

# データベース接続とカーソル生成
CONNECTION = sqlite3.connect(DBPATH)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
CURSOR = CONNECTION.cursor()


class BINANCE:
    """binanceからの取引データを処理するクラス"""

    @classmethod
    def private_binance(self):

        try:
            api, secret = BINANCE.get_api('BINANCE')
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
    def public_binance(self):
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
        result = BINANCE.private_binance().create_limit_buy_order(currency, amount, price)  # xrpを購入
        print(result)

    @staticmethod
    def sell(currency, amount, price, ):
        """売り注文をするメソッド"""
        result = BINANCE.private_binance().create_limit_sell_order(currency, amount, price)  # xrpを売却　
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

    def add_api(name, api, secret):
        """APIkキーを登録するメソッド"""
        try:
            excanges = Exchanges
            excanges.name = name
            excanges.api = api
            excanges.secret = secret
            print(name+'で追加されました')
            return name, api, secret
        except sqlite3.Error as error:
            print('sqlite3.Error occurred:', error.args[0])
            print('すでに追加されています。')
            return None

    def get_api(name):
        """apiキーを取得するメソッド"""
        try:
            CURSOR.execute("SELECT api,secret FROM exchanges where  name like" + "'" + name + "'")
            """正規表現で形を整える"""
            token = re.sub('\)|\(|\,|\\)|}|{|\'', '', str(CURSOR.fetchall()))
            # 配列に変換する
            apikey = re.sub('[[]|[]]', "", token)
            CONNECTION.close()
            return apikey.split()
        except sqlite3.Error as error:
            print('sqlite3.Error occurred:', error.args[0])
        return None


if __name__ == "__main__":  # テスト用に追加
    print(BINANCE.add_api('BINANCE', 'zeJ2xO6LKOkWCX6Eb6E7b84P17oKUNrbhDYuZjWKWlEzrWLQAgv7mcjghQO5TbwG', 'yhiEdfHFn5VYTGFCRM3mvwuH4T2qty4LlBA1GbVSVEi6bwPkYRd86f05SpFWcAOB'))