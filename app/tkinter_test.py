#ライブラリーはPythonで標準にあるtkinterを使用

#インポート
import sqlite3
import sys
from tkinter import *
from tkinter import ttk

# データベースファイルのパス(なければ作られる)
dbpath = 'config/sample_db.sqlite'

# データベース接続とカーソル生成
connection = sqlite3.connect(dbpath)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
cursor = connection.cursor()

try:
    # CREATE  (IF NOT EXISTS　は作成済みのテーブルを作るエラーを解消)
    # execute (SQLを実行する)
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS sample (Private INTEGER PRIMARY KEY, Token TEXT)")

#エラー時の処理
except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

root = Tk()
root.title(u"Test")
root.geometry("400x300")

#メソッド（ボタン)
def ButtonValue(event):
    #エントリーの中身取得
    Edit_value = EditBox.get()
    Box_value = Box.get()
    # INSERT (プレースホルダ使用)
    cursor.execute("INSERT INTO sample VALUES (?, ?)", (Edit_value, Box_value))
    th = Label(text=Edit_value)
    th.pack()


#エントリー　（privateキーの値を入れる)
EditBox = Entry()
EditBox.pack()

#エントリー２ (トークンの値を入れる)
Box = Entry()
Box.insert(END,"トークンの値")
Box.pack()

#ボタン
Button = Button(text=u'登録')
Button.bind("<Button-1>",ButtonValue)
Button.pack()

root.mainloop()

# 保存を実行
connection.commit()

# 接続を閉じる
connection.close()
