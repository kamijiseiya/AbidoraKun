"""" LINEを操作するモジュール"""
# Python 3.5.2 にて動作を確認
# sqlite3 標準モジュールをインポート
import sqlite3
import requests
import time

# データベースファイルのパス
DBPATH = 'cash_cow_db.sqlite'

# データベース接続とカーソル生成
CONNECTION = sqlite3.connect(DBPATH)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
CONNECTION.isolation_level = None
CURSOR = CONNECTION.cursor()


# エラー処理（例外処理）

class LINE:
    """" LINEを操作するクラス"""

    def registration(name, api):
        """" APIkキーを登録するメソッド"""
        try:


            CURSOR.execute(
                "CREATE TABLE IF NOT EXISTS sns (name TEXT PRIMARY KEY, api TEXT)")
            # INSERT
            CURSOR.execute("INSERT INTO sns VALUES (:name, :api)",
                           {'name': name, 'api': api})
            CURSOR.execute('SELECT * FROM sns ORDER BY name')
            res = CURSOR.fetchall()

            # 保存を実行（忘れると保存されないので注意）
            CONNECTION.commit()
            # 接続を閉じる
            CONNECTION.close()
            # 登録された値を返す
            return api, name
        except sqlite3.Error as error:
            print('sqlite3.Error occurred:', error.args[0])
            return 'none'

    def search_apykey(name):
        try:
            CURSOR.execute("SELECT api FROM sns where  name like" + "'"+name+"'")

            res = CURSOR.fetchall()
            print(res)
            CONNECTION.close()
            return res
        except sqlite3.Error as error:
            print('sqlite3.Error occurred:', error.args[0])
        return 'none'


    @staticmethod
    def line_image():
        """Lineに画像を送るためのサンプル"""
        while True:
            url = "https://notify-api.line.me/api/notify"
            token = 'LINE Notifyのアクセストークン'  # DBから取得予定
            headers = {"Authorization": "Bearer " + token}
            message = ("今から画像を送ります。")
            params = {"message": message}
            files = {"imageFile": open("../../../img/sample.jpg", "rb")}
            post = requests.post(url, headers=headers, params=params, files=files)
            print(post.status_code)  # ステータスコード取得
            # １時間ごとに取得
            time.sleep(3600)
            return post.status_code


if __name__ == "__main__":  # テスト用に追加
    #print(LINE.registration('test','0001'))
    print(LINE.search_apykey('test'))
