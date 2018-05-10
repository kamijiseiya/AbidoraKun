'''
Bitbankから取得したXRPをBTCに対応させるモジュールです
'''
#インポート
import ccxt
class BitbankExchange:
    '''
    XRPをBTCに対応させるクラスです
    '''
    def exchangeXRP_BTC(self):
        '''
        BitbankからXRP/JPY, JPY/BTCのオーダーブックを取得してXRP/BTCのASK, BID, スプレッドを計算するクラスです
        '''
        #オーダーブック取得
        bitbank = ccxt.bitbank() #bitbankの情報を呼び出す
        xrp_jpy_orderbook = bitbank.fetch_order_book('XRP/JPY') #XRP/JPYのオーダーブック取得
        btc_jpy_orderbook = bitbank.fetch_order_book('BTC/JPY') #BTC/JPYのオーダーブック取得

        #ASKとBIDを取得
        xrp_jpy_ask = xrp_jpy_orderbook['asks'][0][0] if (xrp_jpy_orderbook['asks']) else None #XRP/JPYのASK
        xrp_jpy_bid = xrp_jpy_orderbook['bids'][0][0] if (xrp_jpy_orderbook['bids']) else None #XRP/JPYのBID
        btc_jpy_ask = btc_jpy_orderbook['asks'][0][0] if (btc_jpy_orderbook['asks']) else None #BTC/JPYのASK
        btc_jpy_bid = btc_jpy_orderbook['bids'][0][0] if (btc_jpy_orderbook['bids']) else None #BTC/JPYのBID

        #XRP/BTCのASK, BIDを計算する
        xrp_btc_ask = (xrp_jpy_ask * btc_jpy_bid) if (xrp_jpy_ask and btc_jpy_bid) else None #XRP/BTCのASK
        xrp_btc_bid = (xrp_jpy_bid * btc_jpy_ask) if (xrp_jpy_bid and btc_jpy_ask) else None #XRP/BTCのBID

        #XRP/BTCのスプレッドを計算する
        xrp_btc_spread = (xrp_btc_ask - xrp_btc_bid) if (xrp_btc_ask and xrp_btc_bid) else None

        #ASK, BID, スプレッドを返す
        xrp_btc = {'bids':xrp_btc_bid, 'asks':xrp_btc_ask, 'spread':xrp_btc_spread} #ASK, BID, スプレッドを連想配列に入れる
        return xrp_btc


if __name__ == "__main__": #テスト用
    exchange = BitbankExchange()
    print(exchange.exchangeXRP_BTC()) #xrp_btcの中身を表示する

