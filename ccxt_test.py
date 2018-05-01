import ccxt

binance = ccxt.binance()
orderbook = binance.fetch_order_book('XRP/BTC')
bid = orderbook['bids'][0][0] if len (orderbook['bids']) > 0 else None
ask = orderbook['asks'][0][0] if len (orderbook['asks']) > 0 else None
spread = (ask - bid) if (bid and ask) else None
print (binance.id, 'market price',{'bid':bid, 'ask':ask, 'spread':spread})
