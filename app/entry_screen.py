"""ユーザーのAPIキーをDBに登録する"""
#インポート
import sqlite3
from tkinter import Tk, Label, Entry, END, Button

# データベースファイルのパス(なければ作られる)
DBPATH = 'config/sample_db.sqlite'

# データベース接続とカーソル生成
CONNECTION = sqlite3.connect(DBPATH)
# 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
# connection.isolation_level = None
CURSOR = CONNECTION.cursor()

try:
    # CREATE  (IF NOT EXISTS　は作成済みのテーブルを作るエラーを解消)
    # execute (SQLを実行する)
    CURSOR.execute(
        "CREATE TABLE IF NOT EXISTS bitbank (Private INTEGER PRIMARY KEY, Token TEXT)")

    CURSOR.execute(
        "CREATE TABLE IF NOT EXISTS binace (Private INTEGER PRIMARY KEY, Token TEXT)")
    #エラー時の処理
except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

ROOT = Tk()
ROOT.title(u"Test")
ROOT.geometry("450x300")

HEAD = Label(text=u'API KEYS')
HEAD.grid(row=0, column=1)
CONTENT = Label(text=u'各取引所からAPIキーを取得してください。')
CONTENT.grid(row=1, column=1)

EXCHANGES = Label(text=u'取引所')
EXCHANGES.grid(row=2, column=0)

APIK = Label(text=u'APIキー')
APIK.grid(row=2, column=1)

TOKEN = Label(text=u'トークンキー')
TOKEN.grid(row=2, column=2)

BANK = Label(text=u'bitbank')
BANK.grid(row=3, column=0)
BINA = Label(text=u'binace')
BINA.grid(row=4, column=0)

#エントリー　（privateキーの値を入れる)
BITBANK_API = Entry()
BITBANK_API.grid(row=3, column=1, padx=15)

BINACE_API = Entry()
BINACE_API.grid(row=4, column=1, padx=15)

#エントリー２ (トークンの値を入れる)
BITBANK_TOKEN = Entry()
BITBANK_TOKEN.insert(END, "トークンの値")
BITBANK_TOKEN.grid(row=3, column=2, padx=20)

BINACE_TOKEN = Entry()
BINACE_TOKEN.insert(END, "トークンの値")
BINACE_TOKEN.grid(row=4, column=2, padx=20)

def Bitbank_Value(entry):
    #エントリーの中身取得
    BITBANK_VALUE_API = BITBANK_API.get()
    BITBANK_VALUE_TOKEN = BITBANK_TOKEN.get()
    # INSERT (プレースホルダ使用)
    CURSOR.execute("INSERT INTO bitbank VALUES (?, ?)", (BITBANK_VALUE_API, BITBANK_VALUE_TOKEN))
    BITBANK_ENTRY = Label(text=u'bitbank登録しました。')
    BITBANK_ENTRY.grid(row=5, column=1)


#ボタン(bitbank)
BUTTON_BITBANK = Button(text=u'登録')
BUTTON_BITBANK.bind("<Button-1>", Bitbank_Value)
BUTTON_BITBANK.grid(row=3, column=4)

def Binance_Value(entry):
    #エントリーの中身取得
    BINACE_VALUE_API = BINACE_API.get()
    BINACE_VALUE_TOKEN = BINACE_TOKEN.get()
    # INSERT (プレースホルダ使用)
    CURSOR.execute("INSERT INTO binace VALUES (?, ?)", (BINACE_VALUE_API, BINACE_VALUE_TOKEN))
    BINACE_ENTRY = Label(text=u'binace登録しました。')
    BINACE_ENTRY.grid(row=6, column=1)

#ボタン(binace)
BUTTON_BINACE = Button(text=u'登録')
BUTTON_BINACE.bind("<Button-1>", Binance_Value)
BUTTON_BINACE.grid(row=4, column=4)

#ボタン(メインに戻る用)
MAIN_MENU = Button(text=u'決定')
MAIN_MENU.grid(row=7, column=1)

ROOT.mainloop()

# 保存を実行
CONNECTION.commit()

# 接続を閉じる
CONNECTION.close()
