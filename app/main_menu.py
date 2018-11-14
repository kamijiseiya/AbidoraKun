"""メイン画面"""
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
import subprocess

sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
# ライブラリ
import tkinter
from tkinter import ttk
import time  # 価格取得を繰り返す為
import sqlite3  # DBへの追加時のエラーを取得する為

from app.module.exchangess import bitbank
from app.module.exchangess import binance
# from app.module.sns import line
from app import xrpchart

import matplotlib

matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
from matplotlib.figure import Figure

from time import sleep

# startボタンを押したときの処理
def changePage(page):
    # MainPageを上位層にする
    page.tkraise()


def main() -> None:
    # インスタンス生成
    window = tkinter.Tk()

    # ウィンドウタイトルを決定
    window.title("メインメニュー")

    # ウィンドウの大きさを決定
    window.geometry("1500x1000")

    # ウィンドウのグリッドを 1x1 にする
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    # -----------------------------------StartPage---------------------------------
    ### StartPage用のFrameを生成
    startpage = ttk.Frame(window)
    #starttest = tkinter.Frame(startpage, height=200, width=300, relief="groove")
    starttest = tkinter.Frame(startpage, bg='black', width=300, height=200, bd=30, relief="groove")
    backpage = tkinter.Frame(startpage, bg='black', height=400, width=330, bd=10, relief="ridge")
    badpage = tkinter.Frame(backpage, height=320, width=330, bg='white')
    #canvass = tkinter.Canvas(backpage, height=100, width=50)
    canvass = tkinter.Canvas(backpage, height=350, width=290, bg='gray')

    bar = tkinter.Scrollbar(backpage, orient=tkinter.VERTICAL)
    bar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    bar.config(command=canvass.yview)

    canvass.config(yscrollcommand=bar.set)
    canvass.config(scrollregion=(0,0,400,500))
    canvass.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

    scrollframe = tkinter.Frame(canvass, bg='gray')

    canvass.create_window((0,0), window=scrollframe, anchor=tkinter.NW, width=canvass.cget('width'))

    button=[]
    for i in range(30):
        bt = tkinter.Label(scrollframe, text="")
        button.append(bt)
        bt.pack(fill=tkinter.X)

    bidpage = tkinter.Frame(startpage,  height=50, width=330, bd=10, relief="ridge")
    orderpage = tkinter.Frame(startpage, bg='black', height=305, width=330, relief="ridge", bd=10)
    #askpage = tkinter.Frame(startpage, bg='black', height=175, width=330, bd=10, relief="ridge")
    tablepage = tkinter.Frame(startpage, bg='black', width=1010, height=400, bd=15, relief="sunken")
    ordercanvas = tkinter.Canvas(orderpage, height=270, width=290)

    orderbar = tkinter.Scrollbar(orderpage, orient=tkinter.VERTICAL)
    orderbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    orderbar.config(command=ordercanvas.yview)

    ordercanvas.config(yscrollcommand=orderbar.set)
    ordercanvas.config(scrollregion=(0,0,400,500))
    ordercanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

    orderframe = tkinter.Frame(ordercanvas, bg='gray')

    ordercanvas.create_window((0,0), window=orderframe, anchor=tkinter.NW, width=ordercanvas.cget('width'))

    test=[]
    for n in range(30):
        tes = tkinter.Label(orderframe, text="")
        test.append(tes)
        tes.pack(fill=tkinter.X)

    PointFont = ("Helevetice", 14)
    PointFont2 = ("", 11)

    exchangeA = ttk.Label(scrollframe, text=u"bitbank", font=PointFont)
    exchangeA.place(relx=0.1, rely=0.15)
    exchangeC = ttk.Label(scrollframe, text=u"binance", font=PointFont)
    exchangeC.place(relx=0.1, rely=0.2)

    ordertest =ttk.Label(orderframe, text=u'bitbank', font=PointFont)
    ordertest.place(relx=0.1, rely=0.02)

    class Helmholtz_App(tkinter.Tk):
        def __init__(self):

            container = tkinter.Frame(tablepage)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}

            for F in (PageOne, PageTwo):
                frame = F(container, self)

                self.frames[F] = frame

                frame.grid(row=0, column=0, sticky="nsew")

            self.show_frame(PageOne)

        def show_frame(self, cont):
            frame = self.frames[cont]
            frame.tkraise()

    class PageOne(tkinter.Frame):
        def __init__(self, parent, controller):
            tkinter.Frame.__init__(self, parent)

            fig1 = Figure(figsize=(4, 4), dpi=170)
            a = fig1.add_subplot(111)

            # 表を作る
            def callback():
                xrpchart.candlechart()

                canvas = FigureCanvasTkAgg(fig1, self)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)

                toolbar = NavigationToolbar2TkAgg(canvas, self)
                toolbar.update()
                canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

                # 作った表を消す
                def ClearCallback():
                    # ~~~~~~~~~~~
                    fig1.clf()
                    # ~~~~~~~~~~~
                    clearbutton.destroy()

                clearbutton = ttk.Button(tablepage, text="Clear", command=ClearCallback)
                clearbutton.pack()

            b = ttk.Button(tablepage, text="Plot Data", command=callback)
            b.pack()

            def uge():
                callback()
                window.after(1000, uge())

    class PageTwo(tkinter.Frame):
        def __init__(self, parent, controller):
            tkinter.Frame.__init__(self, parent)

    app = Helmholtz_App()
    #xrpchart.candlechart()

    def Chart() :
        subprocess.check_call({"python","app.xrpchart.py"})
        #os.system("start python app\\xrpchart.py")
        #os.system("start notepad.exe")

    cart = chartbutton = \
        tkinter.Button(tablepage, text="CHART", command=Chart)
    cart.pack()

    ### ボタン表示
    # APIキー登録ボタン生成
    startbutton = \
        tkinter.Button(starttest, width=31, height=3, text="取引所設定", font=PointFont,
                       command=lambda: changePage(mainPage))

    # expand 親に合わせて変化　fill frameの空きスペースを埋めるか
    startbutton.pack(side="left", expand=1, fill="both")

    # SNSボタン生成
    linebutton = \
        tkinter.Button(starttest, width=31, height=3, text="通知設定", font=PointFont, command=lambda: changePage(snspage))

    linebutton.pack(side="left", expand=1, fill="both")

    # 設定ボタン生成
    configbutton = \
        tkinter.Button(starttest, width=31, height=3, text="詳細設定", font=PointFont, command=lambda: changePage(configPage))

    configbutton.pack(side="left", expand=1, fill="both")

    def Getxrp() :
        # bitbankから現在価格取得
        exhanges, ask, bid = bitbank.BITBANK.currencyinformation('XRP')
        bitbank_ask = ttk.Label(scrollframe, text=ask, font=PointFont)
        bitbank_ask.place(relx=0.4, rely=0.15)
        bitbank_ask.update()
        bitbank_bid = ttk.Label(scrollframe, text=bid, font=PointFont)
        bitbank_bid.place(relx=0.7, rely=0.15)
        bitbank_bid.update()
        # binanseから現在価格取得
        exchange2, ask2, bid2 = binance.BINANCE.currencyinformation('XRP')
        binance_ask = ttk.Label(scrollframe, text=ask2, font=PointFont)
        binance_ask.place(relx=0.4, rely=0.2)
        binance_ask.update()
        binance_bid = ttk.Label(scrollframe, text=bid2, font=PointFont)
        binance_bid.place(relx=0.7, rely=0.2)
        binance_bid.update()

    xrp = tkinter.Button(backpage, text="XRP", width=7, font=PointFont, command=Getxrp)
    xrp.place(relx=0.0, rely=0.0)

    def Getbtc() :
        # bitbankから現在価格取得
        exhanges, ask, bid = bitbank.BITBANK.currencyinformation('BTC')
        bitbank_ask = ttk.Label(scrollframe, text=ask, font=PointFont)
        bitbank_ask.place(relx=0.4, rely=0.15)
        bitbank_ask.update()
        bitbank_bid = ttk.Label(scrollframe, text=bid, font=PointFont)
        bitbank_bid.place(relx=0.7, rely=0.15)
        bitbank_bid.update()
        # binanseから現在価格取得
        exchange2, ask2, bid2 = binance.BINANCE.currencyinformation('BTC')
        binance_ask = ttk.Label(scrollframe, text=ask2, font=PointFont)
        binance_ask.place(relx=0.4, rely=0.2)
        binance_ask.update()
        binance_bid = ttk.Label(scrollframe, text=bid2, font=PointFont)
        binance_bid.place(relx=0.7, rely=0.2)
        binance_bid.update()

    bitbankbutton = tkinter.Button(backpage, text="BTC", font=PointFont, width=7, command=Getbtc)
    bitbankbutton.place(relx=0.25, rely=0.0)

    def Geteth() :
        # bitbankから現在価格取得
        exhanges, ask, bid = bitbank.BITBANK.currencyinformation('ETH')
        bitbank_ask = ttk.Label(scrollframe, text=ask, foreground='white', background='black', font=PointFont)
        bitbank_ask.place(relx=0.4, rely=0.2)
        bitbank_ask.update()
        bitbank_bid = ttk.Label(scrollframe, text=bid, foreground='white', background='black', font=PointFont)
        bitbank_bid.place(relx=0.7, rely=0.2)
        bitbank_bid.update()
        # binanseから現在価格取得
        exchange2, ask2, bid2 = binance.BINANCE.currencyinformation('ETH')
        binance_ask = ttk.Label(scrollframe, text=ask2, foreground='white', background='black', font=PointFont)
        binance_ask.place(relx=0.4, rely=0.3)
        binance_ask.update()
        binance_bid = ttk.Label(scrollframe, text=bid2, foreground='white', background='black', font=PointFont)
        binance_bid.place(relx=0.7, rely=0.3)
        binance_bid.update()

    eth = tkinter.Button(backpage, text="ETH", font=PointFont, width=7, command=Geteth)
    eth.place(relx=0.5, rely=0.0)
    ltc = tkinter.Button(backpage, text="LTC", font=PointFont, width=7)
    ltc.place(relx=0.75, rely=0.0)

    exchange = ttk.Label(backpage, text=u"取引所", font=PointFont)
    exchange.place(relx=0.1, rely=0.12)
    bid = ttk.Label(backpage, text=u'買値', font=PointFont)
    bid.place(relx=0.4, rely=0.12)
    ask = ttk.Label(backpage, text=u'売値', font=PointFont)
    ask.place(relx=0.7, rely=0.12)
    #exchangeA = ttk.Label(backpage, text=u"bitbank", font=PointFont)
    #exchangeA.place(relx=0.1, rely=0.2)
    #exchangeB = ttk.Label(backpage, text=u"binance", font=PointFont)
    #exchangeB.place(relx=0.1, rely=0.3)

    #buy_order = ttk.Label(bidpage, text=u"買い注文", foreground='white', background='black', font=PointFont)
    #buy_order.place(relx=0.4, rely=0.1)
    #sell_order = ttk.Label(askpage, text=u"売り注文", foreground='white', background='black', font=PointFont)
    #sell_order.place(relx=0.4, rely=0.1)

    orderexchange = ttk.Label(bidpage, text=u'取引所', font=PointFont)
    orderexchange.place(relx=0.1, rely=0.1)
    orderstatus = ttk.Label(bidpage, text=u'注文状態', font=PointFont)
    orderstatus.place(relx=0.4, rely=0.1)
    orderprice = ttk.Label(bidpage, text=u'注文価格', font=PointFont)
    orderprice.place(relx=0.7, rely=0.1)

    # フレームを配置
    startpage.grid(row=0, column=0, sticky="nsew")
    starttest.place(relx=0.01, rely=0.01)
    backpage.place(relx=0.75, rely=0.01)
    badpage.place(relx=0.0, rely=0.1)
    bidpage.place(relx=0.75, rely=0.5)
    #askpage.place(relx=0.75, rely=0.75)
    tablepage.place(relx=0.01, rely=0.19)
    #canvass.place(relx=0.01, rely=0.01)
    canvass.pack()
    orderpage.place(relx=0.75, rely=0.555)
    ordercanvas.pack()
    #scrollframe.place(relx=0.01, rely=0.01)

    # -----------------------------------MainPage---------------------------------
    ### MainPage用のFrameを生成
    mainPage = tkinter.Frame(window)

    # 別ファイルから読み込み実行
    # exec(open("./entry.py",'r',encoding="utf-8").read())
    side = ("", 32)

    titlepage = tkinter.Frame(mainPage, bg='gray', width=1340, height=250, bd=10)
    mainpage = tkinter.Frame(mainPage, bg='gray', width=1340, height=450, bd=10)
    # Page = tkinter.Frame(startPage, bg='black', width=1010, height=400, bd=15, relief="sunken")


    # 以下、entry_screenを流用
    head = tkinter.Label(titlepage, text=u'API KEYS', foreground='white', background='gray', font=("", 40))
    head.place(relx=0.01, rely=0.01)
    content = tkinter.Label(titlepage, text=u'各取引所からAPIキーを取得してください。', foreground='white', background='gray',
                            font=("", 25))
    content.place(relx=0.15, rely=0.3)

    exchange = tkinter.Label(mainpage, text=u'取引所', foreground='white', background='gray', font=side)
    exchange.place(relx=0.015, rely=0.01)

    apik = tkinter.Label(mainpage, text=u'APIキー', foreground='white', background='gray', font=side)
    apik.place(relx=0.3, rely=0.01)

    token = tkinter.Label(mainpage, text=u'トークンキー', foreground='white', background='gray', font=side)
    token.place(relx=0.6, rely=0.01)

    bank = tkinter.Label(mainpage, text=u'  bitbank   ', foreground='white', background='gray', font=side, bd=25,
                         relief="ridge")
    bank.place(relx=0.01, rely=0.2)
    bina = tkinter.Label(mainpage, text=u'  binance  ', foreground='white', background='gray', font=side, bd=25,
                         relief="ridge")
    bina.place(relx=0.01, rely=0.4)

    # エントリー　（APIキーの値を入れる)
    bitbank_api = tkinter.Entry(mainpage, width=29, bd=25, font=("", 20), relief="flat")
    bitbank_api.place(relx=0.2, rely=0.2)

    binance_api = tkinter.Entry(mainpage, width=29, bd=25, font=("", 20), relief="flat")
    binance_api.place(relx=0.2, rely=0.4)

    # エントリー２ (トークンの値を入れる)
    bitbank_token = tkinter.Entry(mainpage, width=29, bd=25, font=("", 20), relief="flat")
    bitbank_token.place(relx=0.55, rely=0.2)

    binance_token = tkinter.Entry(mainpage, width=29, bd=25, font=("", 20), relief="flat")
    binance_token.place(relx=0.55, rely=0.4)

    def bitbank_entry(self):
        api_value = bitbank_api.get()
        token_value = bitbank_token.get()
        # bitbank.BITBANK.registration("BITBANK", api_value, token_value)

    button_bitbank = tkinter.Button(mainpage, text=u'登録', foreground='white', background='gray', font=side)
    button_bitbank.place(relx=0.9, rely=0.2)
    button_bitbank.bind("<Button-1>", bitbank_entry)

    def binance_entry(self):
        api_value = binance_api.get()
        token_value = binance_token.get()
        # binance.BINANCE.registration("BINANCE", api_value, token_value)

    button_binance = tkinter.Button(mainpage, text=u'登録', foreground='white', background='gray', font=side)
    button_binance.place(relx=0.9, rely=0.4)
    button_binance.bind("<Button-1>", binance_entry)

    main_menu = tkinter.Button(mainpage, width=30, height=1, text="  戻る  ", command=lambda: changePage(startPage),
                               font=("", 24))
    main_menu.place(relx=0.3, rely=0.7)

    # MainPageを配置
    mainpage.grid(row=0, column=0, sticky="nsew")
    titlepage.place(relx=0.01, rely=0.01)
    mainpage.place(relx=0.01, rely=0.3)

    # StartPageを上位層にする
    startpage.tkraise()

    # ----snsPage------------------------------------

    # SNS登録のフレーム
    snspage = ttk.Frame(window)

    titlepage = tkinter.Frame(snspage, bg='gray', width=1340, height=250, bd=10)
    snspage = tkinter.Frame(snspage, bg='gray', width=1340, height=450, bd=10)

    side = ("", 32)

    # 以下、line_screenから流用
    head = tkinter.Label(titlepage, text=u'API KEYS', foreground='white', background='gray', font=("", 40))
    head.place(relx=0.01, rely=0.01)
    content = tkinter.Label(titlepage, text=u'各SNSからAPIキーを取得してください。', foreground='white', background='gray',
                            font=("", 25))
    content.place(relx=0.15, rely=0.3)

    exchange = tkinter.Label(snspage, text=u'SNS', foreground='white', background='gray', font=side)
    exchange.place(relx=0.015, rely=0.01)

    apik = tkinter.Label(snspage, text=u'APIキー', foreground='white', background='gray', font=side)
    apik.place(relx=0.3, rely=0.01)

    sns = tkinter.Label(snspage, text=u'LINE', foreground='white', background='gray', font=side, bd=25, relief="ridge")
    sns.place(relx=0.01, rely=0.2)
    plans = tkinter.Label(snspage, text=u'予定', foreground='white', background='gray', font=side, bd=25, relief="ridge")
    plans.place(relx=0.01, rely=0.4)

    # エントリー２ (トークンの値を入れる)
    line_token = tkinter.Entry(snspage, width=29, bd=25, font=("", 20), relief="flat")
    line_token.place(relx=0.3, rely=0.2)

    plans_token = tkinter.Entry(snspage, width=29, bd=25, font=("", 20), relief="flat")
    plans_token.place(relx=0.3, rely=0.4)

    def line_entry(self):
        line_value = line_token.get()
        # line.LINE.registration("LINE", line_value)

    button_line = tkinter.Button(snspage, text=u'登録',
                                 foreground='white', background='gray', font=side)
    button_line.place(relx=0.9, rely=0.2)
    button_line.bind("<Button-1>", line_entry)

    button_plans = tkinter.Button(snspage, text=u'登録',
                                  foreground='white', background='gray', font=side)
    button_plans.place(relx=0.9, rely=0.4)

    line_button = tkinter.Button(snspage, width=30, height=1, text="  戻る  ",
                                 command=lambda: changePage(startPage), font=("", 24))
    line_button.place(relx=0.3, rely=0.7)

    # MainPageを配置
    snspage.grid(row=0, column=0, sticky="nsew")
    titlepage.place(relx=0.01, rely=0.01)
    snspage.place(relx=0.01, rely=0.3)

    # StartPageを上位層にする
    startpage.tkraise()


    # プログラムを始める
    window.mainloop()

# メイン
if __name__ == '__main__':
    main()