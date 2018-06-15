"""XRPの売値をccxtを使用して取得しそれを利用してチャートを表示する"""
import time
import datetime
#import ccxt
import numpy as np#インストールが必要
import pandas as pd#インストールが必要
import matplotlib.pyplot as plt#インストールが必要
from module import exchanges_bitbank
from module import exchanges_binance
from module import btc_to_jpy

#http://okuribitoni.hatenablog.com/entry/2018/01/11/211204を参考にした。

list_bitbank_price = []
list_length_bitbank = 0
list_binance_price = []
list_length_binance = 0
MAXLENGTH = 100 #ﾁｬｰﾄx方向最大値です。
FREQUENCY = 10 #ﾃﾞｰﾀ取得周期です。

#print(ccxt.exchanges)

while True:
    # BITBANKでのXRP売値=bitbank_ask
    bitbank_ask = exchanges_bitbank.bitbank_ask()\
        if exchanges_bitbank.bitbank_ask() is not None else None

    binance_ask = btc_to_jpy.btc_to_jpy(exchanges_binance.binace_ask())
    print(bitbank_ask)
    print(binance_ask)

    # 現在の時刻を取得
    print(datetime.datetime.today())
    time.sleep(FREQUENCY)

    if list_length_bitbank < MAXLENGTH and list_length_binance < MAXLENGTH:
        list_bitbank_price.append(bitbank_ask)
        list_binance_price.append(binance_ask)
    else:
        # list内の要素がmaxlengthを超えたら、
        # 先頭の1要素を削除し、最後尾に追加します。
        if list_length_bitbank < MAXLENGTH:
            list_bitbank_price.append(bitbank_ask)
            list_binance_price.pop(0)
            list_binance_price.append(binance_ask)
        elif list_length_binance < MAXLENGTH:
            list_binance_price.append(binance_ask)
            list_bitbank_price.pop(0)
            list_bitbank_price.append(bitbank_ask)
        else:
            list_bitbank_price.pop(0)
            list_bitbank_price.append(bitbank_ask)
            list_binance_price.pop(0)
            list_binance_price.append(binance_ask)
    # ﾁｬｰﾄ用ﾃﾞｰﾀの作成をします。
    bitbank_xrp = pd.Series(list_bitbank_price)
    list_length_bitbank = len(list_bitbank_price)

    binance_xrp = pd.Series(list_binance_price)
    list_length_binance = len(list_binance_price)

    # ここからﾁｬｰﾄ作成です
    plt.figure(1)
    bitbank_xrp.plot(label='bitbank(xrp/jpy)')
    binance_xrp.plot(label='binance(xrp/jpy)')
    plt.legend()  # チャート名表示
    plt.pause(.001)  # チャート画面を表示
    plt.clf()
    time.sleep(FREQUENCY)
