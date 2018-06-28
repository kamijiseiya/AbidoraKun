"""取引所から通貨情報を取得する"""
# coding: UTF-8 文字コード指定
import time
import ccxt  # 取引所ライブラリをインポート


class BITBANK:
    """bitbankからの取引データを処理するクラス"""

    def currencyinformation(self):
        """bitbankのself(選択した通貨)/JPY取引データを返す"""
        while True:
            try:
                bitbank = ccxt.bitbank()
                # 通貨ペアself/JPYをcurrencypairに返却する。
                currencypair = BITBANK.currency_pair_creation(self)
                # biybankのcurrencypairのオーダーブックの取得
                bitbank_orderbook = bitbank.fetch_order_book(currencypair)
                # price_acquisitionからbitbank_bidにbitbank_orderbookのbidsの値を返却する。
                bitbank_bid = BITBANK.price_acquisition('bids', bitbank_orderbook)
                # price_acquisitionからbitbank_bidにbitbank_orderbookのbidsの値を返却する。
                bitbank_ask = BITBANK.price_acquisition('asks', bitbank_orderbook)
                print(bitbank_bid,bitbank_ask)
                return {bitbank.id,bitbank_ask,bitbank_bid}

            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)


    def currency_pair_creation(self):
        """ 通貨ペアを返却する"""
        return self + '/JPY'
    def price_acquisition(self, orderbook):
        """selfで選択した価格をorderbookから取得しその値を返却する。"""
        return orderbook[self][0][0] \
            if (orderbook[self]) else None


if __name__ == "__main__":  # テスト用に追加
    print(BITBANK.currencyinformation('XRP'))