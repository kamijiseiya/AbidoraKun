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
    list_time = []
    list_ticker = []
    MAXLENGTH = 100  # 取得したﾃﾞｰﾀを保存する数
    FREQUENCY = 5  # ﾃﾞｰﾀ取得周期

    plt.ion()  # インタラクティブモードにする
    fig, ax = plt.subplots(1, 1)
    # 表示場所の設定
    ax_bitbank = plt.subplot(211)
    ax_ticker = plt.subplot(212, sharex=ax_bitbank)
    while True:
        # BITBANKでのXRP売値=bitbank_ask
        bitbank_id, bitbank_ask, bitbank_bid = BITBANK.currencyinformation('XRP')\
                if BITBANK.currencyinformation('XRP') is not None else None
        # 取引高を取得
        bitbank_ticker_json = BITBANK.tickers('XRP')
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
        plt.figure(1)
        ax.xaxis.set_major_locator(mdates.SecondLocator())
        bitbank_xrp_ohlc = bitbank_xrp.resample('30s').ohlc()
        tickers_resampled = tickers.resample('30s').max()
        ax_bitbank.clear()
        ax_ticker.clear()
        # ローソク足
        mpf.candlestick2_ohlc(ax=ax_bitbank, opens=bitbank_xrp_ohlc.open, highs=bitbank_xrp_ohlc.high,\
                lows=bitbank_xrp_ohlc.low, closes=bitbank_xrp_ohlc.close, width=1)
        # 取引高
        ax_ticker.set_ylim(bottom=20400000, top=20500000)
        tickers_resampled.plot(kind='bar', ax=ax_ticker)
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


# テスト用
if __name__ == "__main__":
    candlechart()
