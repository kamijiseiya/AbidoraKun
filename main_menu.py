"""メイン画面"""
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
# ライブラリ
import tkinter
from tkinter import ttk
import time #価格取得を繰り返す為
import sqlite3 #DBへの追加時のエラーを取得する為

from app.module.exchangess import bitbank
from app.module.exchangess import binance
#from app.module.sns import line
from app import xrpchart

import matplotlib
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg , NavigationToolbar2TkAgg
from matplotlib.figure import Figure

import matplotlib.pyplot as plt  # インストールが必要
from matplotlib import ticker
import pandas as pd  # インストールが必要
import mpl_finance as mpf  #インストールが必要
import matplotlib.dates as mdates
import datetime

import math
import threading
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

    #-----------------------------------StartPage---------------------------------
    ### StartPage用のFrameを生成
    startPage = ttk.Frame(window)
    startTest = tkinter.Frame(startPage, bg='black', width=300, height=200, bd=30, relief="groove")
    backPage = tkinter.Frame(startPage, bg='black', height=400, width=330, bd=10, relief="ridge")
    bidPage = tkinter.Frame(startPage, bg='black', height=175, width=330, bd=10, relief="ridge")
    askPage = tkinter.Frame(startPage, bg='black', height=175, width=330, bd=10, relief="ridge")
    tablePage = tkinter.Frame(startPage, bg='black', width=1010, height=400, bd=15, relief="sunken")

    PointFont = ("Helevetice", 14)
    PointFont2 = ("", 11)

    class Helmholtz_App(tkinter.Tk):
        def __init__(self):
            #tkinter.Tk.__init__(self, *args, **kwargs) 新タブ作成
            #tkinter.Tk.wm_title(self, "Helmholtz Coils Data")　

            container = tkinter.Frame(tablePage)
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

            fig1 = Figure(figsize=(4, 4), dpi=190)
            a = fig1.add_subplot(111)

            #表を作る
            def callback():
                """チャートを表示する"""
                list_bitbank_price = []
                list_time = []
                list_ticker = []
                MAXLENGTH = 100  # 取得したﾃﾞｰﾀを保存する数
                FREQUENCY = 5  # ﾃﾞｰﾀ取得周期

                #Figure.ion()  # インタラクティブモードにする
                fig, ax = Figure(1, 1)
                # 表示場所の設定
                ax_bitbank = Figure.subplot(211)
                ax_ticker = Figure.subplot(212, sharex=ax_bitbank)
                while True:
                    # BITBANKでのXRP売値=bitbank_ask
                    bitbank_id, bitbank_ask, bitbank_bid = bitbank.BITBANK.currencyinformation('XRP') \
                        if bitbank.BITBANK.currencyinformation('XRP') is not None else None
                    # 取引高を取得
                    bitbank_ticker_json = bitbank.BITBANK.tickers('XRP')
                    print(bitbank_ticker_json['baseVolume'])
                    bitbank_ticker = bitbank_ticker_json['baseVolume']
                    print(bitbank_ticker)
                    # 現在の時刻を取得
                    now = datetime.datetime.now()

                    if len(list_time) < MAXLENGTH:
                        list_bitbank_price.append(bitbank_ask)
                        list_ticker.append(bitbank_ticker)
                        list_time.append(now)
                    else:
                        # list内の要素がMAXLENGTHを超えたら、
                        # 先頭の1要素を削除し、最後尾に追加する
                        list_bitbank_price.pop(0)
                        list_bitbank_price.append(bitbank_ask)

                        list_ticker.pop(0)
                        list_ticker.append(bitbank_ticker)

                        list_time.pop(0)
                        list_time.append(now)

                    # ﾁｬｰﾄ用ﾃﾞｰﾀの作成
                    index = pd.DatetimeIndex(list_time, start=list_time[0])
                    bitbank_xrp = pd.Series(list_bitbank_price, index=index)
                    tickers = pd.Series(list_ticker, index=index)
                    print(list_bitbank_price)
                    print(bitbank_xrp)

                    # ここからﾁｬｰﾄ作成
                    Figure.figure(1)
                    ax.xaxis.set_major_locator(mdates.SecondLocator())
                    bitbank_xrp_ohlc = bitbank_xrp.resample('30s').ohlc()
                    tickers_resampled = tickers.resample('30s').max()
                    ax_bitbank.clear()
                    ax_ticker.clear()
                    # ローソク足
                    mpf.candlestick2_ohlc(ax=ax_bitbank, opens=bitbank_xrp_ohlc.open, highs=bitbank_xrp_ohlc.high, \
                                          lows=bitbank_xrp_ohlc.low, closes=bitbank_xrp_ohlc.close, width=1)
                    # 取引高
                    ax_ticker.set_ylim(bottom=min(tickers_resampled) - 10000, top=max(tickers_resampled) + 10000)
                    tickers_resampled.plot(kind='bar', ax=ax_ticker, color='black')
                    # 横軸を日付にする
                    xdate = bitbank_xrp_ohlc.index
                    ax_bitbank.xaxis.set_major_locator(ticker.AutoLocator())

                    def mydate(x, pos):
                        try:
                            return xdate[int(x)]
                        except IndexError:
                            return ''

                    ax_bitbank.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
                    ax_bitbank.format_xdata = mdates.DateFormatter('%H-%T-%s')
                    Figure.xlim(-0.5, 16.5)
                    fig.autofmt_xdate()
                    fig.tight_layout()

                    Figure.draw()
                    Figure.pause(FREQUENCY)  # チャート画面を表示
                    a.plot(kind='bar', ax=ax_ticker, color=('black'))

                #xrpchart.candlechart()
                #a.plot(volt[1], volt[0], 'bo')
                #a.plot(xrpchart.candlechart())
                #a.plot_date(xrpchart.candlechart(), tablePage)

                canvas = FigureCanvasTkAgg(fig1, self)
                canvas.draw()
                canvas.get_tk_widget().pack(side=tkinter.BOTTOM, fill=tkinter.BOTH, expand=True)

                toolbar = NavigationToolbar2TkAgg(canvas, self)
                toolbar.update()
                canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=True)

                #作った表を消す
                def ClearCallback():
                    # problem line
                    # ~~~~~~~~~~~
                    fig1.clf()
                    # ~~~~~~~~~~~
                    clearbutton.destroy()

                clearbutton = ttk.Button(tablePage, text="Clear", command=ClearCallback)
                clearbutton.pack()

            b = ttk.Button(tablePage, text="Plot Data", command=callback)
            b.pack()

            def uge():
                callback()
                window.after(1000, uge())

            #ugeを回す
            #uge()


    class PageTwo(tkinter.Frame):
        def __init__(self, parent, controller):
            tkinter.Frame.__init__(self, parent)

    app = Helmholtz_App()
    #xrpchart.candlechart()



    ### ボタン表示
    # APIキー登録ボタン生成
    startButton =\
     tkinter.Button(startTest, width=31, height=3, text="取引所APIキー登録画面", font=PointFont, command=lambda : changePage(mainPage))

    #expand 親に合わせて変化　fill frameの空きスペースを埋めるか
    startButton.pack(side="left", expand=1, fill="both")

    # SNSボタン生成
    lineButton =\
     tkinter.Button(startTest, width=31, height=3, text="SNS登録", font=PointFont, command=lambda : changePage(snsPage))

    lineButton.pack(side="left", expand=1, fill="both")

    # 設定ボタン生成
    ConfigButton =\
     tkinter.Button(startTest, width=31, height=3, text="設定", font=PointFont, command=lambda : changePage(configPage))

    ConfigButton.pack(side="left", expand=1, fill="both")


    exchange = ttk.Label(backPage, text=u"取引所", foreground='white', background='black', font=PointFont)
    exchange.place(relx=0.1, rely=0.1)
    bid = ttk.Label(backPage, text=u'買値', foreground='white', background='black', font=PointFont)
    bid.place(relx=0.4, rely=0.1)
    ask = ttk.Label(backPage, text=u'売値', foreground='white', background='black', font=PointFont)
    ask.place(relx=0.7, rely=0.1)
    exchangeA = ttk.Label(backPage, text=u"bitbank", foreground='white', background='black', font=PointFont)
    exchangeA.place(relx=0.1, rely=0.2)
    exchangeB = ttk.Label(backPage, text=u"binance", foreground='white', background='black', font=PointFont)
    exchangeB.place(relx=0.1, rely=0.3)



    # bitbankから価格の取得
    """
    exhanges, ask, bid = bitbank.BITBANK.currencyinformation('XRP')
    print(exchange, ask, bid)
    bitbank_ask = ttk.Label(backPage, text=ask, foreground='white', background='black', font=PointFont)
    bitbank_ask.place(relx=0.4, rely=0.2)
    bitbank_bid = ttk.Label(backPage, text=bid, foreground='white', background='black', font=PointFont)
    bitbank_bid.place(relx=0.7, rely=0.2)

    
    # binanceから価格の取得
    exchange2, ask2, bid2 = binance.BINANCE.xrp(0)
    print(exchange2, ask2, bid2)
    binance_ask = ttk.Label(backPage, text=ask2, foreground='white', background='black', font=PointFont)
    binance_ask.place(relx=0.4, rely=0.3)
    binance_bid = ttk.Label(backPage, text=bid2, foreground='white', background='black', font=PointFont)
    binance_bid.place(relx=0.7, rely=0.3)
    """

    buy_order = ttk.Label(bidPage, text=u"買い注文", foreground='white', background='black', font=PointFont)
    buy_order.place(relx=0.4, rely=0.1)
    sell_order = ttk.Label(askPage, text=u"売り注文", foreground='white', background='black', font=PointFont)
    sell_order.place(relx=0.4, rely=0.1)


    #フレームを配置
    startPage.grid(row=0, column=0, sticky="nsew")
    startTest.place(relx=0.01, rely=0.01)
    backPage.place(relx=0.75, rely=0.01)
    bidPage.place(relx=0.75, rely=0.5)
    askPage.place(relx=0.75, rely=0.75)
    tablePage.place(relx=0.01, rely=0.19)

    #-----------------------------------MainPage---------------------------------
    ### MainPage用のFrameを生成
    mainPage = tkinter.Frame(window)

    #別ファイルから読み込み実行
    #exec(open("./entry.py",'r',encoding="utf-8").read())
    side = ("", 32)

    TitlePage = tkinter.Frame(mainPage, bg='gray', width=1340, height=250, bd=10)
    MainPage = tkinter.Frame(mainPage, bg='gray', width=1340, height=450, bd=10)
    #Page = tkinter.Frame(startPage, bg='black', width=1010, height=400, bd=15, relief="sunken")


    #以下、entry_screenを流用
    HEAD = tkinter.Label(TitlePage, text=u'API KEYS', foreground='white', background='gray', font=("", 40))
    HEAD.place(relx=0.01, rely=0.01)
    CONTENT = tkinter.Label(TitlePage, text=u'各取引所からAPIキーを取得してください。', foreground='white', background='gray', font=("", 25))
    CONTENT.place(relx=0.15, rely=0.3)

    EXCHANGES = tkinter.Label(MainPage, text=u'取引所', foreground='white', background='gray', font=side)
    EXCHANGES.place(relx=0.015, rely=0.01)

    APIK = tkinter.Label(MainPage, text=u'APIキー', foreground='white', background='gray', font=side)
    APIK.place(relx=0.3, rely=0.01)

    TOKEN = tkinter.Label(MainPage, text=u'トークンキー', foreground='white', background='gray', font=side)
    TOKEN.place(relx=0.6, rely=0.01)

    BANK = tkinter.Label(MainPage, text=u'  bitbank   ', foreground='white', background='gray', font=side, bd=25, relief="ridge")
    BANK.place(relx=0.01, rely=0.2)
    BINA = tkinter.Label(MainPage, text=u'  binance  ', foreground='white', background='gray', font=side, bd=25, relief="ridge")
    BINA.place(relx=0.01, rely=0.4)

    # エントリー　（APIキーの値を入れる)
    BITBANK_API = tkinter.Entry(MainPage, width=29, bd=25, font=("",20), relief="flat")
    BITBANK_API.place(relx=0.2, rely=0.2)

    BINACE_API = tkinter.Entry(MainPage, width=29, bd=25, font=("",20), relief="flat")
    BINACE_API.place(relx=0.2, rely=0.4)

    # エントリー２ (トークンの値を入れる)
    BITBANK_TOKEN = tkinter.Entry(MainPage, width=29, bd=25, font=("",20), relief="flat")
    BITBANK_TOKEN.place(relx=0.55, rely=0.2)

    BINACE_TOKEN = tkinter.Entry(MainPage, width=29, bd=25, font=("",20), relief="flat")
    BINACE_TOKEN.place(relx=0.55, rely=0.4)

    def bitbank_entry(self):
        API_value = BITBANK_API.get()
        TOKEN_value = BITBANK_TOKEN.get()
        #bitbank.BITBANK.registration("BITBANK", API_value, TOKEN_value)


    BUTTON_BITBANK = tkinter.Button(MainPage, text=u'登録', foreground='white', background='gray', font=side)
    BUTTON_BITBANK.place(relx=0.9, rely=0.2)
    BUTTON_BITBANK.bind("<Button-1>", bitbank_entry)

    def binance_entry(self):
        API_value = BINACE_API.get()
        TOKEN_value = BINACE_TOKEN.get()
        #binance.BINANCE.registration("BINANCE", API_value, TOKEN_value)

    BUTTON_BINANCE = tkinter.Button(MainPage, text=u'登録', foreground='white', background='gray', font=side)
    BUTTON_BINANCE.place(relx=0.9, rely=0.4)
    BUTTON_BINANCE.bind("<Button-1>", binance_entry)


    MAIN_MENU = tkinter.Button(MainPage, width=30, height=1, text="  戻る  ", command=lambda : changePage(startPage), font=("",24))
    MAIN_MENU.place(relx=0.3, rely=0.7)

    # MainPageを配置
    mainPage.grid(row=0, column=0, sticky="nsew")
    TitlePage.place(relx=0.01, rely=0.01)
    MainPage.place(relx=0.01, rely=0.3)



    # StartPageを上位層にする
    startPage.tkraise()


