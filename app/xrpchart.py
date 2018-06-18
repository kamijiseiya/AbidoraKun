"""XRPの売値をccxtを使用して取得しそれを利用してチャートを表示する"""
import time
import datetime
import matplotlib.dates as mdates
#import ccxt
import numpy as np#インストールが必要
import pandas as pd#インストールが必要
import matplotlib.pyplot as plt#インストールが必要
from module import exchanges_bitbank
from module import exchanges_binance
from module import btc_to_jpy

#参考
#http://okuribitoni.hatenablog.com/entry/2018/01/11/211204
#https://teratail.com/questions/85572
list_bitbank_price = []
list_length_bitbank = 0
list_binance_price = []
list_length_binance = 0
list_time = []
list_length_time = 0
MAXLENGTH = 100 #ﾁｬｰﾄx方向最大値です。
FREQUENCY = 10 #ﾃﾞｰﾀ取得周期です。

#print(ccxt.exchanges)
plt.ion() # インタラクティブモードにする
fig, ax = plt.subplots(1,1)
ax_bitbank = plt.subplot(211)
ax_binance = plt.subplot(212)
while True:
    # BITBANKでのXRP売値=bitbank_ask
    bitbank_ask = exchanges_bitbank.bitbank_ask()\
        if exchanges_bitbank.bitbank_ask() is not None else None
    # 現在の時刻を取得
    now = datetime.datetime.now()
    print(now)

    binance_ask = btc_to_jpy.btc_to_jpy(exchanges_binance.binace_ask())
    print(bitbank_ask)
    print(binance_ask)

    if list_length_bitbank < MAXLENGTH and list_length_binance < MAXLENGTH and list_length_time < MAXLENGTH:
        list_bitbank_price.append(bitbank_ask)
        list_binance_price.append(binance_ask)
        list_time.append(now)
    else:
        # list内の要素がmaxlengthを超えたら、
        # 先頭の1要素を削除し、最後尾に追加します。
        if list_length_bitbank < MAXLENGTH:
            list_binance_price.pop(0)
            list_bitbank_price.append(bitbank_ask)

        if list_length_binance < MAXLENGTH:
            list_bitbank_price.pop(0)
            list_binance_price.append(binance_ask)

        if list_length_time < MAXLENGTH:
            list_time.pop(0)
            list_time.append(now)

    # ﾁｬｰﾄ用ﾃﾞｰﾀの作成をします。
    index = pd.DatetimeIndex(list_time)
    index = index.floor('S')

    bitbank_xrp = pd.Series(list_bitbank_price, index = index)
    list_length_bitbank = len(list_bitbank_price)

    binance_xrp = pd.Series(list_binance_price, index = index)
    list_length_binance = len(list_binance_price)

    # ここからﾁｬｰﾄ作成です
    plt.figure(1)
    ax.xaxis.set_major_locator(mdates.SecondLocator())
    bitbank_xrp_ohlc = bitbank_xrp.resample('B').ohlc()
    binance_xrp_ohlc = binance_xrp.resample('B').ohlc()
    print(bitbank_xrp_ohlc)
    ax_bitbank.clear()
    ax_binance.clear()
    bitbank_xrp_ohlc.plot(stacked = True, ax = ax_bitbank)
    binance_xrp_ohlc.plot(stacked = True, ax = ax_binance)
    plt.legend()  # チャート名表示
    plt.draw()
    plt.pause(.1)  # チャート画面を表示
    time.sleep(FREQUENCY)
