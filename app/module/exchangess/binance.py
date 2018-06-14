"""取引所（バイナンス）から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time
import ccxt  # 取引所ライブラリをインポート
from app.module.money_exchange import btc_to_jpy


class BINANCE:
    """binanceからの取引データを処理するクラス"""

    def xrp(self):
        """binanceの取引データを返す"""
        while True:
            try:
                binance = ccxt.binance()
                # biybankのXRP/JPYのオーダーブックの取得
                binance_orderbook = binance.fetch_order_book('XRP/BTC')
                # bitbank_orderbookからbidsの値を取得
                binance_bid = binance_orderbook['bids'][0][0] \
                    if (binance_orderbook['bids']) else None
                # bitbank_orderbookからasksの値を取得
                binance_ask = binance_orderbook['asks'][0][0] \
                    if (binance_orderbook['asks']) else None
                print(btc_to_jpy.btc_to_jpy(binance_ask),
                        btc_to_jpy.btc_to_jpy(binance_bid))
                return [binance.id,
                        btc_to_jpy.btc_to_jpy(binance_ask),
                        btc_to_jpy.btc_to_jpy(binance_bid)]
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)
if __name__ == "__main__":  # テスト用に追加
    print(BINANCE.xrp(0))
