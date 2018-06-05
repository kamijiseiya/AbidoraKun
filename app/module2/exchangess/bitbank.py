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
                bitbnka_id = bitbank.id  # bitbankのIDを取得
                # biybankのXRP/JPYのオーダーブックの取得
                bitbank_orderbook = bitbank.fetch_order_book('BTC/JPY')
                # bitbank_orderbookからbidsの値を取得
                bitbank_bid = bitbank_orderbook['bids'][0][0] \
                    if (bitbank_orderbook['bids']) else None
                # bitbank_orderbookからasksの値を取得
                bitbank_ask = bitbank_orderbook['asks'][0][0] \
                    if (bitbank_orderbook['asks']) else None
                orderbook = {'bitbank': {}, 'bid': {}, 'ask': {}}
                orderbook['bitbank'] = {'bitbank_id': bitbnka_id}
                orderbook['bid'] = {bitbnka_id: bitbank_bid}
                orderbook['ask'] = {bitbnka_id: bitbank_ask}
                return orderbook

            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

    @property
    def xrp(self):
        while True:
            try:
                bitbank = ccxt.bitbank()  # 取引所の指定
                # bitbankのIDを取得
                bitbnka_id = bitbank.id
                # biybankのXRP/JPYのオーダーブックの取得
                bitbank_orderbook = bitbank.fetch_order_book('XRP/JPY')
                # bitbank_orderbookからbidsの値を取得
                bitbank_bid = bitbank_orderbook['bids'][0][0] \
                    if (bitbank_orderbook['bids']) else None
                # bitbank_orderbookからasksの値を取得
                bitbank_ask = bitbank_orderbook['asks'][0][0] \
                    if (bitbank_orderbook['asks']) else None

                orderbook = {'bitbank': {}, 'bid': {}, 'ask': {}}
                orderbook['bitbank'] = {'bitbank_id': bitbnka_id}
                orderbook['bid'] = {bitbnka_id: bitbank_bid}
                orderbook['ask'] = {bitbnka_id: bitbank_ask}
                return orderbook
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)
