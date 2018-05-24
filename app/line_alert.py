"""口座情報をユーザに通知する"""

import time
import requests
import config.TokenSave
from module import exchanges_bitbank

# タイムの繰り返すため
while True:
    BID = exchanges_bitbank.bitbank_bid()  # moduleから呼び出して現在の買い価格取得
    ASK = exchanges_bitbank.bitbank_ask()  # moduleから呼び出して現在の売り価格取得

    URL = "https://notify-api.line.me/api/notify"
    TOKEN = config.TokenSave.Get_Token()  # 別ファイルからアクセストークン取得
    HEADERS = {"Authorization": "Bearer " + TOKEN}  # 転送先を制御する付加情報

    # message LINEに送る値
    MESSAGE = (BID, ASK)
    PARAMS = {"message": MESSAGE}
    print(MESSAGE)  # 取得できれいるかテストするため出力

    requests.post(URL, headers=HEADERS, params=PARAMS)

    # １時間ごとに取得
    time.sleep(3600)
