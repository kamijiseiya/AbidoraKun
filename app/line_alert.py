#インポート
import time
import requests
import ccxt
import config.TokenSave
from module import exchanges_bitbank

#タイムの繰り返すため
while True:

    bid = exchanges_bitbank.bitbank_bid() #moduleから呼び出して現在の買い価格取得
    ask = exchanges_bitbank.bitbank_ask() #moduleから呼び出して現在の売り価格取得

    url = "https://notify-api.line.me/api/notify"
    token = config.TokenSave.Get_Token() #別ファイルからアクセストークン取得
    headers = {"Authorization" : "Bearer "+ token} #転送先を制御する付加情報

    #message LINEに送る値
    message = (bid, ask)
    params = {"message" :  message}
    print (message) #取得できれいるかテストするため出力

    requests.post(url, headers = headers, params = params)

    #１時間ごとに取得
    time.sleep(3600)
