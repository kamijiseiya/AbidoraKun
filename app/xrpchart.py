"""XRPの売値をccxtを使用して取得しそれを利用してチャートを表示する"""
import os
import sys
import datetime
import matplotlib.dates as mdates
import pandas as pd  # インストールが必要
import matplotlib.pyplot as plt  # インストールが必要
from matplotlib import ticker
import mpl_finance as mpf  #インストールが必要
from module.exchangess.bitbank import BITBANK
from module.exchangess.binance import BINANCE
sys.path.append(os.path.abspath(os.path.join('..')))
# 参考
# http://okuribitoni.hatenablog.com/entry/2018/01/11/211204
# https://teratail.com/questions/85572

def candlechart():
    """チャートを表示する"""
    list_bitbank_price = []
    list_binance_price = []
    list_time = []
    MAXLENGTH = 100  # 取得したﾃﾞｰﾀを保存する数
    FREQUENCY = 5  # ﾃﾞｰﾀ取得周期

    plt.ion()  # インタラクティブモードにする
    fig, ax = plt.subplots(1, 1)
    # 表示場所の設定
    ax_bitbank = plt.subplot(211)
    ax_binance = plt.subplot(212, sharex=ax_bitbank)
    while True:
        # BITBANKでのXRP売値=bitbank_ask
        bitbank_id, bitbank_ask, bitbank_bid = BITBANK.currencyinformation('XRP')\
                if BITBANK.currencyinformation('XRP') is not None else None
        # BINANCEでのXRP売値=binance_ask
        binance_ask = BINANCE.xrp(1)[1] if BINANCE.xrp(1)[1] is not None else None
        # 現在の時刻を取得
        now = datetime.datetime.now()

        if len(list_bitbank_price) < MAXLENGTH and len(list_binance_price) < MAXLENGTH\
                and len(list_time) < MAXLENGTH:
            list_bitbank_price.append(bitbank_ask)
            list_binance_price.append(binance_ask)
            list_time.append(now)
        else:
            # list内の要素がMAXLENGTHを超えたら、
            # 先頭の1要素を削除し、最後尾に追加する
            list_binance_price.pop(0)
            list_bitbank_price.append(bitbank_ask)

            list_bitbank_price.pop(0)
            list_binance_price.append(binance_ask)

            list_time.pop(0)
            list_time.append(now)

        # ﾁｬｰﾄ用ﾃﾞｰﾀの作成
        index = pd.DatetimeIndex(list_time, start=list_time[0])
        bitbank_xrp = pd.Series(list_bitbank_price, index=index)
        binance_xrp = pd.Series(list_binance_price, index=index)

        # ここからﾁｬｰﾄ作成
        plt.figure(1)
        ax.xaxis.set_major_locator(mdates.SecondLocator())
        bitbank_xrp_ohlc = bitbank_xrp.resample('30s').ohlc()
        binance_xrp_ohlc = binance_xrp.resample('30s').ohlc()
        ax_bitbank.clear()
        ax_binance.clear()
        # ローソク足
        mpf.candlestick2_ohlc(ax_bitbank, opens=bitbank_xrp_ohlc.open, highs=bitbank_xrp_ohlc.high,\
                lows=bitbank_xrp_ohlc.low, closes=bitbank_xrp_ohlc.close, width=1)
        mpf.candlestick2_ohlc(ax_binance, opens=binance_xrp_ohlc.open, highs=binance_xrp_ohlc.high,\
                lows=binance_xrp_ohlc.low, closes=binance_xrp_ohlc.close, width=1)

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
        plt.xlim(-0.5, 16.5)
        fig.autofmt_xdate()
        fig.tight_layout()

        plt.draw()
        plt.pause(FREQUENCY)  # チャート画面を表示


if __name__ == "__main__":
    candlechart()