#----snsPage------------------------------------

    # SNS登録のフレーム
    snsPage = ttk.Frame(window)

    titlePage = tkinter.Frame(snsPage, bg='gray', width=1340, height=250, bd=10)
    SnsPage = tkinter.Frame(snsPage, bg='gray', width=1340, height=450, bd=10)

    side = ("", 32)

    #以下、line_screenから流用
    HEAD = tkinter.Label(titlePage, text=u'API KEYS', foreground='white', background='gray', font=("", 40))
    HEAD.place(relx=0.01, rely=0.01)
    CONTENT = tkinter.Label(titlePage, text=u'各SNSからAPIキーを取得してください。',  foreground='white', background='gray', font=("", 25))
    CONTENT.place(relx=0.15, rely=0.3)

    EXCHANGES = tkinter.Label(SnsPage, text=u'SNS', foreground='white', background='gray', font=side)
    EXCHANGES.place(relx=0.015, rely=0.01)

    APIK = tkinter.Label(SnsPage, text=u'APIキー', foreground='white', background='gray', font=side)
    APIK.place(relx=0.3, rely=0.01)

    SNS = tkinter.Label(SnsPage, text=u'LINE', foreground='white', background='gray', font=side, bd=25, relief="ridge")
    SNS.place(relx=0.01, rely=0.2)
    PLANS = tkinter.Label(SnsPage, text=u'予定', foreground='white', background='gray', font=side, bd=25, relief="ridge")
    PLANS.place(relx=0.01, rely=0.4)

    # エントリー２ (トークンの値を入れる)
    LINE_TOKEN = tkinter.Entry(SnsPage, width=29, bd=25, font=("",20), relief="flat")
    LINE_TOKEN.place(relx=0.3, rely=0.2)

    PLANS_TOKEN = tkinter.Entry(SnsPage, width=29, bd=25, font=("",20), relief="flat")
    PLANS_TOKEN.place(relx=0.3, rely=0.4)

    def line_entry(self):
        line_value = LINE_TOKEN.get()
        #line.LINE.registration("LINE", line_value)

    BUTTON_LINE = tkinter.Button(SnsPage, text=u'登録', foreground='white', background='gray', font=side)
    BUTTON_LINE.place(relx=0.9, rely=0.2)
    BUTTON_LINE.bind("<Button-1>", line_entry)

    BUTTON_PLANS = tkinter.Button(SnsPage, text=u'登録', foreground='white', background='gray', font=side)
    BUTTON_PLANS.place(relx=0.9, rely=0.4)


    LINE_Button = tkinter.Button(SnsPage, width=30, height=1, text="  戻る  ", command=lambda: changePage(startPage), font=("", 24))
    LINE_Button.place(relx=0.3, rely=0.7)

    # MainPageを配置
    snsPage.grid(row=0, column=0, sticky="nsew")
    titlePage.place(relx=0.01, rely=0.01)
    SnsPage.place(relx=0.01, rely=0.3)

    # StartPageを上位層にする
    startPage.tkraise()


    """
    def get_bitbank():
        tes = 'hoge'
        tess= 'uge'
        xr = 0.001
        bit_test = ttk.Label(backPage, text=u'test')
        bit_test.place(relx=0.41, rely=0.25)
        bit2_test= ttk.Label(backPage, text=u'tess')
        bit2_test.place(relx=0.71, rely=0.25)

    def get_bitbank():
        for num in range(1):
            exhanges, ask, bid = bitbank.BITBANK.currencyinformation('XRP')
            print(exchange, ask, bid)
            hub = tkinter.Label(backPage, text=u'更新', foreground='white', )



    def bitbank_time():
        get_bitbank()
        window.after(10000, bitbank_time())

    button_relrd = tkinter.Button(backPage, text=u'更新', foreground='white', background='gray')
    button_relrd.place(relx=0.4, rely=0.4)
    button_relrd.bind("<Button-1>", get_bitbank())

    #価格取得の繰り返し
    #bitbank_time()
    """

    """
    def __init__(self):
        flg = False
        self.txt = StringVar()
        ttk.Button(self.root, text="test", command=self.changeLabel).pack()
        self.txt.set("hoge")
        ttk.Label(self.root, textvariable=self.txt).pack()

    def changeLabel(self):
        self.txt.set("Start...")
        t = threading.Thread(target=FunctionThatTakeALotOfTime, args=(self,))
        t.start()

    def FunctionThatTakeALotOfTime(w):
        sleep(2)
        w.txt.set("Finished!")
    """
        # 無限ループ

    while True:
        time.sleep(1)
        exhanges, ask, bid = bitbank.BITBANK.currencyinformation('XRP')
        binance_ask = ttk.Label(backPage, text=ask, foreground='white', background='black')
        binance_ask.place(relx=0.4, rely=0.3)
        binance_ask.update()
        bitbank_bid = ttk.Label(backPage, text=bid, foreground='white', background='black')
        bitbank_bid.place(relx=0.6, rely=0.3)
        bitbank_bid.update()
        exchange2, ask2, bid2 = binance.BINANCE.currencyinformation('XRP')
        binance_ask = ttk.Label(backPage, text=ask2, foreground='white', background='black')
        binance_ask.place(relx=0.4, rely=0.2)
        binance_ask.update()
        binance_bid = ttk.Label(backPage, text=bid2, foreground='white', background='black')
        binance_bid.place(relx=0.6, rely=0.2)
        binance_bid.update()

    # プログラムを始める
    window.mainloop()


# メイン
if __name__ == '__main__':
    main()