"""取引所（バイナンス）から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time
import ccxt  # 取引所ライブラリをインポート
import json
# sqlite3 標準モジュールをインポート
import sqlite3
import re  # 正規表現を使用するため
from app.module.money_exchange import btc_to_jpy


# データベースファイルのパス
DBPATH = 'cash_cow_db.sqlite'

# データベース接続とカーソル生成
CONNECTION = sqlite3.connect(DBPATH)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
CURSOR = CONNECTION.cursor()

binance = ccxt.binance()
class BINANCE:
    """binanceからの取引データを処理するクラス"""

    def currencyinformation(self):
        """binanceの取引データを返す"""
        while True:
            try:
                # 通貨ペアself/JPYをcurrencypairに返却する。
                currencypair = BINANCE.currency_pair_creation(self)
                # biybankのcurrencypairのオーダーブックの取得
                binance_orderbook = binance.fetch_order_book(currencypair)
                # price_acquisitionからbitbank_bidにbitbank_orderbookのbidsの値を返却する。
                binance_bid = BINANCE.price_acquisition('bids', binance_orderbook)
                # price_acquisitionからbitbank_bidにbitbank_orderbookのbidsの値を返却する。
                binance_ask = BINANCE.price_acquisition('asks', binance_orderbook)
                #  タイプの確認のための処理
                print(binance_ask,
                      binance_bid)
                return [binance.id,
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
        result = binance.create_limit_buy_order(currency, amount, price)  # xrpを購入
        print(result)

    @staticmethod
    def sell(currency, amount, price, ):
        """売り注文をするメソッド"""
        result = binance.create_limit_sell_order(currency, amount, price)  # xrpを売却　
        print(result)

    def get_address(self):
        """binanceの取引通貨ごとのアドレスを返す"""
        if self == 'BTC' or self == 'XRP':
            while True:
                try:
                    print(json.dumps(BINANCE.exchange.fetch_deposit_address(self), indent=4))
                    address = BINANCE.exchange.fetch_deposit_address(self)['address']
                    tag = BINANCE.exchange.fetch_deposit_address(self)['tag']
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
            # テーブルがない場合は作成する。
            CURSOR.execute(
                "CREATE TABLE IF NOT EXISTS exchanges (name TEXT PRIMARY KEY, api TEXT,secret TEXT)")
            # INSERT
            CURSOR.execute("INSERT INTO exchanges VALUES (:name, :api,:secret)",
                           {'name': name, 'api': api, 'secret': secret})
            # 保存を実行（忘れると保存されないので注意）
            CONNECTION.commit()
            # 接続を閉じる
            CONNECTION.close()
            # 登録された値を返す
            return name, api, secret
        except sqlite3.Error as error:
            print('sqlite3.Error occurred:', error.args[0])
            print('すでに追加されています。')
            return None

    def get_api(name):
        try:
            CURSOR.execute("SELECT api,secret FROM exchanges where  name like" + "'"+name+"'")
            """正規表現で形を整える"""
            token = re.sub('\)|\(|\,|\\)|}|{|\'', '', str(CURSOR.fetchall()))
            CONNECTION.close()
            apikey,secretkey = token.split()
            apykey = re.sub('[[]|[]]', "",apikey)
            secretkey = re.sub('[[]|[]]', "", secretkey)
            return apykey, secretkey
        except sqlite3.Error as error:
            print('sqlite3.Error occurred:', error.args[0])
        return None

if __name__ == "__main__":  # テスト用に追加
    print(BINANCE.currencyinformation('XRP'))
    print(BINANCE.get_api('test'))