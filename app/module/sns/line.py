"""" LINEを操作するモジュール"""
# Python 3.5.2 にて動作を確認
# sqlite3 標準モジュールをインポート
import sqlite3
import requests
import re  # 正規表現を使用するため

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

            # 保存を実行（忘れると保存されないので注意）
            CONNECTION.commit()
            # 接続を閉じる
            CONNECTION.close()
            # 登録された値を返す
            return api, name
        except sqlite3.Error as error:
            print('sqlite3.Error occurred:', error.args[0])
            return None

    def search_apykey(name):
        try:
            CURSOR.execute("SELECT api FROM sns where  name like" + "'"+name+"'")
            """正規表現で形を整える"""
            TOKEN_REWORK = re.sub('\)|\(|\,|\'', '', str(CURSOR.fetchall()))
            print(TOKEN_REWORK)
            CONNECTION.close()
            return TOKEN_REWORK
        except sqlite3.Error as error:
            print('sqlite3.Error occurred:', error.args[0])
        return None
if __name__ == "__main__":  # テスト用に追加
    #print(LINE.registration('test','0001'))
    print(LINE.search_apykey('test'))
    #print(LINE.search_apykey('test'))
