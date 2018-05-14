"""取引所（バイナンス）から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import ccxt  # 取引所ライブラリをインポート

BINANCE = ccxt.binance()# 取引所の指定



def bitbank_id() -> " 取引所ID":
    """取引所IDを返します"""
    return BINANCE.id

def bitbank_bid() -> " 購入価格":
    """購入価格を返します"""
    bitbank_orderbook = BINANCE.fetch_order_book('XRP/JPY')
    return bitbank_orderbook['bids'][0][0] if (bitbank_orderbook['bids'])else None


def bitbank_ask() -> "売却価格":
    """売却価格を返します"""
    bitbank_orderbook = BINANCE.fetch_order_book('XRP/JPY')
    return bitbank_orderbook['asks'][0][0] if (bitbank_orderbook['asks'])else None


def bitbank_spread() -> "スプレッド":
    """スプレッド情報を返します"""
    return (bitbank_ask() - bitbank_bid()) if (bitbank_bid() and bitbank_ask()) else None

if __name__ == "__main__": #テスト用
    print(bitbank_bid) #xrp_btcの中身を表示する
