#ライブラリーはPythonで標準にあるtkinterを使用

#インポート
import sqlite3
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
        "CREATE TABLE IF NOT EXISTS bitbank (Private INTEGER PRIMARY KEY, Token TEXT)")

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS binace (Private INTEGER PRIMARY KEY, Token TEXT)")
    #エラー時の処理
except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

root = Tk()
root.title(u"Test")
root.geometry("450x300")

head = Label(text=u'API KEYS')
head.grid(row=0, column=1)
cond = Label(text=u'各取引所からAPIキーを取得してください。')
cond.grid(row=1, column=1)

tori = Label(text=u'取引所')
tori.grid(row=2, column=0)

apik = Label(text=u'APIキー')
apik.grid(row=2, column=1)

tokn = Label(text=u'トークンキー')
tokn.grid(row=2, column=2)

bank = Label(text=u'bitbank')
bank.grid(row=3, column=0)
bina = Label(text=u'binace')
bina.grid(row=4, column=0)

#エントリー　（privateキーの値を入れる)
bitbank_api = Entry()
bitbank_api.grid(row=3, column=1, padx=15)

binace_api = Entry()
binace_api.grid(row=4, column=1, padx=15)

#エントリー２ (トークンの値を入れる)
bitbank_token = Entry()
bitbank_token.insert(END,"トークンの値")
bitbank_token.grid(row=3, column=2, padx=20)

binace_token = Entry()
binace_token.insert(END,"トークンの値")
binace_token.grid(row=4, column=2, padx=20)

def Bitbank_Value(event):
    #エントリーの中身取得
    API_value = bitbank_api.get()
    token_value = bitbank_token.get()
    # INSERT (プレースホルダ使用)
    cursor.execute("INSERT INTO bitbank VALUES (?, ?)", (API_value, token_value))
    th = Label(text=u'bitbank登録しました。')
    th.grid(row=5, column=1)


#ボタン(bitbank)
Button_bitbank = Button(text=u'登録')
Button_bitbank.bind("<Button-1>",Bitbank_Value)
Button_bitbank.grid(row=3, column=4)

def Binance_Value(event):
    #エントリーの中身取得
    API_value = binace_api.get()
    token_value = binace_token.get()
    # INSERT (プレースホルダ使用)
    cursor.execute("INSERT INTO binace VALUES (?, ?)", (API_value, token_value))
    th.grid(row=6, column=1)

#ボタン(binace)
Button_binace = Button(text=u'登録')
Button_binace.bind("<Button-1>",Binance_Value)
Button_binace.grid(row=4, column=4)

#ボタン(メインに戻る用)
Main_Menu = Button(text=u'決定')
Main_Menu.grid(row=7, column=1)

root.mainloop()

# 保存を実行
connection.commit()

# 接続を閉じる
connection.close()
