"""BTCからJPYへJPYからBTCに変換するモジュールです"""

# インポート
import ccxt
# インポート
from app import module


def btc_to_jpy(btc):
    '''
    BTCの枚数を引数として受け取り、日本円の金額に変換するメソッドです
    '''
    # BTC/JPYのレートを取得する
    bitbank = ccxt.bitbank()  # bitbankの情報を呼び出す
    orderbook = bitbank.fetch_order_book('BTC/JPY')  # BTC/JPYのオーダーブック取得
    # BTC/JPYのBIDを取得する
    bid = orderbook['bids'][0][0] if (orderbook['bids']) else None

    jpy = btc * bid  # BTCを日本円の額に変換する
    return jpy


if __name__ == "__main__":  # テスト用
    print(btc_to_jpy(1))

'''
Bitbankから取得したXRP/JPYをBTCに対応させるモジュールです
'''


def xrp_btc_bid(xrp_jpy_bid):
    '''
    XRP/JPYのbidを引数で受け取り、XRP/BTCのbidに変換して返すメソッドです
    '''
    # BTC/JPYのASKを取得する
    btc_jpy_ask = exchanges_bitbank.bitbank_btc_ask()

    # XRP/BTCのBIDを計算する
    xrp_btc_bid = xrp_jpy_bid / btc_jpy_ask if (xrp_jpy_bid and btc_jpy_ask) else None

    # return
    return xrp_btc_bid


def xrp_btc_ask(xrp_jpy_ask):
    '''
    XRP/JPYのaskを引数で受け取り、XRP/BTCのaskに変換して返すメソッドです
    '''
    # BTC/JPYのBIDを取得する
    btc_jpy_bid = exchanges_bitbank.bitbank_btc_bid()

    # XRP/BTCのASKを計算する
    xrp_btc_ask = xrp_jpy_ask / btc_jpy_bid if (xrp_jpy_ask and btc_jpy_bid) else None

    # return
    return xrp_btc_ask


if __name__ == "__main__":  # テスト用
    # 結果の表示
    print(xrp_btc_bid(80))
    print(xrp_btc_ask(80))
