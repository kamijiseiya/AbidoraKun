import numpy as np
import pandas as pd
import json
import requests
from datetime import datetime
from pprint import pprint
import time

import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

#------------------------------------------
def sma(df, n):
    df = df.rolling(window=int(n)).mean()
    return df

def ewm(df, n):
    df = df.ewm(span=int(n)).mean()
    return df

#設定   ------------------------
GET_PERIODS = 60 * 5 # 時間足(秒)
GET_AFTER = 50 # 足本数

class GRAPHCREATION:
    def create_graph_png(self):
        # Cryptowatch API History Data   ------------------------
        now = datetime.now()
        now = int(now.timestamp())  # 現在時刻のUnixtime(秒単位)
        market = "kraken/"+ self  # 取引所と通貨ペアの取得（krakenを指定すれば大体の通貨ペアを習得できる。）
        get_periods = GET_PERIODS
        get_after = now - get_periods * GET_AFTER
        # HTTPライブラリ Requestsによる価格履歴取得
        r = requests.get(
            "https://api.cryptowat.ch/markets/" + market + "/ohlc?periods=" + str(get_periods) + "&after=" + str(
                get_after)).json()
        print("[ now :", now, "]", "[ periods :", get_periods, "]", "[ after :", get_after, "]")
        # Pandas OHLCデータ   ------------------------
        ohlcv = r["result"][str(get_periods)]
        df = pd.DataFrame(ohlcv, columns=["datetime", "open", "high", "low", "close", "volume", ''])
        df = df.set_index("datetime")

        # Indicator   ------------------------
        slider1_min, slider1_max, slider1_init, slider1_step = 1, 100, 15, 1
        slider2_min, slider2_max, slider2_init, slider2_step = 1, 100, 5, 1
        df_1 = sma(df["close"], slider1_init)
        df_2 = ewm(df["close"], slider1_init)

        print(df.head(5))
        print(df.iloc[len(df_1) - 1])

        # matplotlib -------------------
        plt.style.use("ggplot")  # matplotlib ggplot style読込

        plt.rcParams['figure.figsize'] = 9.7, 3.7  # 横970px、縦370px
        gs = GridSpec(4, 1, height_ratios=[6, 3, 0.2, 1])  # 縦４個、横１個のグリッドとその表示比率
        gs.update(left=0.1, bottom=0, right=0.95, top=0.95, hspace=0, )  # 全体の余白

        # 表示する線の描画

        ax0 = plt.subplot(gs[0])

        ax0.plot(df["close"], marker="o", markersize=1.5, linewidth=2, color="orange")
        ax0.plot(df["high"], linewidth=2, color="red")
        ax0.plot(df["low"], linewidth=0.7, color="orange")
        l1, = ax0.plot(df_1, linewidth=2, color="red")
        l2, = ax0.plot(df_2, linewidth=2, color="green")

        ax0.tick_params(axis="x", bottom=False, labelbottom=False)  # x軸目盛とラベルの非表示
        # ax0.axhline(0, color="orange")

        ax1 = plt.subplot(gs[1], sharex=ax0)
        ax1.spines["top"].set_color("slategray")  # ax0とax1の境界線
        ax1.bar(df.index, df["volume"], color="orange", width=get_periods * 0.94)

        plt.savefig('./config/img/'+self +'candlestick_week.png')

        plt.show()

if __name__ == "__main__":  # テスト用に追加
    print(GRAPHCREATION.create_graph_png("btcjpy"))