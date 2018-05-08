import requests
import ccxt
import time
import datetime

#タイムの繰り返すため
while True:

    bitbank = ccxt.bitbank()
    bitbank_orderbook = bitbank.fetch_order_book('XRP/JPY')
    bitbank_bid = bitbank_orderbook['bids'][0][0] if len (bitbank_orderbook['bids']) > 0 else None
    bitbank_ask = bitbank_orderbook['asks'][0][0] if len (bitbank_orderbook['asks']) > 0 else None
    bitbank_spread = (bitbank_ask - bitbank_bid) if (bitbank_bid and bitbank_ask) else None
    print (bitbank.id, 'market price',{'bitbank':bitbank_bid, 'ask':bitbank_ask, 'spread':bitbank_spread})

    url = "https://notify-api.line.me/api/notify"
    token = 'P0pE1muSVOPghHYIHKGzpFRVo52VZCAhuK8r0gXuyr9' #アクセストークン
    headers = {"Authorization" : "Bearer "+ token}

    #bid 売り時の値段　ask　買う時の値段
    message = (bitbank_bid,bitbank_ask)
    #message LINEに送る値
    payload = {"message" :  message}

    r = requests.post(url ,headers = headers , params=payload)


    #１時間ごとに取得
    time.sleep(3600)
