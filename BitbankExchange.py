#インポート
import ccxt
'''
Bitbankから取得したXRPをBTCに対応させる処理をするクラスです
'''
class BitbankExchange:
    '''
    XRP/BTCのASK, BID, スプレッドを計算して返すメソッドです
    '''
    def exchangeXRP_BTC:
        #オーダーブック取得
        xrp_jpy_orderbook = bitbank.fetch_order_book('XRP/JPY') #XRP/JPYのオーダーブック取得
        jpy_btc_orderbook = bitbank.fetch_order_book('JPY/BTC') #JPY/BTCのオーダーブック取得

        #ASKとBIDを取得
        xrp_jpy_ask = xrp_jpy_orderbook['asks'][0][0] if len (xrp_jpy_orderbook['asks']) > 0 else None #XRP/JPYのASK
        xrp_jpy_bid = xrp_jpy_orderbook['bids'][0][0] if len (xrp_jpy_orderbook['bids']) > 0 else None #XRP/JPYのBID
        jpy_btc_ask = jpy_btc_orderbook['asks'][0][0] if len (jpy_btc_orderbook['asks']) > 0 else None #JPY/BTCのASK
        jpy_btc_bid = jpy_btc_orderbook['bids'][0][0] if len (jpy_btc_orderbook['bids']) > 0 else None #JPY/BTCのBID

        #XRP/BTCのASK, BIDを計算する
        xrp_btc_ask = (xrp_jpy_ask * jpy_btc_ask) if (xrp_jpy_ask and jpy_btc_ask) else None #XRP/BTCのASK
        xrp_btc_bid = (xrp_jpy_bid * jpy_btc_bid) if (xrp_jpy_bid and jpy_btc_bid) else None #XRP/BTCのBID
        
        #XRP/BTCのスプレッドを計算する
        xrp_btc_spread = (xrp_btc_ask - xrp_btc_bid) if (xrp_btc_ask and xrp_brc_bid) else None

        #ASK, BID, スプレッドを返す
        xrp_btc = {'bids':xrp_btc_bid, 'asks':xrp_btc_ask, 'spread':xrp_btc_spread} #ASK, BID, スプレッドを連想配列に入れる
        return xrp_btc
