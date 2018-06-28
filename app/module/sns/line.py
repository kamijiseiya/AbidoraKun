"""ユーザーのトークンキーをDBに登録する"""
# インポート
import sqlite3

# データベースファイルのパス(なければ作られる)
DBPATH = 'cash-cow_db.sqlite'
# データベース接続とカーソル生成
CONNECTION = sqlite3.connect(DBPATH)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
CONNECTION.isolation_level = None
CURSOR = CONNECTION.cursor()


class LINE:
    """"LINEを操作するクラス"""
    def registration(name, apykey):
        """""APIキーを登録するメソッド
        :param apykey:
        :return:
        """
        try:
            # CREATE  (IF NOT EXISTS　は作成済みのテーブルを作るエラーを解消)
            # execute (SQLを実行する)
            CURSOR.execute(
                "CREATE TABLE IF NOT EXISTS line (name TEXT PRIMARY KEY,apykey TEXT)")

            # エラー時の処理
            print(apykey)

            CURSOR.execute('SELECT * FROM Line ORDER BY name')
            # 全件取得は cursor.fetchall()
            res = CURSOR.fetchall()
            print(res)
            return name, apykey
        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])
            return 'none'


if __name__ == "__main__":

    print(LINE.registration('slack', '110asd03dk'))
