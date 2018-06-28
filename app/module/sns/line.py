# Python 3.5.2 にて動作を確認
# sqlite3 標準モジュールをインポート
import sqlite3

# データベースファイルのパス
DBPATH = 'sample_db.sqlite'

# データベース接続とカーソル生成
CONNECTION = sqlite3.connect(DBPATH)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
CURSOR = CONNECTION.cursor()


# エラー処理（例外処理）
class LINE:

    def registration(name, api):
        try:

            CURSOR.execute("DROP TABLE IF EXISTS sample")
            CURSOR.execute(
                "CREATE TABLE IF NOT EXISTS sample (name TEXT PRIMARY KEY, api TEXT)")
            # INSERT
            CURSOR.execute("INSERT INTO sample VALUES (:name, :api)",
                           {'name': name, 'api':  api})
            # プレースホルダの使用例
            # プレースホルダには疑問符(qmark スタイル)と名前(named スタイル)の2つの方法がある
            # 1つの場合には最後に , がないとエラー。('鈴木') ではなく ('鈴木',)
            CURSOR.execute("INSERT INTO sample VALUES ('LINE', 'kpksdkふぉsじょそぼsmvsd「')")
            # 保存を実行（忘れると保存されないので注意）
            CONNECTION.commit()
            # 接続を閉じる
            CONNECTION.close()
            return api, name
        except sqlite3.Error as e:
            print('sqlite3.Error occurred:', e.args[0])
            return 'none'


if __name__ == "__main__":  # テスト用に追加
    print(LINE.registration('slack' , '上地'))
