#�C���|�[�g
import ccxt
'''
Bitbank����擾����XRP��BTC�ɑΉ������鏈��������N���X�ł�
'''
class BitbankExchange:
    '''
    XRP/BTC��ASK, BID, �X�v���b�h���v�Z���ĕԂ����\�b�h�ł�
    '''
    def exchangeXRP_BTC:
        #�I�[�_�[�u�b�N�擾
        xrp_jpy_orderbook = bitbank.fetch_order_book('XRP/JPY') #XRP/JPY�̃I�[�_�[�u�b�N�擾
        jpy_btc_orderbook = bitbank.fetch_order_book('JPY/BTC') #JPY/BTC�̃I�[�_�[�u�b�N�擾

        #ASK��BID���擾
        xrp_jpy_ask = xrp_jpy_orderbook['asks'][0][0] if len (xrp_jpy_orderbook['asks']) > 0 else None #XRP/JPY��ASK
        xrp_jpy_bid = xrp_jpy_orderbook['bids'][0][0] if len (xrp_jpy_orderbook['bids']) > 0 else None #XRP/JPY��BID
        jpy_btc_ask = jpy_btc_orderbook['asks'][0][0] if len (jpy_btc_orderbook['asks']) > 0 else None #JPY/BTC��ASK
        jpy_btc_bid = jpy_btc_orderbook['bids'][0][0] if len (jpy_btc_orderbook['bids']) > 0 else None #JPY/BTC��BID

        #XRP/BTC��ASK, BID���v�Z����
        xrp_btc_ask = (xrp_jpy_ask * jpy_btc_ask) if (xrp_jpy_ask and jpy_btc_ask) else None #XRP/BTC��ASK
        xrp_btc_bid = (xrp_jpy_bid * jpy_btc_bid) if (xrp_jpy_bid and jpy_btc_bid) else None #XRP/BTC��BID
        
        #XRP/BTC�̃X�v���b�h���v�Z����
        xrp_btc_spread = (xrp_btc_ask - xrp_btc_bid) if (xrp_btc_ask and xrp_brc_bid) else None
