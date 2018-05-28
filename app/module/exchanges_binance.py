"""取引所（バイナンス）から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import ccxt  # 取引所ライブラリをインポート

BINANCE = ccxt.binance()  # 取引所の指定


def binace_id() -> " 取引所ID":
        """取引所IDを返します"""
        return BINANCE.id


def binace_bid() -> " 購入価格":
    """購入価格を返します"""
    binace_orderbook = BINANCE.fetch_order_book('XRP/JPY')
    return binace_orderbook['bids'][0][0] if (binace_orderbook['bids']) else None


def binace_ask() -> "売却価格":
    """売却価格を返します"""
    binace_orderbook = BINANCE.fetch_order_book('XRP/BTC')
    return binace_orderbook['asks'][0][0] if (binace_orderbook['asks']) else None


def binace_spread() -> "スプレッド":
    """スプレッド情報を返します"""
    return (binace_ask() - binace_bid()) if (binace_bid() and binace_ask()) else None

if __name__ == "__main__":  #テスト用に追加
    try:
        print(binace_bid())
    except:
        import traceback
