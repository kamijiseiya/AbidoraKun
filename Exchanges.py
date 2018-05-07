import ccxt
import time
import datetime

#タイムの繰り返すため
while True:

    #現在の時刻を取得
    print(datetime.datetime.today())

    bitbank = ccxt.bitbank()
    binance = ccxt.binance()
    bitbank_orderbook = bitbank.fetch_order_book('XRP/JPY')
    binance_orderbook = binance.fetch_order_book('XRP/BTC')

    bitbank_bid = bitbank_orderbook['bids'][0][0] if len (bitbank_orderbook['bids']) > 0 else None
    bitbank_ask = bitbank_orderbook['asks'][0][0] if len (bitbank_orderbook['asks']) > 0 else None

    binance_bid = binance_orderbook['bids'][0][0] if len (binance_orderbook['bids']) > 0 else None
    binance_ask = binance_orderbook['asks'][0][0] if len (binance_orderbook['asks']) > 0 else None

    bitbank_spread = (bitbank_ask - bitbank_bid) if (bitbank_bid and bitbank_ask) else None
    binance_spread = (binance_ask - binance_bid) if (binance_bid and binance_ask) else None

    print (bitbank.id, 'market price',{'bitbank':bitbank_bid, 'ask':bitbank_ask, 'spread':bitbank_spread})
    print (binance.id, 'market price',{'binance':binance_bid, 'ask':binance_ask, 'spread':binance_spread})

    #プリント時見やすくするため
    print()

    #毎秒取得
    time.sleep(1)
