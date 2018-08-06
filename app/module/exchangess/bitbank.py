"""取引所から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time
import ccxt  # 取引所ライブラリをインポート

# エラー処理（例外処理）
bitbank = ccxt.bitbank()
"""bitbankを取得"""


class BITBANK:
    """bitbankからの取引データを処理するクラス"""

    def tickers(self):
        """XRPの取引高を取得するメソッド"""
        currencypair = BITBANK.currency_pair_creation(self)
        tk = bitbank.fetch_ticker(currencypair)
        return tk

    def currencyinformation(self):
        """bitbankのself(選択した通貨)/JPY取引データを返す"""
        while True:
            try:
                # 通貨ペアself/JPYをcurrencypairに返却する。
                currencypair = BITBANK.currency_pair_creation(self)
                # biybankのcurrencypairのオーダーブックの取得
                bitbank_orderbook = bitbank.fetch_order_book(currencypair)
                # price_acquisitionからbitbank_bidにbitbank_orderbookのbidsの値を返却する。
                bitbank_bid = BITBANK.price_acquisition('bids', bitbank_orderbook)
                # price_acquisitionからbitbank_bidにbitbank_orderbookのbidsの値を返却する。
                bitbank_ask = BITBANK.price_acquisition('asks', bitbank_orderbook)
                print(bitbank_bid, bitbank_ask)

                return {bitbank.id, bitbank_ask, bitbank_bid}

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
    def buy(currency, amount, price,):
        """買い注文をするメソッド"""
        result = bitbank.create_limit_buy_order(currency, amount, price)  # xrpを購入
        print(result)

    @staticmethod
    def sell(currency, amount, price, ):
        """売り注文をするメソッド"""

        result = bitbank.create_limit_sell_order(currency, amount, price)  # xrpを売却　
        print(result)

    def registration(name, api, secret):
        """" APIkキーを登録するメソッド"""
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
            return name, api,secret
        except sqlite3.Error as error:
            print('sqlite3.Error occurred:', error.args[0])
            print('すでに追加されています。')
            return 'none'


if __name__ == "__main__":  # テスト用に追加
    #print(BITBANK.registration('test', '0001', '0002'))
    print(BITBANK.currencyinformation('XRP'))
    print(BITBANK.tickers('XRP'))

