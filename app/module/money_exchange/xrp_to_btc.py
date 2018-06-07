"""Bitbankから取得したXRPをBTCに対応させるモジュールです"""

# インポート
from app.module.exchangess import bitbank

def exchange_xrp_btc(xrp_jpy, pricetype):
    """XRP/JPYのpricetypeを引数で受け取り、XRP/BTCのpricetypeに変換して返すメソッドです"""

    # pricetypeが'bid'の場合
    if pricetype == 'bid':


        # BTC/JPYのASKを取得する

        bitbankorderbook = bitbank.BITBANK.currencyinformation('BTC')

        btc_jpy_ask = price_acquisition('ask', bitbankorderbook)

        # XRP/BTCのBIDを計算する
        xrp_btc_bid = xrp_jpy / btc_jpy_ask if (xrp_jpy and btc_jpy_ask) else None

        # return
        return xrp_btc_bid

    #pricetypeが'ask'の場合
    elif pricetype == 'ask':
        # BTC/JPYのBIDを取得する
        bitbankorderbook = bitbank.BITBANK.currencyinformation('BTC')

        btc_jpy_bid = price_acquisition('bid', bitbankorderbook)

        # XRP/BTCのASKを計算する
        xrp_btc_ask = xrp_jpy / btc_jpy_bid if (xrp_jpy and btc_jpy_bid) else None

        # return
        return xrp_btc_ask


def price_acquisition(pricetype, orderbook):
    """BTC/JPYのpricetypeで指定した引数をorderbookから取り出し、その値を返却する"""
    return orderbook[pricetype].get('bitbank')


if __name__ == "__main__":  # テスト用
    # 結果の表示

    print(exchange_xrp_btc(80, 'bid'))
    print(exchange_xrp_btc(80, 'ask'))
