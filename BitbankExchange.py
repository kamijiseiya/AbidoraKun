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
        jpy_btc_orderbook = bitbank.fetch_order_book('JPY/BTC') #JPY/BTCのオーダーブック取得

        #ASKとBIDを取得
        xrp_jpy_ask = xrp_jpy_orderbook['asks'][0][0] if (xrp_jpy_orderbook['asks']) else None #XRP/JPYのASK
        xrp_jpy_bid = xrp_jpy_orderbook['bids'][0][0] if (xrp_jpy_orderbook['bids']) else None #XRP/JPYのBID
        jpy_btc_ask = jpy_btc_orderbook['asks'][0][0] if (jpy_btc_orderbook['asks']) else None #JPY/BTCのASK
        jpy_btc_bid = jpy_btc_orderbook['bids'][0][0] if (jpy_btc_orderbook['bids']) else None #JPY/BTCのBID

        #XRP/BTCのASK, BIDを計算する
        xrp_btc_ask = (xrp_jpy_ask * jpy_btc_ask) if (xrp_jpy_ask and jpy_btc_ask) else None #XRP/BTCのASK
        xrp_btc_bid = (xrp_jpy_bid * jpy_btc_bid) if (xrp_jpy_bid and jpy_btc_bid) else None #XRP/BTCのBID

        #XRP/BTCのスプレッドを計算する
        xrp_btc_spread = (xrp_btc_ask - xrp_btc_bid) if (xrp_btc_ask and xrp_btc_bid) else None

        #ASK, BID, スプレッドを返す
        xrp_btc = {'bids':xrp_btc_bid, 'asks':xrp_btc_ask, 'spread':xrp_btc_spread} #ASK, BID, スプレッドを連想配列に入れる
        return xrp_btc
