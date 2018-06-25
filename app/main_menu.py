
# ライブラリ
import tkinter
from tkinter import ttk



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
    window.geometry("800x600")

    # ウィンドウのグリッドを 1x1 にする
    window.grid_rowconfigure(0, weight=1)
    window.grid_columnconfigure(0, weight=1)

    #-----------------------------------StartPage---------------------------------
    ### StartPage用のFrameを生成
    startPage = ttk.Frame(window)
    startTest = tkinter.Frame(startPage, bg='black', width=300, height=200, bd=20, relief="groove")
    backPage = tkinter.Frame(startPage, bg='black', height=300, width=200, bd=10, relief="ridge")
    bidPage = tkinter.Frame(startPage, bg='black', height=150, width=200, bd=10, relief="ridge")
    askPage = tkinter.Frame(startPage, bg='black', height=150, width=200, bd=10, relief="ridge")
    tablePage = tkinter.Frame(startPage, bg='black', width=590, height=350, bd=10, relief="sunken")


    ### ボタン表示
    # APIキー登録ボタン生成
    startButton =\
     tkinter.Button(startTest, width=25, height=2, text="取引所APIキー登録画面", command=lambda : changePage(mainPage))

    #expand 親に合わせて変化　fill frameの空きスペースを埋めるか
    startButton.pack(side="left", expand=1, fill="both")

    # SNSボタン生成
    lineButton =\
     tkinter.Button(startTest, width=25, height=2, text="SNS登録", command=lambda : changePage(snsPage))

    lineButton.pack(side="left", expand=1, fill="both")

    # 設定ボタン生成
    ConfigButton =\
     tkinter.Button(startTest, width=25, height=2, text="設定", command=lambda : changePage(configPage))

    ConfigButton.pack(side="left", expand=1, fill="both")


    exchange = ttk.Label(backPage, text=u"取引所", foreground='white', background='black')
    exchange.place(relx=0.1, rely=0.1)
    bid = ttk.Label(backPage, text=u'買値', foreground='white', background='black')
    bid.place(relx=0.4, rely=0.1)
    ask = ttk.Label(backPage, text=u'売値', foreground='white', background='black')
    ask.place(relx=0.7, rely=0.1)
    exchangeA = ttk.Label(backPage, text=u"取引所A", foreground='white', background='black')
    exchangeA.place(relx=0.1, rely=0.2)
    exchangeB = ttk.Label(backPage, text=u"取引所B", foreground='white', background='black')
    exchangeB.place(relx=0.1, rely=0.3)



    buy_order = ttk.Label(bidPage, text=u"買い注文", foreground='white', background='black')
    buy_order.place(relx=0.1, rely=0.1)
    sell_order = ttk.Label(askPage, text=u"売り注文", foreground='white', background='black')
    sell_order.place(relx=0.1, rely=0.1)


    #フレームを配置
    startPage.grid(row=0, column=0, sticky="nsew")
    startTest.place(relx=0.01, rely=0.01)
    backPage.place(relx=0.75, rely=0.01)
    bidPage.place(relx=0.75, rely=0.5)
    askPage.place(relx=0.75, rely=0.75)
    tablePage.place(relx=0.01, rely=0.15)

    #-----------------------------------MainPage---------------------------------
    ### MainPage用のFrameを生成
    mainPage = tkinter.Frame(window)

    #別ファイルから読み込み実行
    #exec(open("./entry.py",'r',encoding="utf-8").read())


    #以下、entry_screenを流用
    HEAD = tkinter.Label(mainPage, text=u'API KEYS')
    HEAD.grid(row=0, column=1)
    CONTENT = tkinter.Label(mainPage, text=u'各取引所からAPIキーを取得してください。')
    CONTENT.grid(row=1, column=1)

    EXCHANGES = tkinter.Label(mainPage, text=u'取引所')
    EXCHANGES.grid(row=2, column=0)

    APIK = tkinter.Label(mainPage, text=u'APIキー')
    APIK.grid(row=2, column=1)

    TOKEN = tkinter.Label(mainPage, text=u'トークンキー')
    TOKEN.grid(row=2, column=2)

    BANK = tkinter.Label(mainPage, text=u'bitbank')
    BANK.grid(row=3, column=0)
    BINA = tkinter.Label(mainPage, text=u'binace')
    BINA.grid(row=4, column=0)

    # エントリー　（privateキーの値を入れる)
    BITBANK_API = tkinter.Entry(mainPage)
    BITBANK_API.grid(row=3, column=1, padx=15)

    BINACE_API = tkinter.Entry(mainPage)
    BINACE_API.grid(row=4, column=1, padx=15)

    # エントリー２ (トークンの値を入れる)
    BITBANK_TOKEN = tkinter.Entry(mainPage)
    BITBANK_TOKEN.insert(tkinter.END, "トークンの値")
    BITBANK_TOKEN.grid(row=3, column=2, padx=20)

    BINACE_TOKEN = tkinter.Entry(mainPage)
    BINACE_TOKEN.insert(tkinter.END, "トークンの値")
    BINACE_TOKEN.grid(row=4, column=2, padx=20)

    BUTTON_BITBANK = tkinter.Button(mainPage, text=u'登録')
    BUTTON_BITBANK.grid(row=3, column=4)

    BUTTON_BINANCE = tkinter.Button(mainPage, text=u'登録')
    BUTTON_BINANCE.grid(row=4, column=4)

    MAIN_MENU = tkinter.Button(mainPage, text=u'決定')
    MAIN_MENU.grid(row=5, column=1)


    okButton = ttk.Button(mainPage, text="  戻る  ", command=lambda : changePage(startPage))
    okButton.grid(row=6, column=1)

    # MainPageを配置
    mainPage.grid(row=0, column=0, sticky="nsew")

    # StartPageを上位層にする
    startPage.tkraise()

