"""取引所から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time
import ccxt  # 取引所ライブラリをインポート

BITBANK = ccxt.bitbank()  # 取引所の指定
BINANCE = ccxt.binance()


class Bitbank:
    """bitbankからの取引データを処理するクラス"""
    def btc(self):
        while True:
            try:
                # bitbankのIDを取得
                bitbnka_id = BITBANK.id
                # biybankのXRP/JPYのオーダーブックの取得
                bitbank_orderbook = BITBANK.fetch_order_book('BTC/JPY')
                # bitbank_orderbookからbidsの値を取得
                bitbank_bid = bitbank_orderbook['bids'][0][0] \
                    if (bitbank_orderbook['bids']) else None
                # bitbank_orderbookからasksの値を取得
                bitbank_ask = bitbank_orderbook['asks'][0][0] \
                    if (bitbank_orderbook['asks']) else None

                orderbook = {'bitbank': {}, 'bid': {}, 'ask': {}}

                orderbook['bitbank'] = {'bitbank_id': bitbnka_id}
                orderbook['bid'] = {bitbnka_id:  bitbank_bid}
                orderbook['ask'] = {bitbnka_id:  bitbank_ask}
                return orderbook

            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(5)



    def xrp(self):
        while True:
            try:
                # bitbankのIDを取得
                bitbnka_id = BITBANK.id
                # biybankのXRP/JPYのオーダーブックの取得
                bitbank_orderbook = BITBANK.fetch_order_book('XRP/JPY')
                # bitbank_orderbookからbidsの値を取得
                bitbank_bid = bitbank_orderbook['bids'][0][0] \
                    if (bitbank_orderbook['bids']) else None
                # bitbank_orderbookからasksの値を取得
                bitbank_ask = bitbank_orderbook['asks'][0][0] \
                    if (bitbank_orderbook['asks']) else None

                orderbook = {'bitbank': {}, 'bid': {}, 'ask': {},}
                orderbook['bitbank'] = {'bitbank_id': bitbnka_id}
                orderbook['bid'] = {bitbnka_id: bitbank_bid}
                orderbook['ask'] = {bitbnka_id: bitbank_ask}
                return orderbook
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(5)


class Binance:
    """binanceからの取引データを処理するクラス"""

    def xrp(self):
        """binanceの取引データを返す"""
        while True:
            try:
                # bitbankのIDを取得
                binance_id = BINANCE.id
                # biybankのXRP/JPYのオーダーブックの取得
                binance_orderbook = BINANCE.fetch_order_book('XRP/BTC')
                # bitbank_orderbookからbidsの値を取得
                binance_bid = binance_orderbook['bids'][0][0] \
                    if (binance_orderbook['bids']) else None
                # bitbank_orderbookからasksの値を取得
                binance_ask = binance_orderbook['asks'][0][0] \
                    if (binance_orderbook['asks']) else None

                # bitbank_orderbook_btcからbidsの値を取得
                binance_bit_btc = 0
                binance_ask_btc = 0
                orderbook = {'binance': {'binance_id': binance_id}, 'bid': {binance_id: binance_bid},
                             'ask': {binance_id: binance_ask}, 'bit_btc/jpy': {binance_id: binance_bit_btc},
                             'ask_btc/jpy': {binance_id: binance_ask_btc}}
                return orderbook
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)


sampleo = Binance()
print(sampleo.xrp())

CALLSAMPLEDATA = Bitbank()
print(CALLSAMPLEDATA.btc())
