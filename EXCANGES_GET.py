"""取引所から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import ccxt  # 取引所ライブラリをインポート

BITBANK = ccxt.bitbank()  # 取引所の指定



def bitbank_id() -> " 取引所ID":
    """取引所IDを返します"""
    return bitbank_id == BITBANK.id


def bitbank_bid() -> " 購入価格":
    """購入価格を返します"""
    bitbank_orderbook = BITBANK.fetch_order_book('XRP/JPY')
    return bitbank_orderbook['bids'][0][0] if (bitbank_orderbook['bids']) > 0 else None


def bitbank_ask() -> "売却価格":
    """売却価格を返します"""
    bitbank_orderbook = BITBANK.fetch_order_book('XRP/JPY')
    return bitbank_orderbook['asks'][0][0] if (bitbank_orderbook['asks']) > 0 else None


def bitbank_spread() -> "スプレッド":
    """スプレッド情報を返します"""
    return (bitbank_ask() - bitbank_bid()) if (bitbank_bid() and bitbank_ask()) else None


if __name__ == '__main__':  # データが正しく返って来るかどうかテスト
    print(bitbank_bid())
    print(bitbank_ask())
    print(bitbank_spread())
