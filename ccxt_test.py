import ccxt
import time
import datetime

while True:

    #現在の時刻を取得
    print(datetime.datetime.today())

    bitbank = ccxt.bitbank()
    binance = ccxt.binance()
    orderbook = bitbank.fetch_order_book('XRP/JPY')
    orderbook2 = binance.fetch_order_book('XRP/BTC')

    bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
    ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None

    bid2 = orderbook2['bids'][0][0] if len (orderbook2['bids']) > 0 else None
    ask2 = orderbook2['asks'][0][0] if len (orderbook2['asks']) > 0 else None

    spread = (ask - bid) if (bid and ask) else None
    spread2 = (ask2 - bid2) if (bid2 and ask2) else None

    print (bitbank.id, 'market price',{'bank':bid, 'ask':ask, 'spread':spread})
    print (binance.id, 'market price',{'binance':bid2, 'ask2':ask, 'spread':spread})


    print()

    #毎秒取得
    time.sleep(1)
