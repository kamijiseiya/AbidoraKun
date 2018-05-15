'''
BTCを現金化するときに何円になるか計算するモジュールです
'''
#インポート
import ccxt

def btc_to_jpy(btc):
    '''
    BTCの枚数を引数として受け取り、日本円の金額に変換するメソッドです
    '''
    #BTC/JPYのレートを取得する
    bitbank = ccxt.bitbank() #bitbankの情報を呼び出す
    orderbook = bitbank.fetch_order_book('BTC/JPY') #BTC/JPYのオーダーブック取得
    #BTC/JPYのBIDを取得する
    bid = orderbook['bids'][0][0] if (btc_jpy_orderbook['bids']) else None

    jpy = btc / bid #BTCを日本円の額に変換する
    return jpy