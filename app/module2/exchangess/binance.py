"""取引所（バイナンス）から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time
import ccxt  # 取引所ライブラリをインポート

class BINANCE:
    """binanceからの取引データを処理するクラス"""

    def xrp(self):
        """binanceの取引データを返す"""
        while True:
            try:
                binance = ccxt.binance()
                # bitbankのIDを取得
                binance_id = binance.id
                # biybankのXRP/JPYのオーダーブックの取得
                binance_orderbook = binance.fetch_order_book('XRP/BTC')
                # bitbank_orderbookからbidsの値を取得
                binance_bid = binance_orderbook['bids'][0][0] \
                    if (binance_orderbook['bids']) else None
                # bitbank_orderbookからasksの値を取得
                binance_ask = binance_orderbook['asks'][0][0] \
                    if (binance_orderbook['asks']) else None

                # bitbank_orderbook_btcからbidsの値を取得

                orderbook = {'binance': {'bianca_id': binance_id},
                             'bid': {binance_id: binance_bid},
                             'ask': {binance_id: binance_ask}, }
                return orderbook
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)
