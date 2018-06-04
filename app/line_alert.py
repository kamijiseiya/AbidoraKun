"""口座情報をユーザに通知する"""

import re # 正規表現を使用するため
import sqlite3
import time
import requests
import module

# データベースファイルのパス
DBPATH = 'config/sample_db.sqlite'

CONNECTION = sqlite3.connect(DBPATH)
CURSOR = CONNECTION.cursor()

CURSOR.execute("SELECT API_KYE FROM lline")
GET_TOKEN = CURSOR.fetchone() # fetchone　一件取得
#正規表現を使用し余計な部分を削除　(),''  str()は数値を文字列に変換
TOKEN_REWORK = re.sub('\)|\(|\,|\'', '', str(GET_TOKEN))
print (TOKEN_REWORK)


# タイムの繰り返すため
while True:
    BID = module.exchanges.bitbank.xrp(0)  # moduleから呼び出して現在の買い価格取得
    BITBANK_BID = BID['bid'].get('bitbank')
    print (BITBANK_BID)

    ASK = module.exchanges.bitbank.xrp(0)  # moduleから呼び出して現在の買い価格取得
    BITBANK_ASK = ASK['ask'].get('bitbank')
    print (BITBANK_ASK)

    URL = "https://notify-api.line.me/api/notify"
    TOKEN = (str(TOKEN_REWORK))  # DBからアクセストークン取得
    HEADERS = {"Authorization": "Bearer " + TOKEN}  # 転送先を制御する付加情報

    # MESSAGE LINEに送る値
    MESSAGE = (BITBANK_BID, BITBANK_ASK)
    PARAMS = {"message": MESSAGE}

    R = requests.post(URL, headers=HEADERS, params=PARAMS)
    print (R.status_code) #ステータスコード取得

    # １時間ごとに取得
    time.sleep(3600)