#----snsPage------------------------------------
    # SNS登録のフレーム
    snsPage = ttk.Frame(window)

    #別ファイルから読み込み実行
    #exec(open("./sns.py",'r',encoding="utf-8").read())


    #以下、line_screenから流用
    HEAD = tkinter.Label(snsPage, text=u'API KEYS')
    HEAD.grid(row=0, column=1)
    CONTENT = tkinter.Label(snsPage, text=u'各SNSからAPIキーを取得してください。')
    CONTENT.grid(row=1, column=1)

    EXCHANGES = tkinter.Label(snsPage, text=u'SNS')
    EXCHANGES.grid(row=2, column=0)

    APIK = tkinter.Label(snsPage, text=u'APIキー')
    APIK.grid(row=2, column=1)

    SNS = tkinter.Label(snsPage, text=u'LINE')
    SNS.grid(row=3, column=0)
    PLANS = tkinter.Label(snsPage, text=u'予定')
    PLANS.grid(row=4, column=0)

    # エントリー２ (トークンの値を入れる)
    LINE_TOKEN = tkinter.Entry(snsPage)
    LINE_TOKEN.grid(row=3, column=1, padx=20)

    PLANS_TOKEN = tkinter.Entry(snsPage)
    PLANS_TOKEN.grid(row=4, column=1, padx=20)

    BUTTON_LINE = tkinter.Button(snsPage, text=u'登録')
    BUTTON_LINE.grid(row=3, column=2)

    BUTTON_PLANS = tkinter.Button(snsPage, text=u'登録')
    BUTTON_PLANS.grid(row=4, column=2)

    # ボタン(メインに戻る用)
    MAIN_MENU = tkinter.Button(snsPage, text=u'決定')
    MAIN_MENU.grid(row=5, column=1)


    LINE_Button = ttk.Button(snsPage, text="  戻る  ", command=lambda: changePage(startPage))
    LINE_Button.grid(row=6, column=1)

    # MainPageを配置
    snsPage.grid(row=0, column=0, sticky="nsew")

    # StartPageを上位層にする
    startPage.tkraise()



    # プログラムを始める
    window.mainloop()

# 本体処理
if __name__ == "__main__":
    main()
