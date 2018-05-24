"""取引所から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time
import ccxt  # 取引所ライブラリをインポート

BITBANK = ccxt.bitbank()  # 取引所の指定

class Sample:
    """bitbankからの取引データを処理するクラス"""
    def bitbank_id(self) -> " BITBANK取引所ID":
        """取引所IDを返します"""
        return BITBANK.id

    def bitbank(self):
        while True:
            try:
                #bitbankのIDを取得
                bitbnka_id = BITBANK.id
                #biybankのXRP/JPYのオーダーブックの取得
                bitbank_orderbook = BITBANK.fetch_order_book('XRP/JPY')
                #bitbank_orderbookからbidsの値を取得
                bitbank_bid = bitbank_orderbook['bids'][0][0] \
                    if (bitbank_orderbook['bids']) else None
                #bitbank_orderbookからasksの値を取得
                bitbank_ask = bitbank_orderbook['asks'][0][0] \
                    if (bitbank_orderbook['asks']) else None

                orderbook = {'bitbank':{}, 'open_price':{}, 'high_price':{}}
                orderbook['bitbank'] = {'bitbank_id': bitbnka_id}
                orderbook['open_price'] = {bitbnka_id: bitbank_bid}
                orderbook['high_price'] = {bitbnka_id: bitbank_ask}
                return orderbook
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)


CALLSAMPLEDATA = Sample()
print(CALLSAMPLEDATA.bitbank())

