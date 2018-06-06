"""取引所から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time
import ccxt  # 取引所ライブラリをインポート


class BITBANK:
    """bitbankからの取引データを処理するクラス"""

    def btc(self):
        while True:
            try:
                bitbank = ccxt.bitbank()  # 取引所の指定
                # biybankのXRP/JPYのオーダーブックの取得
                bitbank_orderbook = bitbank.fetch_order_book('BTC/JPY')
                # bitbank_orderbookからbidsの値を取得
                bitbank_bid = bitbank_orderbook['bids'][0][0] \
                    if (bitbank_orderbook['bids']) else None
                # bitbank_orderbookからasksの値を取得
                bitbank_ask = bitbank_orderbook['asks'][0][0] \
                    if (bitbank_orderbook['asks']) else None
                orderbook = {'bitbank': {
                    'bitbank_id': bitbank.id
                }, 'bid': {
                    bitbank.id: bitbank_bid
                }, 'ask': {
                    bitbank.id: bitbank_ask
                }}
                return orderbook

            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

    def xrp(self):
        while True:
            try:
                bitbank = ccxt.bitbank()  # 取引所の指定
                # biybankのXRP/JPYのオーダーブックの取得
                bitbank_orderbook = bitbank.fetch_order_book('XRP/JPY')
                # bitbank_orderbookからbidsの値を取得
                bitbank_bid = bitbank_orderbook['bids'][0][0] \
                    if (bitbank_orderbook['bids']) else None
                # bitbank_orderbookからasksの値を取得
                bitbank_ask = bitbank_orderbook['asks'][0][0] \
                    if (bitbank_orderbook['asks']) else None

                orderbook = {'bitbank': {
                    'bitbank_id': bitbank.id
                }, 'bid': {
                    bitbank.id: bitbank_bid
                }, 'ask': {
                    bitbank.id: bitbank_ask
                }}
                return orderbook
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)
