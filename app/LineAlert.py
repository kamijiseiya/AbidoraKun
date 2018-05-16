#インポート
import time
import requests
import ccxt
import sample.TokenSave
from module import exchanges_binance 

#タイムの繰り返すため
while True:

    bid = __init__.bitbank_bid()
    print (bid)

    url = "https://notify-api.line.me/api/notify"
    token = sample.TokenSave.Get_Token() #別ファイルからアクセストークン取得
    headers = {"Authorization" : "Bearer "+ token} #転送先を制御する付加情報

    #message LINEに送る値
    message = (bitbank_bid, bitbank_ask)
    params = {"message" :  message}

    requests.post(url, headers = headers, params = params)

    #１時間ごとに取得
    time.sleep(3600)
