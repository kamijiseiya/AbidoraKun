"""取引所から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time

import ccxt  # 取引所ライブラリをインポート

BITBANK = ccxt.bitbank()  # 取引所の指定


def bitbank_id() -> " BITBANK取引所ID":
    """取引所IDを返します"""
    return BITBANK.id

def bitbank(min,i):

    bitbnka_id = BITBANK.id

    bitbank_orderbook = BITBANK.fetch_order_book('XRP/JPY')

    bitbank_bid = bitbank_orderbook['bids'][0][0] if (bitbank_orderbook['bids']) else None

    bitbank_ask = bitbank_orderbook['asks'][0][0] if (bitbank_orderbook['asks']) else None


    while True:
            return {"bid": bitbnka_id[str(min)][i][0],
                    "open_price": bitbank_bid[str(min)][i][1],
                    "high_price": bitbank_ask[str(min)][i][2],
                    "close_price": bitbank_spread[str(min)][i][3]}


            print("取引所のデータ取得でエラー発生 : ", e)
            print("10秒待機してやり直します")
            time.sleep(10)

if __name__ == "__main__": #テスト用に追加
    print(bitbank(min,0))