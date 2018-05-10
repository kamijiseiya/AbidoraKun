#インポート
import time
import requests
import ccxt
import sample.TokenSave

#タイムの繰り返すため
while True:

    bitbank = ccxt.bitbank()
    bitbank_orderbook = bitbank.fetch_order_book('XRP/JPY')
    bitbank_bid = bitbank_orderbook['bids'][0][0] if len (bitbank_orderbook['bids']) > 0 else None
    bitbank_ask = bitbank_orderbook['asks'][0][0] if len (bitbank_orderbook['asks']) > 0 else None
    bitbank_spread = (bitbank_ask - bitbank_bid) if (bitbank_bid and bitbank_ask) else None
    print ('bitbank market price', {'bid':bitbank_bid, 'ask':bitbank_ask, 'spread':bitbank_spread})

    url = "https://notify-api.line.me/api/notify"
    token = sample.TokenSave.Get_Token() #別ファイルからアクセストークン取得
    headers = {"Authorization" : "Bearer "+ token} #転送先を制御する付加情報

    #message LINEに送る値
    message = (bitbank_bid, bitbank_ask)
    params = {"message" :  message}

    requests.post(url, headers = headers, params = params)

    #１時間ごとに取得
    time.sleep(3600)
