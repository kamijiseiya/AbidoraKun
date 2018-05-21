'''
Bitbankから取得したXRPをBTCに対応させるモジュールです
'''
#インポート
import exchanges_bitbank

def exchange_xrp_btc_bid(xrp_jpy_bid):
    '''
    XRP/JPYのbidを引数で受け取り、XRP/BTCのbidに変換して返すメソッドです
    '''
    #BTC/JPYのASKを取得する
    btc_jpy_ask = exchanges_bitbank.bitbank_btc_ask()

    #XRP/BTCのBIDを計算する
    xrp_btc_bid = xrp_jpy_bid / btc_jpy_ask if (xrp_jpy_bid and btc_jpy_ask) else None

    #return
    return xrp_btc_bid


def exchange_xrp_btc_ask(xrp_jpy_ask):
    '''
    XRP/JPYのaskを引数で受け取り、XRP/BTCのaskに変換して返すメソッドです
    '''
    #BTC/JPYのBIDを取得する
    btc_jpy_bid = exchanges_bitbank.bitbank_btc_bid()

    #XRP/BTCのASKを計算する
    xrp_btc_ask = xrp_jpy_ask / btc_jpy_bid if (xrp_jpy_ask and btc_jpy_bid) else None

    #return
    return xrp_btc_ask


if __name__ == "__main__": #テスト用
    #結果の表示
    print(exchange_xrp_btc_bid(80))
    print(exchange_xrp_btc_ask(80))
