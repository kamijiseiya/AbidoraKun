'''
Bitbankから取得したXRPをBTCに対応させるモジュールです
'''
#インポート
import ccxt

def exchange_xrp_btc_bid(xrp_jpy_bid):
    '''
    XRP/JPYのbidを引数で受け取り、XRP/BTCのbidに変換して返すメソッドです
    '''
    #オーダーブック取得
    bitbank = ccxt.bitbank() #bitbankの情報を呼び出す
    btc_jpy_orderbook = bitbank.fetch_order_book('BTC/JPY') #BTC/JPYのオーダーブック取得

    #BTC/JPYのASKを取得する
    btc_jpy_ask = btc_jpy_orderbook['asks'][0][0] if (btc_jpy_orderbook['asks']) else None

    #XRP/BTCのBIDを計算する
    xrp_btc_bid = xrp_jpy_bid / btc_jpy_ask if (xrp_jpy_bid and btc_jpy_ask) else None

    #return
    return xrp_btc_bid


def exchange_xrp_btc_ask(xrp_jpy_ask):
    '''
    XRP/JPYのaskを引数で受け取り、XRP/BTCのaskに変換して返すメソッドです
    '''
    #オーダーブック取得
    bitbank = ccxt.bitbank() #bitbankの情報を呼び出す
    btc_jpy_orderbook = bitbank.fetch_order_book('BTC/JPY') #BTC/JPYのオーダーブック取得

    #BTC/JPYのBIDを取得する
    btc_jpy_bid = btc_jpy_orderbook['bids'][0][0] if (btc_jpy_orderbook['bids']) else None

    #XRP/BTCのASKを計算する
    xrp_btc_ask = xrp_jpy_ask / btc_jpy_bid if (xrp_jpy_ask and btc_jpy_bid) else None

    #return
    return xrp_btc_ask


if __name__ == "__main__": #テスト用
    #結果の表示
    print(exchange_xrp_btc_bid(80))
    print(exchange_xrp_btc_ask(80))
