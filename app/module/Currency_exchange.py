"""BTCからJPYへJPYからBTCに変換するモジュールです"""

# インポート
import ccxt
# インポート
from app import module


def btc_to_jpy(btc):
    '''
    BTCの枚数を引数として受け取り、日本円の金額に変換するメソッドです
    '''

    BITBANKORDERBOOK = module.exchanges.bitbank.btc(0)
    bid = BITBANKORDERBOOK['bid'].get('bitbank')
    jpy = btc * bid  # BTCを日本円の額に変換する bitbank btc/jpy bidを呼び出す。
    return jpy


if __name__ == "__main__":  # テスト用
    print(btc_to_jpy(1))

'''
Bitbankから取得したXRP/JPYをBTCに対応させるモジュールです
'''


def exchange_xrp_btc_bid(xrp_jpy_bid):
    '''
    XRP/JPYのbidを引数で受け取り、XRP/BTCのbidに変換して返すメソッドです
    '''
    #BTC/JPYのASKを取得する

    BITBANKORDERBOOK = module.exchanges.bitbank.btc(0)

    btc_jpy_ask = BITBANKORDERBOOK['ask'].get('bitbank')

    #XRP/BTCのBIDを計算する
    xrp_btc_bid = xrp_jpy_bid / btc_jpy_ask if (xrp_jpy_bid and btc_jpy_ask) else None

    #return
    return xrp_btc_bid


def exchange_xrp_btc_ask(xrp_jpy_ask):
    '''
    XRP/JPYのaskを引数で受け取り、XRP/BTCのaskに変換して返すメソッドです
    '''
    #BTC/JPYのBIDを取得する
    BITBANKORDERBOOK = module.exchanges.bitbank.btc(0)

    btc_jpy_bid = BITBANKORDERBOOK['bid'].get('bitbank')

    #XRP/BTCのASKを計算する
    xrp_btc_ask = xrp_jpy_ask / btc_jpy_bid if (xrp_jpy_ask and btc_jpy_bid) else None

    #return
    return xrp_btc_ask



if __name__ == "__main__": #テスト用
    #結果の表示
    print(exchange_xrp_btc_bid(800))
    print(exchange_xrp_btc_ask(80))
