"""メイン画面"""
import os  # パスを操作するモジュール
import sys  # パスを読み込むモジュール
import subprocess
import threading

sys.path.append(os.path.abspath(os.path.join('..')))  # 自作モジュールのパス指定
# ライブラリ
import tkinter
from tkinter import ttk
import time  # 価格取得を繰り返す為
import sqlite3  # DBへの追加時のエラーを取得する為

#from app.module.exchangess import bitbank
#from app.module.exchangess import binance
#from app.module.exchangess import quoinex
#from app.module.sns import line
#from app import xrpchart
from app import graphcreation
from app.module.exchangess import calculation

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
    canvass = tkinter.Canvas(backpage, height=350, width=290, bg='gray')

    #スクロールバー生成
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

    bidpage = tkinter.Frame(startpage,  height=50, width=330, bd=10, relief="ridge", bg='black')
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

    #button 300 furagu1010 =1310  zenntai 1500 heig 1000-furagu400button200 zenn 600
    undrpage = tkinter.Frame(startpage, width=1010, height=180, bd=15, relief="ridge", bg='black')
    undercanvas = tkinter.Canvas(undrpage, bg='black', width=960, height=125, relief="ridge")

    under = tkinter.Scrollbar(undrpage, orient=tkinter.VERTICAL)
    under.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    under.config(command=undercanvas.yview)

    undercanvas.config(yscrollcommand=under.set)
    undercanvas.config(scrollregion=(0,0,400,500))
    undercanvas.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

    underframe = tkinter.Frame(undercanvas, bg='gray')

    undercanvas.create_window((0,0), window=underframe, anchor=tkinter.NW, width=undercanvas.cget('width'))

    #underpageを白く(underframe)の上書きになるため＃化
    #undrtext = ttk.Label(undrpage, text=u'                             ', font=('',80))
    #undrtext.place(rely=0.0, relx=0.0)

    htest = []
    for n in range(40):
        tes = tkinter.Label(underframe, text="")
        htest.append(tes)
        tes.pack(fill=tkinter.X)

    test=[]
    for n in range(30):
        tes = tkinter.Label(orderframe, text="")
        test.append(tes)
        tes.pack(fill=tkinter.X)

    PointFont = ("Helevetice", 14)

    exchangeA = ttk.Label(scrollframe, text=u"bitbank", font=PointFont)
    exchangeA.place(relx=0.1, rely=0.15)
    exchangeC = ttk.Label(scrollframe, text=u"binance", font=PointFont)
    exchangeC.place(relx=0.1, rely=0.2)
    exchangeD = ttk.Label(scrollframe, text=u"quoinex", font=PointFont)
    exchangeD.place(relx=0.1, rely=0.25)

    #現在の売買最大値取得(XRP)
    #transaction = calculation.CALCULATION.difference_xrp_btc("")['max']
    tara = ttk.Label(underframe, text="binanceで○○で購入しbitbankで□□で売り"+"の利益です。", font=PointFont)
    tara.place(relx=0.1, rely=0.05)

    #現在の売買最大値取得(BTC)
    """
    ask_btc = ""
    bid_btc = ""
    btc_max = calculation.CALCULATION.difference_btc_xrp(1)['max']
    btc_value = calculation.CALCULATION.difference_btc_xrp(1)['maxvalue']
    #buy = calculation.CALCULATION.difference_btc_xrp(1)['max_buy']
    #sale = calculation.CALCULATION.difference_btc_xrp(1)['min_sale']

    #売買取引所の抽出
    if(str(btc_max).startswith('bitbank')):
        ask_btc = "bitbank"
    elif(str(btc_max).startswith('binance')):
        ask_btc = "binance"
    elif(str(btc_max).startswith('coinex')):
        ask_btc = "coinex"

    if(str(btc_max).endswith('bitbank')):
        bid_btc = "bitbank"
    elif(str(btc_max)).endswith(('binance')):
        bid_btc = "binance"
    elif(str(btc_max)).endswith(('coinex')):
        bid_btc = "coinex"

    bmax = ttk.Label(underframe, text=ask_btc+str(btc_value)+bid_btc, font=PointFont)
    #bmax = ttk.Label(underframe, text=ask_btc+str(btc_value)+bid_btc+str(buy)+str(sale), font=PointFont)

    bmax.place(relx=0.1, rely=0.1)
    """
    # 現在の売買最大値取得(BTC)
    def func():
        count = 0.0
        for num in range(1, 10):
            lists = calculation.CALCULATION.difference_btc_xrp(1)
            max_exchange = lists["max"]
            #利益売買取引所の抽出
            ask_btc = ""
            bid_btc = ""
            if (str(max_exchange).startswith('bitbank')):
                ask_btc = "bitbank"
            elif (str(max_exchange).startswith('binance')):
                ask_btc = "binance"
            elif (str(max_exchange).startswith('coinex')):
                ask_btc = "coinex"

            if (str(max_exchange).endswith('bitbank')):
                bid_btc = "bitbank"
            elif (str(max_exchange)).endswith(('binance')):
                bid_btc = "binance"
            elif (str(max_exchange)).endswith(('coinex')):
                bid_btc = "coinex"
            #現在の最大利益取得
            btc_value = lists['maxvalue']
            max_btc = lists['max_buy']
            min_btc = lists['min_sale']
            thread = ttk.Label(underframe, text=str(ask_btc)+"で"+str(max_btc)+"円購入し"+str(bid_btc)+"で"+str(min_btc)+"円売却し"+str(btc_value)+"の利益です。", font=PointFont)
            thread.place(relx=0.1, rely=0.01 + float(count))
            thread.update()
            count =+ 0.03 * num
            time.sleep(30)
    """
    def func():
        count = 0.0
        while True:
            btc_value = calculation.CALCULATION.difference_btc_xrp(1)['maxvalue']
            thread = ttk.Label(underframe, text=btc_value, font=PointFont)
            thread.place(relx=0.1, rely=0.01 + float(count))
            thread.update()
            count =+ 0.03
            time.sleep(10)
    """

    # orderframe test
    ordertest =ttk.Label(orderframe, text=u'bitbank', font=PointFont)
    ordertest.place(relx=0.1, rely=0.02)

    ### ボタン表示
    # APIキー登録ボタン生成
    startbutton = \
        tkinter.Button(starttest, width=31, height=3, text="取引所設定", font=PointFont, command=lambda: changePage(mainPage))

    # expand 親に合わせて変化　fill frameの空きスペースを埋めるか
    startbutton.pack(side="left", expand=1, fill="both")

    # 管理画面ボタン生成
    managementbutton = \
        tkinter.Button(starttest, width=31, height=3, text=u'管理画面', font=PointFont,
                       command=lambda: changePage(managementpage))

    managementbutton.pack(side='left', expand=1, fill="both")

    # SNSボタン生成
    linebutton = \
        tkinter.Button(starttest, width=31, height=3, text="通知設定", font=PointFont, command=lambda: changePage(snsPage))

    linebutton.pack(side="left", expand=1, fill="both")

    def create(self) :
        grobal = graphcreation.GRAPHCREATION.create_graph_png(self)
        return grobal


    def Getxrp() :
        graphcreation.GRAPHCREATION.create_graph_png("xrpjpy")
        xrpjpy = tkinter.PhotoImage(file='config/img/xrpjpycandlestick_week.png')
        #画像更新
        figure = tkinter.Canvas(tablepage, width=950, height=370)
        figure.place(x=0, y=0)
        figure.create_image(0, 0, image=xrpjpy, anchor=tkinter.NW)
        figure.update()

        exchangeA = ttk.Label(scrollframe, text=u"bitbank", font=PointFont)
        exchangeA.place(relx=0.1, rely=0.15)
        exchangeA.update()
        exchangeC = ttk.Label(scrollframe, text=u"binance", font=PointFont)
        exchangeC.place(relx=0.1, rely=0.2)
        exchangeC.update()
        exchangeD = ttk.Label(scrollframe, text=u"quoinex", font=PointFont)
        exchangeD.place(relx=0.1, rely=0.25)
        exchangeD.update()
        # bitbankからxrp価格取得
        exhanges, ask, bid = bitbank.BITBANK.currencyinformation('XRP')
        bitbank_ask = ttk.Label(scrollframe, text=ask, font=PointFont)
        bitbank_ask.place(relx=0.4, rely=0.15)
        bitbank_ask.update()
        bitbank_bid = ttk.Label(scrollframe, text=bid, font=PointFont)
        bitbank_bid.place(relx=0.7, rely=0.15)
        bitbank_bid.update()
        # binanseから価格取得
        exchange2, ask2, bid2 = binance.BINANCE.currencyinformation('XRP')
        binance_ask = ttk.Label(scrollframe, text=ask2, font=PointFont)
        binance_ask.place(relx=0.4, rely=0.2)
        binance_ask.update()
        binance_bid = ttk.Label(scrollframe, text=bid2, font=PointFont)
        binance_bid.place(relx=0.7, rely=0.2)
        binance_bid.update()
        # quoinexから価格取得
        exchange2, ask2, bid2 = quoinex.Quoinex.currencyinformation('XRP')
        quoinex_ask = ttk.Label(scrollframe, text=ask2, font=PointFont)
        quoinex_ask.place(relx=0.4, rely=0.25)
        quoinex_ask.update()
        quoinex_bid = ttk.Label(scrollframe, text=bid2, font=PointFont)
        quoinex_bid.place(relx=0.7, rely=0.25)
        quoinex_bid.update()


    xrp = tkinter.Button(backpage, text="XRP", width=7, font=PointFont, command=Getxrp)
    xrp.place(relx=0.0, rely=0.0)

    def Getbtc() :
        graphcreation.GRAPHCREATION.create_graph_png("btcjpy")
        btcjpy = tkinter.PhotoImage(file='config/img/btcjpycandlestick_week.png')
        # 画像更新
        figure = tkinter.Canvas(tablepage, width=970, height=370)
        figure.place(x=0, y=0)
        figure.create_image(0, 0, image=btcjpy, anchor=tkinter.NW)
        figure.update()

        exchangeA = ttk.Label(scrollframe, text=u"bitbank", font=PointFont)
        exchangeA.place(relx=0.1, rely=0.15)
        exchangeA.update()
        exchangeC = ttk.Label(scrollframe, text=u"binance", font=PointFont)
        exchangeC.place(relx=0.1, rely=0.2)
        exchangeC.update()
        exchangeD = ttk.Label(scrollframe, text=u"quoinex", font=PointFont)
        exchangeD.place(relx=0.1, rely=0.25)
        exchangeD.update()
        # bitbankから現在価格取得
        exhanges, ask, bid = bitbank.BITBANK.currencyinformation('BTC')
        bitbank_ask = ttk.Label(scrollframe, text=ask, font=PointFont)
        bitbank_ask.place(relx=0.4, rely=0.15)
        bitbank_ask.update()
        bitbank_bid = ttk.Label(scrollframe, text=bid, font=PointFont)
        bitbank_bid.place(relx=0.7, rely=0.15)
        bitbank_bid.update()
        """
        # binanseから現在価格取得 
        exchange2, ask2, bid2 = binance.BINANCE.currencyinformation('BTC')
        binance_ask = ttk.Label(scrollframe, text=ask2, font=PointFont)
        binance_ask.place(relx=0.4, rely=0.2)
        binance_ask.update()
        binance_bid = ttk.Label(scrollframe, text=bid2, font=PointFont)
        binance_bid.place(relx=0.7, rely=0.2)
        binance_bid.update()
        """
        # quoinexから価格取得
        exchange3, ask3, bid3 = quoinex.Quoinex.currencyinformation('BTC')
        quoinex_ask = ttk.Label(scrollframe, text=ask3, font=PointFont)
        quoinex_ask.place(relx=0.4, rely=0.25)
        quoinex_ask.update()
        quoinex_bid = ttk.Label(scrollframe, text=bid3, font=PointFont)
        quoinex_bid.place(relx=0.7, rely=0.25)
        quoinex_bid.update()

    bitbankbutton = tkinter.Button(backpage, text="BTC", font=PointFont, width=7, command=Getbtc)
    bitbankbutton.place(relx=0.25, rely=0.0)

    def Geteth() :
        graphcreation.GRAPHCREATION.create_graph_png("ethjpy")
        ethjpy = tkinter.PhotoImage(file='config/img/ethjpycandlestick_week.png')
        # 画像更新
        figure = tkinter.Canvas(tablepage, width=980, height=370)
        figure.place(x=0, y=0)
        figure.create_image(0, 0, image=ethjpy, anchor=tkinter.NW)
        figure.update()

        exchangeA = ttk.Label(scrollframe, text=u"bitbank", font=PointFont)
        exchangeA.place(relx=0.1, rely=0.15)
        exchangeA.update()
        exchangeC = ttk.Label(scrollframe, text=u"          ", font=PointFont)
        exchangeC.place(relx=0.1, rely=0.2)
        exchangeC.update()
        exchangeD = ttk.Label(scrollframe, text=u"          ", font=PointFont)
        exchangeD.place(relx=0.1, rely=0.25)
        exchangeD.update()
        # bitbankから現在価格取得
        exhanges, ask, bid = bitbank.BITBANK.currencyinformation('ETH')
        bitbank_ask = ttk.Label(scrollframe, text=ask, font=PointFont)
        bitbank_ask.place(relx=0.4, rely=0.15)
        bitbank_ask.update()
        bitbank_bid = ttk.Label(scrollframe, text=bid, font=PointFont)
        bitbank_bid.place(relx=0.7, rely=0.15)
        bitbank_bid.update()

    eth = tkinter.Button(backpage, text="ETH", font=PointFont, width=7, command=Geteth)
    eth.place(relx=0.5, rely=0.0)

    def Getltc() :
        #グラフ生成、保存、表示
        graphcreation.GRAPHCREATION.create_graph_png("ltcbtc")
        ltcjpy = tkinter.PhotoImage(file='config/img/ltcbtccandlestick_week.png')
        figure = tkinter.Canvas(tablepage, width=980, height=370)
        figure.place(x=0, y=0)
        figure.create_image(0, 0, image=ltcjpy, anchor=tkinter.NW)
        figure.update()

        exchangeA = ttk.Label(scrollframe, text=u"bitbank", font=PointFont)
        exchangeA.place(relx=0.1, rely=0.15)
        exchangeA.update()
        exchangeC = ttk.Label(scrollframe, text=u"binance", font=PointFont)
        exchangeC.place(relx=0.1, rely=0.2)
        exchangeC.update()
        exchangeD = ttk.Label(scrollframe, text=u"          ", font=PointFont)
        exchangeD.place(relx=0.1, rely=0.25)
        exchangeD.update()
        """
        # bitbankから現在価格取得
        exhanges, ask, bid = bitbank.BITBANK.currencyinformation('LTC')
        bitbank_ask = ttk.Label(scrollframe, text=ask, font=PointFont)
        bitbank_ask.place(relx=0.4, rely=0.15)
        bitbank_ask.update()
        bitbank_bid = ttk.Label(scrollframe, text=bid, font=PointFont)
        bitbank_bid.place(relx=0.7, rely=0.15)
        bitbank_bid.update()
        """
        # binanseから現在価格取得
        exchange2, ask2, bid2 = binance.BINANCE.currencyinformation('LTC')
        binance_ask = ttk.Label(scrollframe, text=ask2, font=PointFont)
        binance_ask.place(relx=0.4, rely=0.2)
        binance_ask.update()
        binance_bid = ttk.Label(scrollframe, text=bid2, font=PointFont)
        binance_bid.place(relx=0.7, rely=0.2)
        binance_bid.update()
        # quoinexの値を空白に
        quoinex_ask = ttk.Label(scrollframe, text=u"          ", font=PointFont)
        quoinex_ask.place(relx=0.4, rely=0.25)
        quoinex_bid = ttk.Label(scrollframe, text=u"          ", font=PointFont)
        quoinex_bid.place(relx=0.7, rely=0.25)

    ltc = tkinter.Button(backpage, text="LTC", font=PointFont, width=7, command=Getltc)
    ltc.place(relx=0.75, rely=0.0)

    exchange = ttk.Label(backpage, text=u"取引所", font=PointFont)
    exchange.place(relx=0.1, rely=0.12)
    bid = ttk.Label(backpage, text=u'買値', font=PointFont)
    bid.place(relx=0.4, rely=0.12)
    ask = ttk.Label(backpage, text=u'売値', font=PointFont)
    ask.place(relx=0.7, rely=0.12)

    orderpaint = ttk.Label(bidpage, text="        ", font=('', 100))
    orderpaint.place(relx=0.0, rely=0.0)
    orderexchange = ttk.Label(bidpage, text=u'取引所', font=PointFont)
    orderexchange.place(relx=0.1, rely=0.1)
    orderstatus = ttk.Label(bidpage, text=u'注文状態', font=PointFont)
    orderstatus.place(relx=0.4, rely=0.1)
    orderprice = ttk.Label(bidpage, text=u'注文価格', font=PointFont)
    orderprice.place(relx=0.7, rely=0.1)

    #起動時重くなる為今はグラフ生成省略
    #graphcreation.GRAPHCREATION.create_graph_png("xrpjpy") #グラフ作成
    #起動時のグラフ表示
    fill = tkinter.PhotoImage(file='config/img/xrpjpycandlestick_week.png')
    can = tkinter.Canvas(tablepage, width=980, height=370)
    can.place(x=0, y=0)
    can.create_image(0, 0, image=fill, anchor=tkinter.NW)
    can.update()


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

    #window.columnconfigure(0, weight=1)
    #window.master.columnconfigure(0, weight=1)
    #window.master.rowconfigure(0, weight=1)

    undrpage.place(relx=0.01, rely=0.725)
    undercanvas.pack()

    # -----------------------------------MainPage---------------------------------
    ### MainPage用のFrameを生成
    mainPage = tkinter.Frame(window)

    side = ("", 32)

    full = tkinter.Frame(mainPage, width=1300, height=900)

    allbar = tkinter.Canvas(full, width=1330, height=900)

    abar = tkinter.Scrollbar(full, orient=tkinter.VERTICAL)
    abar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    abar.config(command=allbar.yview)

    allbar.config(yscrollcommand=abar.set)
    allbar.config(scrollregion=("0c","0c","50c","50c"))
    allbar.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

    allframe = tkinter.Frame(allbar)

    allbar.create_window((0,0), window=allframe, anchor=tkinter.NW, width=allbar.cget('width'))

    alf=[]
    for m in range(4000):
        btb = tkinter.Label(allframe, text="")
        alf.append(btb)
        btb.pack(fill=tkinter.X)

    titlepage = tkinter.Frame(allframe, width=1300, height=250, bd=10, relief="groove")
    mainpage = tkinter.Frame(allframe, width=1300, height=450)


    # snspageと同じように
    title = tkinter.Label(titlepage, text=u'')
    title.pack(fill='both', ipadx=550, ipady=30, side='left')
    """
    head = tkinter.Label(titlepage, text=u'API KEYS', foreground='white', background='gray', font=("", 40))
    head.place(relx=0.01, rely=0.01)
    content = tkinter.Label(titlepage, text=u'各取引所からAPIキーを取得してください。', foreground='white', background='gray',
                            font=("", 25))
    content.place(relx=0.15, rely=0.3)
    """

    exchange = tkinter.Label(mainpage, text=u'取引所', font=side, relief="groove")
    exchange.place(relx=0.1, rely=0.0, relheight=0.09, relwidth=0.2)

    apik = tkinter.Label(mainpage, text=u'APIキー', font=side, relief="groove")
    apik.place(relx=0.4, rely=0.0)

    token = tkinter.Label(mainpage, text=u'トークンキー', font=side, relief="groove")
    token.place(relx=0.7, rely=0.0)

    bank = tkinter.Label(mainpage, text=u'  bitbank   ', font=side, relief="groove")
    bank.place(relx=0.1, rely=0.16)
    bina = tkinter.Label(mainpage, text=u'  binance   ', font=side, relief="groove")
    bina.place(relx=0.1, rely=0.4)
    etha = tkinter.Label(mainpage, text=u'  ethereum  ', font=side, relief="groove")
    etha.place(relx=0.1, rely=0.64)
    ltca = tkinter.Label(mainpage, text=u'  litecoin  ', font=side, relief="groove")
    ltca.place(relx=0.1, rely=0.88)


    # エントリー　（APIキーの値を入れる)
    bitbank_api = tkinter.Entry(mainpage, width=20, bd=20, font=("", 18), relief="flat")
    bitbank_api.place(relx=0.4, rely=0.16)

    binance_api = tkinter.Entry(mainpage, width=20, bd=20, font=("", 18), relief="flat")
    binance_api.place(relx=0.4, rely=0.4)

    #kali
    eth_api = tkinter.Entry(mainpage, width=20, bd=20, font=("", 18), relief="flat")
    eth_api.place(relx=0.4, rely=0.64)

    ltc_api = tkinter.Entry(mainpage, width=20, bd=20, font=("", 18), relief="flat")
    ltc_api.place(relx=0.4, rely=0.88)

    # エントリー２ (トークンの値を入れる)
    bitbank_token = tkinter.Entry(mainpage, width=20, bd=20, font=("", 18), relief="flat")
    bitbank_token.place(relx=0.7, rely=0.16)

    binance_token = tkinter.Entry(mainpage, width=20, bd=20, font=("", 18), relief="flat")
    binance_token.place(relx=0.7, rely=0.4)

    # kali
    eth_token = tkinter.Entry(mainpage, width=20, bd=20, font=("", 18), relief="flat")
    eth_token.place(relx=0.7, rely=0.64)

    ltc_token =  tkinter.Entry(mainpage, width=20, bd=20, font=("", 18), relief="flat")
    ltc_token.place(relx=0.7, rely=0.88)

    def bitbank_entry(self):
        api_value = bitbank_api.get()
        token_value = bitbank_token.get()
        # bitbank.BITBANK.registration("BITBANK", api_value, token_value)

    button_bitbank = tkinter.Button(mainpage, text=u'登録', font=side)
    button_bitbank.place(relx=0.9, rely=0.16)
    button_bitbank.bind("<Button-1>", bitbank_entry)

    def binance_entry(self):
        api_value = binance_api.get()
        token_value = binance_token.get()
        # binance.BINANCE.registration("BINANCE", api_value, token_value)

    button_binance = tkinter.Button(mainpage, text=u'登録', font=side)
    button_binance.place(relx=0.9, rely=0.4)
    button_binance.bind("<Button-1>", binance_entry)

    main_menu = tkinter.Button(mainpage, width=30, height=1, text="  戻る  ", command=lambda: changePage(startpage),
                               font=("", 24))
    main_menu.place(relx=0.3, rely=0.92)

    # MainPageを配置
    mainPage.grid(row=0, column=0, sticky="nsew")
    full.place(relx=0.0, rely=0.0)
    titlepage.place(relx=0.01, rely=0.001)
    mainpage.place(relx=0.01, rely=0.003)

    # StartPageを上位層にする
    startpage.tkraise()

    # ----snsPage------------------------------------

    # SNS登録のフレーム
    snsPage = ttk.Frame(window)

    all = tkinter.Frame(snsPage, width=1300, height=900)

    allbar = tkinter.Canvas(all, width=1330, height=900)

    abar = tkinter.Scrollbar(all, orient=tkinter.VERTICAL)
    abar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    abar.config(command=allbar.yview)

    allbar.config(yscrollcommand=abar.set)
    allbar.config(scrollregion=("0c", "0c", "40c", "40c"))
    allbar.pack(side=tkinter.LEFT, fill=tkinter.BOTH)

    allframe = tkinter.Frame(allbar)

    allbar.create_window((0, 0), window=allframe, anchor=tkinter.NW, width=allbar.cget('width'))

    alf = []
    for m in range(4000):
        btb = tkinter.Label(allframe, text="")
        alf.append(btb)
        btb.pack(fill=tkinter.X)

    titlepage = tkinter.Frame(allframe, width=1300, height=250, bd=30, relief="groove")
    snspage = tkinter.Frame(allframe, width=1350, height=1000)

    title = tkinter.Label(titlepage, text=u'')
    title.pack(fill='both', ipadx=550, ipady=30, side='left')

    #service = tkinter.Label(snspage, text=u"通知サービス              APIキー", font=side, relief="groove")
    #service.place(relx=0.1, rely=0.0, relheight=0.1, relwidth=0.8, anchor=tkinter.NW)
    service = tkinter.Label(snspage, text=u"通知サービス", font=side, relief="groove")
    service.place(relx=0.1, rely=0.0, relheight=0.07, relwidth=0.3)
    apikey = tkinter.Label(snspage, text=u"APIキー", font=side, relief="groove")
    apikey.place(relx=0.4, rely=0.0, relheight=0.07, relwidth=0.3)
    line = tkinter.Label(snspage, text=u"LINE", font=side, relief="groove")
    line.place(relx=0.1, rely=0.07, relheight=0.1, relwidth=0.3)

    service = tkinter.Label(snspage, text=u"通知サービス", font=side, relief="groove")
    service.place(relx=0.1, rely=0.2, relheight=0.07, relwidth=0.3)
    apikey = tkinter.Label(snspage, text=u"APIキー", font=side, relief="groove")
    apikey.place(relx=0.4, rely=0.2, relheight=0.07, relwidth=0.3)
    slack = tkinter.Label(snspage, text=u"Slack", font=side, relief="groove")
    slack.place(relx=0.1, rely=0.27, relheight=0.1, relwidth=0.3)

    service = tkinter.Label(snspage, text=u"通知サービス", font=side, relief="ridge")
    service.place(relx=0.1, rely=0.4, relheight=0.07, relwidth=0.3)
    apikey = tkinter.Label(snspage, text=u"APIキー", font=side, relief="ridge")
    apikey.place(relx=0.4, rely=0.4, relheight=0.07, relwidth=0.3)
    sample = tkinter.Label(snspage, text=u"Sample", font=side, relief="ridge")
    sample.place(relx=0.1, rely=0.47, relheight=0.1, relwidth=0.3)


    # エントリー (APIキーの入力)
    line_token = tkinter.Entry(snspage, width=20, bd=20, font=("", 18), relief="flat")
    line_token.place(relx=0.4, rely=0.075, relheight=0.1, relwidth=0.3)

    slack_token = tkinter.Entry(snspage, width=20, bd=20, font=("", 18), relief="flat")
    slack_token.place(relx=0.4, rely=0.27, relheight=0.1, relwidth=0.3)

    slack_token = tkinter.Entry(snspage, width=20, bd=20, font=("", 18), relief="flat")
    slack_token.place(relx=0.4, rely=0.47, relheight=0.1, relwidth=0.3)

    def line_entry(self):
        line_value = line_token.get()
        # line.LINE.registration("LINE", line_value)

    button_line = tkinter.Button(snspage, text=u'登録', font=side, height=2, width=6)
    button_line.place(relx=0.7, rely=0.07)
    button_line.bind("<Button-1>", line_entry)

    button_slack = tkinter.Button(snspage, text=u'登録', font=side, height=2, width=6)
    button_slack.place(relx=0.7, rely=0.27)
    button_slack.bind("<Button-1>", line_entry)

    button_sample = tkinter.Button(snspage, text=u'登録', font=side, height=2, width=6)
    button_sample.place(relx=0.7, rely=0.47)
    button_sample.bind("<Button-1>", line_entry)

    line_button = tkinter.Button(snspage, width=30, height=1, text="  戻る  ",
                                 command=lambda: changePage(startpage))
    line_button.place(relx=0.4, rely=0.7)

    # snsPageを配置
    snsPage.grid(row=0, column=0, sticky="nsew")
    all.place(relx=0.0, rely=0.0)
    titlepage.place(relx=0.1, rely=0.0)
    snspage.place(relx=0.01, rely=0.003)

    # StartPageを上位層にする
    startpage.tkraise()

    # ----managementPage------------------------------------
    # 資産管理のフレーム
    managementpage = ttk.Frame(window)

    setpage = tkinter.Frame(managementpage, width=1300, height=250, bd=30, relief="groove")
    grafpage = tkinter.Frame(managementpage, width=750, height=750)
    valuepage = tkinter.Frame(managementpage, width=750, height=750)

    Font = ("Helevetice", 28)

    ffreme = ttk.Label(setpage, text=u'', font=Font)
    ffreme.pack(fill='both', ipadx=550, ipady=30, side='left')

    # 画像を表示する(jpegとpngは動作確認済)
    sample = tkinter.PhotoImage(file='config/img/figure.png') # 画像ファイルのパス
    canvas = tkinter.Canvas(grafpage, width=1000, height=1000)
    canvas.place(x=0, y=0)
    canvas.create_image(0, 0, image=sample, anchor=tkinter.NW)

    totalasset = ttk.Label(valuepage, text=u'資産総額 ：', font=Font)
    totalasset.place(relx=0.1, rely=0.1)
    totalassetvalue = ttk.Label(valuepage, text=u' 20,660,793円', font=Font)
    totalassetvalue.place(relx=0.35, rely=0.1)

    assetitems = ttk.Label(valuepage, text=u'■資産の内訳', font=Font)
    assetitems.place(relx=0.1, rely=0.15)

    xrp = ttk.Label(valuepage, text=u'      XRP      ', font=Font, relief="ridge")
    xrp.place(relx=0.1, rely=0.2)
    xrpvalue = ttk.Label(valuepage, text=u' 20,660,793円', font=Font, relief="ridge")
    xrpvalue.place(relx=0.35, rely=0.2)
    btc = ttk.Label(valuepage, text=u'      BTC      ', font=Font, relief="ridge")
    btc.place(relx=0.1, rely=0.25)
    btcvalue = ttk.Label(valuepage, text=u' 20,660,793円', font=Font, relief="ridge")
    btcvalue.place(relx=0.35, rely=0.25)
    eth = ttk.Label(valuepage, text=u'      ETH      ', font=Font, relief="ridge")
    eth.place(relx=0.1, rely=0.3)
    ethvalue = ttk.Label(valuepage, text=u' 20,660,793円', font=Font, relief="ridge")
    ethvalue.place(relx=0.35, rely=0.3)
    ltc = ttk.Label(valuepage, text=u'      LTC      ', font=Font, relief="ridge")
    ltc.place(relx=0.1, rely=0.35)
    ltcvalue = ttk.Label(valuepage, text=u' 20,660,793円', font=Font, relief="ridge")
    ltcvalue.place(relx=0.35, rely=0.35)
    mona = ttk.Label(valuepage, text=u'    MONA    ', font=Font, relief="ridge")
    mona.place(relx=0.1, rely=0.4)
    monavalue = ttk.Label(valuepage, text=u' 20,660,793円', font=Font, relief="ridge")
    monavalue.place(relx=0.35, rely=0.4)
    other = ttk.Label(valuepage, text=u'    その他    ', font=Font, relief="ridge")
    other.place(relx=0.1, rely=0.45)
    othervalue = ttk.Label(valuepage, text=u' 20,660,793円', font=Font, relief="ridge")
    othervalue.place(relx=0.35, rely=0.45)

    return_button = tkinter.Button(valuepage, text="  戻る  ", command=lambda: changePage(startpage))
    return_button.place(relx=0.3, rely=0.55)

    # managementPageを配置
    managementpage.grid(row=0, column=0, sticky="nsew")
    setpage.place(relx=0.05, rely=0.01)
    grafpage.place(relx=0.0, rely=0.25)
    valuepage.place(relx=0.55, rely=0.25)

    startpage.tkraise()

    #スレッド要素
    thread_1 = threading.Thread(target=func())
    thread_1.start()

    #threadd = threading.Thread(target=)

    # プログラムを始める
    window.mainloop()

# メイン
if __name__ == '__main__':
    main()
    #thread_1 = threading.Thread(target=func)
    #thread_1.start()