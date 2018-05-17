#ライブラリーはPythonで標準にあるtkinterを使用

#インポート
import sys
from tkinter import *
from tkinter import ttk

root = Tk()
root.title(u"Test")
root.geometry("400x300")

#メソッド（ボタン)
def ButtonValue(event):
    #エントリーの中身出力
    value = EditBox.get()
    th = Label(text=value)
    th.pack()

#ラベル　色と場所指定サンプル
Static1 = Label(text=u'test', foreground='#ff0000', background='#ffaacc')
Static1.place(x=150, y=228)

#エントリー
EditBox = Entry()
EditBox.pack()

#ボタン
Button = Button(text=u'登録')
Button.bind("<Button-1>",ButtonValue)
Button.pack()

root.mainloop()
