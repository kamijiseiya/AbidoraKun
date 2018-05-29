"""取引所から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time
import ccxt  # 取引所ライブラリをインポート
from app import module

BITBANK = ccxt.bitbank()  # 取引所の指定
BINANCE = ccxt.binance()


class bitbank:
    """bitbankからの取引データを処理するクラス"""

    @property
    def btc(self):
        while True:
            try:
                # bitbankのIDを取得
                bitbnka_id = BITBANK.id

                # biybankのXRP/JPYのオーダーブックの取得
                bitbank_BTC = BITBANK.fetch_order_book('BTC/JPY')

                # bitbank_orderbookからBTC/JPYのbidsの値を取得
                BTC_bids = bitbank_BTC['asks'][0][0] \
                    if (bitbank_BTC['asks']) else None

                # bitbank_orderbookからBTC/JPYのasksの値を取得
                BTC_ask = bitbank_BTC['asks'][0][0] \
                    if (bitbank_BTC['asks']) else None

                orderbook = {'bitbank': {'bitbank_id': bitbnka_id}, 'bid': {bitbnka_id: BTC_bids},
                             'ask': {bitbnka_id: BTC_ask}}
                return orderbook
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

    @property
    def xrp(self):
        while True:
            try:
                # bitbankのIDを取得
                bitbnka_id = BITBANK.id
                # bitbank_orderbookからXRP/JPYのbidsの値を取得
                bitbank_orderbook = BITBANK.fetch_order_book('XRP/JPY')
                # bitbank_orderbookからBTC/JPYのbidsの値を取得
                XRP_bid = bitbank_orderbook['asks'][0][0] \
                    if (bitbank_orderbook['asks']) else None

                # bitbank_orderbookからBTC/JPYのasksの値を取得
                XRP_ask = bitbank_orderbook['asks'][0][0] \
                    if (bitbank_orderbook['asks']) else None

                orderbook = {'bitbank': {'bitbank_id': XRP_ask}, 'bid': {bitbnka_id: XRP_bid},
                             'ask': {bitbnka_id: XRP_ask}}
                return orderbook
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)


class BINANCE:
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
                binance_bit_btc = module.btc_to_jpy.btc_to_jpy(binance_orderbook['bids'][0][0])
                binance_ask_btc = module.btc_to_jpy.btc_to_jpy(binance_orderbook['asks'][0][0])

                orderbook = {'binance': {'binance_id': binance_id}, 'bid': {binance_id: binance_bid},
                             'ask': {binance_id: binance_ask}, 'bit_btc/jpy': {binance_id: binance_bit_btc},
                             'ask_btc/jpy': {binance_id: binance_ask_btc}}
                return orderbook
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)


CALLSAMPLEDATA = bitbank()
print(CALLSAMPLEDATA.xrp)
