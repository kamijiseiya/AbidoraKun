"""XRPの売値をccxtを使用して取得しそれを利用してチャートを表示する"""
import time
import datetime
import ccxt
import numpy as np#インストールが必要
import matplotlib.pyplot as plt#インストールが必要

#http://okuribitoni.hatenablog.com/entry/2018/01/11/211204を参考にした。

PRICELIST = []
LISTLENGTH = 0
MAXLENGTH = 100 #ﾁｬｰﾄx方向最大値です。
FREQUENCY = 1 #ﾃﾞｰﾀ取得周期です。
EXCHANGE_LIST = ['bitbank',]#使用する取引所

ASK_EXCHANGE = ''
ASK_PRICE = 99999999
BID_EXCHANGE = ''
BID_PRICE = 99999999
print(ccxt.exchanges)

for exchange_id in EXCHANGE_LIST:


    while True:
        exchange = eval('ccxt.' + exchange_id + '()')

        # symbol: 通貨ペア 例(XRP/JPYは1リップルは日本円でいくらになるか。)
        orderbook = exchange.fetch_order_book(symbol='XRP/JPY')
        #bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None  # 買い注文=bids
        #print(bid)
        ask = orderbook['asks'][0][0] if orderbook['asks'] is not None else None  # 売り注文=asks
        print(ask)

        #現在の時刻を取得
        print(datetime.datetime.today())

        if LISTLENGTH < MAXLENGTH:
            PRICELIST.append(ask)
        else:
            #list内の要素がmaxlengthを超えたら、
            #先頭の1要素を削除し、最後尾に追加します。
            PRICELIST.pop(0)
            PRICELIST.append(ask)
        #ﾁｬｰﾄ用ﾃﾞｰﾀの作成をします。
        coincheck = np.array(PRICELIST)
        LISTLENGTH = len(PRICELIST)
        x = np.linspace(0, LISTLENGTH, LISTLENGTH)
        #ここからﾁｬｰﾄ作成です
        plt.figure(1)
        plt.plot(x, coincheck, label='bitbank(xrp/jpy)')
        #plt.plot(x,zaif, label = 'xrp/jpyの現在の買い最高値')
        plt.legend()
        plt.pause(.001)
        plt.clf()
        time.sleep(FREQUENCY)
