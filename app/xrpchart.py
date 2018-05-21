"""XRPの売値をccxtを使用して取得しそれを利用してチャートを表示する"""
import time
import datetime
#import ccxt
import numpy as np#インストールが必要
import matplotlib.pyplot as plt#インストールが必要
from app import module
#http://okuribitoni.hatenablog.com/entry/2018/01/11/211204を参考にした。

BITBANKPRICELIST = []
BITBANKLISTLENGTH = 0
BINANCEPRICELIST = []
BINANCELISTLENGTH = 0
MAXLENGTH = 100 #ﾁｬｰﾄx方向最大値です。
FREQUENCY = 10 #ﾃﾞｰﾀ取得周期です。

#print(ccxt.exchanges)

while True:
    # BITBANKでのXRP売値=BITBANKASK
    BITBANKASK = module.exchanges_bitbank.bitbank_ask()\
        if module.exchanges_bitbank.bitbank_ask() is not None else None

    BINANCEASK = module.btc_to_jpy.btc_to_jpy(module.exchanges_binance.binace_ask())
    print(BITBANKASK)
    print(BINANCEASK)

    # 現在の時刻を取得
    print(datetime.datetime.today())
    time.sleep(FREQUENCY)

    if BITBANKLISTLENGTH < MAXLENGTH and BINANCELISTLENGTH < MAXLENGTH:
        BITBANKPRICELIST.append(BITBANKASK)
        BINANCEPRICELIST.append(BINANCEASK)
    else:
        # list内の要素がmaxlengthを超えたら、
        # 先頭の1要素を削除し、最後尾に追加します。
        if BITBANKLISTLENGTH < MAXLENGTH:
            BITBANKPRICELIST.append(BITBANKASK)
            BINANCEPRICELIST.pop(0)
            BINANCEPRICELIST.append(BINANCEASK)
        elif BINANCELISTLENGTH < MAXLENGTH:
            BINANCEPRICELIST.append(BINANCEASK)
            BITBANKPRICELIST.pop(0)
            BITBANKPRICELIST.append(BITBANKASK)
        else:
            BITBANKPRICELIST.pop(0)
            BITBANKPRICELIST.append(BITBANKASK)
            BINANCEPRICELIST.pop(0)
            BINANCEPRICELIST.append(BINANCEASK)
    # ﾁｬｰﾄ用ﾃﾞｰﾀの作成をします。
    BITBANKXRP = np.array(BITBANKPRICELIST)
    BITBANKLISTLENGTH = len(BITBANKPRICELIST)
    BITBANKX = np.linspace(0, BITBANKLISTLENGTH, BITBANKLISTLENGTH)

    BINANCEXRP = np.array(BINANCEPRICELIST)
    BINANCELISTLENGTH = len(BINANCEPRICELIST)
    BINANCEX = np.linspace(0, BINANCELISTLENGTH, BINANCELISTLENGTH)

    # ここからﾁｬｰﾄ作成です
    plt.figure(1)
    plt.plot(BITBANKX, BITBANKXRP, label='bitbank(xrp/jpy)')
    plt.plot(BINANCEX, BINANCEXRP, label='binance(xrp/jpy)')
    plt.legend()  # チャート名表示
    plt.pause(.001)  # チャート画面を表示
    plt.clf()
    time.sleep(FREQUENCY)
