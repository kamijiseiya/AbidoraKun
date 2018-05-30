"""ユーザーのトークンキーをDBに登録する"""
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
        "CREATE TABLE IF NOT EXISTS lline (API_KYE INTEGER PRIMARY KEY)")

    CURSOR.execute(
        "CREATE TABLE IF NOT EXISTS plans (API_KYE INTEGER PRIMARY KEY)")
    #エラー時の処理
except sqlite3.Error as e:
    print('sqlite3.Error occurred:', e.args[0])

ROOT = Tk()
ROOT.title(u"Test")
ROOT.geometry("450x300")

HEAD = Label(text=u'API KEYS')
HEAD.grid(row=0, column=1)
CONTENT = Label(text=u'各SNSからAPIキーを取得してください。')
CONTENT.grid(row=1, column=1)

EXCHANGES = Label(text=u'SNS')
EXCHANGES.grid(row=2, column=0)

APIK = Label(text=u'APIキー')
APIK.grid(row=2, column=1)

SNS = Label(text=u'LINE')
SNS.grid(row=3, column=0)
PLANS = Label(text=u'予定')
PLANS.grid(row=4, column=0)

#エントリー２ (トークンの値を入れる)
LINE_TOKEN = Entry()
LINE_TOKEN.grid(row=3, column=1, padx=20)

PLANS_TOKEN = Entry()
PLANS_TOKEN.grid(row=4, column=1, padx=20)

def Line_Value(entry):
    try:
        #エントリーの中身取得
        LINE_VALUE = LINE_TOKEN.get()
        # INSERT (プレースホルダ使用)
        CURSOR.execute("INSERT INTO lline VALUES (?)", (LINE_VALUE))
        LINE_ENTRY = Label(text=u'line登録しました。')
        LINE_ENTRY.grid(row=5, column=1)
    #例外処理（型の違いや重複）
    except sqlite3.Error as e:
        LINE_ERROR = Label(text=u'line登録されませんでした。')
        LINE_ERROR.grid(row=5, column=1)

#ボタン(bitbank)
BUTTON_LINE = Button(text=u'登録')
BUTTON_LINE.bind("<Button-1>", Line_Value)
BUTTON_LINE.grid(row=3, column=2)

def Plans_Value(entry):
    try:
        #エントリーの中身取得
        PLANS_VALUE = PLANS_TOKEN.get()
        # INSERT (プレースホルダ使用)
        CURSOR.execute("INSERT INTO plans VALUES (?)", (PLANS_VALUE))
        PLANS_ENTRY = Label(text=u'plans登録しました。')
        PLANS_ENTRY.grid(row=6, column=1)
    #例外処理（型の違いや重複）
    except sqlite3.Error as e:
        PLANS_ERROR = Label(text=u'plans登録されませんでした。')
        PLANS_ERROR.grid(row=6, column=1)

#ボタン(binace)
BUTTON_PLANS = Button(text=u'登録')
BUTTON_PLANS.bind("<Button-1>", Plans_Value)
BUTTON_PLANS.grid(row=4, column=2)

#ボタン(メインに戻る用)
MAIN_MENU = Button(text=u'決定')
MAIN_MENU.grid(row=7, column=1)

ROOT.mainloop()

# 保存を実行
CONNECTION.commit()

# 接続を閉じる
CONNECTION.close()
