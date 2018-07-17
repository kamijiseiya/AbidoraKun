"""口座情報をユーザに通知する"""
import re  # 正規表現を使用するため
import sqlite3
import time
import requests
from app.module.exchangess import bitbank

# DBの初期設定（接続開始）
DBPATH = 'config/sample_db.sqlite'
CONNECTION = sqlite3.connect(DBPATH)
CURSOR = CONNECTION.cursor()
CURSOR.execute("SELECT API_KYE FROM lline")
GET_TOKEN = CURSOR.fetchone()  # fetchone　一件取得

class LINE_ALERT:
    @staticmethod
    def sql():
        # 正規表現を使用し余計な部分を削除　(),''  str()は数値を文字列に変換
        CURSOR.execute("SELECT API_KYE FROM lline")
        # 正規表現を使用し余計な部分を削除　(),''  str()は数値を文字列に変換
        TOKEN_REWORK = re.sub('\)|\(|\,|\'', '', str(GET_TOKEN))
        return TOKEN_REWORK

    @staticmethod
    def line():
        while True:
            bid = bitbank.BITBANK.xrp(0)  # moduleから呼び出して現在の買い価格取得
            bitbank_bid = bid['bid'].get('bitbank')
            print(bitbank_bid)
            ask = bitbank.BITBANK.xrp(0)  # moduleから呼び出して現在の買い価格取得
            bitbank_ask = ask['ask'].get('bitbank')
            print(bitbank_ask)
            url = "https://notify-api.line.me/api/notify"
            token = (str(LINE_ALERT.sql()))  # DBからアクセストークン取得
            headers = {"Authorization": "Bearer " + token}  # 転送先を制御する付加情報
            # MESSAGE LINEに送る値
            message = (bitbank_bid, bitbank_ask)
            params = {"message": message}
            post = requests.post(url, headers=headers, params=params)
            print(post.status_code)  # ステータスコード取得
            # １時間ごとに取得
            time.sleep(3600)
            return post.status_code

    @staticmethod
    def line_image():
        """Lineに画像を送るためのサンプル"""
        pass

print(LINE_ALERT.line())



