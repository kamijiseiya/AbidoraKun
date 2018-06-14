'''入力されたデータに対してローソク足チャートを返す'''
import numpy as np
import matplotlib.pyplot as plt
import mpl_finance as mpf
from matplotlib import ticker
import matplotlib.dates as mdates
import pandas as pd

def candlechart(ohlc, width=0.8):
    '''入力されたデータフレームに対してローソク足チャートを返す
        引数:
            * ohlc:
                * データフレーム
                * 列名に'open', 'close', 'low', 'high'を入れること
                * 順不同
            * width: ローソクの線幅
        戻り値: ax: subplot'''
    #参考:https://qiita.com/u1and0/items/1d9afdb7216c3d2320ef

    fig, ax = plt.subplots()
    #ローソク足
    mpf.candlestick2_ohlc(ax, opens=ohlc.open.values, closes=ohlc.close.values,
                        lows=ohlc.low.values, highs=ohlc.high.values,
                        width=width, colorup='r', colordown='b')
    #x軸を時間にする
    xdate = ohlc.index
    ax.xaxis.set_major_locator(ticker.MaxNLocator(6))

    def mydate(x, pos):
        try:
            return xdate[int(x)]
        except IndexError:
            return ''

    ax.xaxis.set_major_formatter(ticker.FuncFormatter(mydate))
    ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')

    fig.autofmt_xdate()
    fig.tight_layout()

    return fig, ax
