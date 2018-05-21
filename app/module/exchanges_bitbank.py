"""取引所から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time

import ccxt  # 取引所ライブラリをインポート

BITBANK = ccxt.bitbank()  # 取引所の指定


def bitbank_id() -> " BITBANK取引所ID":
    """取引所IDを返します"""
    return BITBANK.id



def bitbank_bid() -> " RXP/BTC購入価格":
    """購入価格を返します"""
    bitbank_orderbook = BITBANK.fetch_order_book('XRP/JPY')
    return bitbank_orderbook['bids'][0][0] if (bitbank_orderbook['bids']) else None


def bitbank_ask() -> "RXP/BTC売却価格":
    """売却価格を返します"""
    bitbank_orderbook = BITBANK.fetch_order_book('XRP/JPY')
    return bitbank_orderbook['asks'][0][0] if (bitbank_orderbook['asks'])  else None


def bitbank_spread() -> "RXP/BTCスプレッド":
    """スプレッド情報を返します"""
    return (bitbank_ask() - bitbank_bid()) if (bitbank_bid() and bitbank_ask()) else None


def bitbank_btc_bid() -> "BTC/JPY購入価格":
    """売却価格を返します"""
    bitbank_orderbook = BITBANK.fetch_order_book('BTC/JPY')
    return bitbank_orderbook['asks'][0][0] if (bitbank_orderbook['asks'])  else None

def bitbank_btc_ask() -> "BTC/JPY売却価格":
    """売却価格を返します"""
    bitbank_orderbook = BITBANK.fetch_order_book('BTC/JPY')
    return bitbank_orderbook['bids'][0][0] if (bitbank_orderbook['bids'])  else None

if __name__ == "__main__": #テスト用に追加
    print(bitbank(bitbank[id()]))
